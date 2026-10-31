"""Run: python3 check_sapient_replies.py  (Python 3.10+, no dependencies or network).

Candidate Profile regression: match a task reply separately from interpreting its
status. The fixtures are selected fields from published examples, not packets.
Only ACCEPTED is translated here, and only to a candidate code, not an entire
CSAPI CommandStatus. This is not a SAPIENT decoder, device test or server test.
"""
from copy import deepcopy
from dataclasses import dataclass
from typing import Any
import unittest

Message = dict[str, Any]


@dataclass
class Decision:
    linked: bool
    native_reply: Message  # Preserve supplied evidence, even when unlinked.
    notes: tuple[str, ...]
    status_code_for_request: str | None = None


def destination(message: Message, body: Message) -> str | None:
    """Annex B prints the destination in the body; Dstl uses the envelope."""
    values = [part['destinationId'] for part in (message, body) if 'destinationId' in part]
    if not values or not all(isinstance(x, str) and x.strip() and x == values[0] for x in values):
        return None
    return values[0]


def assess(task: Message, reply: Message) -> Decision:
    """Direct request/reply in one source context. Never join on time or filenames."""
    native = deepcopy(reply)
    request, ack = task.get('task'), reply.get('taskAck')
    if not isinstance(request, dict) or not isinstance(ack, dict):
        return Decision(False, native, ('not a task/taskAck pair',))
    comparisons = (
        ('task ID', request.get('taskId'), ack.get('taskId')),
        ('responding node', destination(task, request), reply.get('nodeId')),
        ('reply destination', task.get('nodeId'), destination(reply, ack)),
    )
    bad = tuple(label for label, a, b in comparisons
                if not isinstance(a, str) or not a.strip() or a != b)
    if bad:
        return Decision(False, native, bad)
    if 'taskStatus' not in ack:
        return Decision(True, native, ('required source status absent',))
    status = ack['taskStatus']
    if status in ('TASK_STATUS_ACCEPTED', 'ACCEPTED'):
        return Decision(True, native, (), 'ACCEPTED')
    if status in ('TASK_STATUS_UNSPECIFIED', 'UNSPECIFIED'):
        return Decision(True, native, ('explicitly unspecified',))
    return Decision(True, native, ('status retained; outside this check',))


# BSI Flex 335 v2.0:2024-03, informative Annex B, Figs B.5/B.6, printed p. 93.
# https://www.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-flex-335.pdf#page=105
# Project transcription of correlation fields and times, not complete messages.
BSI_TASK = {'timestamp': '2022-11-03T10:29:39.941877200Z',
            'nodeId': '139bf8c7-84da-4c00-a068-4d58dca747b8',
            'task': {'destinationId': 'b902eb31-97f1-4acf-b994-da3ec901074e',
                     'taskId': '01GGYGM3F6FHSDDMVCQJ11ZNBF'}}
BSI_ACK = {'timestamp': '2022-11-03T10:33:04.819389200Z',
           'nodeId': 'b902eb31-97f1-4acf-b994-da3ec901074e',
           'taskAck': {'destinationId': '139bf8c7-84da-4c00-a068-4d58dca747b8',
                       'taskId': '01GGYGM3F6FHSDDMVCQJ11ZNBF'}}

# Dstl BSI-Flex-335-v2-Test-Harness, selected fields exactly as stored, not runtime messages.
# https://github.com/dstl/BSI-Flex-335-v2-Test-Harness/blob/6a2999d70d761d224914ddd8fa3f663af5005be0/SapientDmmSimulator/SapientDmmSimulator/Default.Task.Mode.json
# https://github.com/dstl/BSI-Flex-335-v2-Test-Harness/blob/6a2999d70d761d224914ddd8fa3f663af5005be0/SapientAsmSimulator/SapientAsmSimulator/Default.TaskAck.ModeChange.json
DSTL_TASK = {'timestamp': '2023-07-07T12:44:17.027638700Z',
             'nodeId': 'a8654cdf-4328-47de-81fa-c495589e30c9',
             'destinationId': 'a8654cdf-4328-47de-81fa-c495589e30c1',
             'task': {'taskId': '01H4R63D7NVN8444Z5M77WEBY6', 'command': {'modeChange': 'REQUEST'}}}
DSTL_ACK = {'timestamp': '2023-07-07T12:44:17.027638700Z',
            'nodeId': 'a8654cdf-4328-47de-81fa-c495589e30c9',
            'destinationId': 'a8654cdf-4328-47de-81fa-c495589e30c1',
            'taskAck': {'taskId': '01H4R63D7NVN8444Z5M77WEBY8', 'taskStatus': 'TASK_STATUS_ACCEPTED'}}


class PublishedCases(unittest.TestCase):
    def test_bsi_keep_matching_reply_without_inventing_status(self):
        result = assess(BSI_TASK, BSI_ACK)
        self.assertTrue(result.linked)
        self.assertEqual(result.native_reply, BSI_ACK)
        self.assertNotIn('taskStatus', result.native_reply['taskAck'])
        self.assertEqual(result.notes, ('required source status absent',))
        self.assertIsNone(result.status_code_for_request)

    def test_dstl_do_not_assign_accepted_to_another_task(self):
        result = assess(DSTL_TASK, DSTL_ACK)
        self.assertFalse(result.linked)
        self.assertEqual(result.native_reply, DSTL_ACK)
        self.assertEqual(result.native_reply['taskAck']['taskStatus'], 'TASK_STATUS_ACCEPTED')
        self.assertEqual(result.notes, ('task ID', 'responding node', 'reply destination'))
        self.assertIsNone(result.status_code_for_request)


class SyntheticControls(unittest.TestCase):
    """Deliberate variations of the printed examples, not additional evidence."""
    def test_matched_explicit_acceptance_is_not_discarded(self):
        ack = deepcopy(BSI_ACK)
        ack['taskAck']['taskStatus'] = 'TASK_STATUS_ACCEPTED'
        result = assess(BSI_TASK, ack)
        self.assertTrue(result.linked)
        self.assertEqual(result.status_code_for_request, 'ACCEPTED')

    def test_each_identity_field_independently_prevents_a_false_join(self):
        for field, expected in [('taskId', 'task ID'), ('nodeId', 'responding node'),
                                ('destinationId', 'reply destination')]:
            with self.subTest(field=field):
                ack = deepcopy(BSI_ACK)
                ack['taskAck']['taskStatus'] = 'TASK_STATUS_ACCEPTED'
                (ack if field == 'nodeId' else ack['taskAck'])[field] = 'different'
                result = assess(BSI_TASK, ack)
                self.assertFalse(result.linked)
                self.assertEqual(result.notes, (expected,))
                self.assertIsNone(result.status_code_for_request)

    def test_absent_ids_do_not_match_by_accident(self):
        req, ack = deepcopy(BSI_TASK), deepcopy(BSI_ACK)
        del req['task']['taskId'], ack['taskAck']['taskId']
        self.assertFalse(assess(req, ack).linked)

    def test_explicit_unspecified_is_not_absent_or_pending(self):
        ack = deepcopy(BSI_ACK)
        ack['taskAck']['taskStatus'] = 'TASK_STATUS_UNSPECIFIED'
        result = assess(BSI_TASK, ack)
        self.assertTrue(result.linked)
        self.assertEqual(result.notes, ('explicitly unspecified',))
        self.assertIsNone(result.status_code_for_request)

    def test_conflicting_destination_is_not_silently_repaired(self):
        ack = dict(BSI_ACK, destinationId='different')
        self.assertFalse(assess(BSI_TASK, ack).linked)


if __name__ == '__main__':
    unittest.main(verbosity=2)
