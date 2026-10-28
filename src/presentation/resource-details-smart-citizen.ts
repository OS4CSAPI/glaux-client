import { node, renderResourceDetailsTemplate } from './resource-details-template';
import './resource-details-case-study.css';

const sourceRoot = 'https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/';
const reference = (name: string, file: string): HTMLAnchorElement => {
  const link = node('a', undefined, name);
  link.href = sourceRoot + file;
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  return link;
};
function block(content: HTMLElement, title: string, explanation: string, source?: [string, string]): void {
  const section = node('section', 'rd-case-section');
  section.append(node('h3', undefined, title), node('p', undefined, explanation));
  if (source) section.append(reference(source[0], source[1]));
  content.append(section);
}
const i05: [string,string] = ['Individual and kind evidence (I05)', 'I05_Individual_System_and_Product_Kind_Mapping_v0.1_27OCT2026.md'];
const i06: [string,string] = ['Method evidence (I06)', 'I06_Procedure_and_Method_Mapping_v0.1_28OCT2026.md'];
const i07: [string,string] = ['Assembly evidence (I07)', 'I07_Composition_and_Component_Standing_Mapping_v0.1_28OCT2026.md'];
const i08: [string,string] = ['Digital representation evidence (I08)', 'I08_Digital_Representation_and_Five_Pass_Reconciliation_v0.1_28OCT2026.md'];
const i12: [string,string] = ['Critical mapping checks (I12)', 'I12_Critical_Interoperability_Challenge_v0.1_28OCT2026.md'];
function renderCaseContent(content: HTMLElement, category: string, view: string): void {
  const intro = node('p', 'rd-case-caption', 'Source-grounded product-design study · NOT a live equipment record');
  content.append(intro);
  if (category === 'operational' && view === 'Overview') {
    block(content, 'What are we looking at?', 'Smart Citizen Kit 2.3 is a documented environmental sensing product generation. The case does not identify one authenticated manufactured Kit. The Resource Details frame is a teaching surface, not a real CSAPI System resource.', i05);
    block(content, 'Individual vs model', 'SCK2.3 identifies a reusable design, not one System uniqueIdentifier. The individual-to-model association cannot be populated from the evidence.');
    block(content, 'What 13 steps earned', 'Five distinctions were traced to source evidence and compared to OGC standards. Four tempting but incorrect mappings were rejected. A real equipment-to-CSAPI exchange has not been demonstrated.', ['Integrated report (I13)', 'I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md']);
  } else if (category === 'operational' && view === 'Equipment') {
    block(content, 'Manufacturer-described assembly', 'Data Board and Urban Board connect physically. A separately cabled particulate sensor is secured inside the normal enclosure; battery and microSD support the Kit. This is product-design evidence, not an inspected serial-specific inventory.', i07);
    block(content, 'Sensing components are not channels', 'The SHT31 supports temperature and humidity; one AS7331 supports UV-A, UV-B and UV-C. These outputs are not five different physical Systems.');
    block(content, 'Installed equipment', 'Unknown: exact PM variant (SEN50/54/55), installed board revisions, serial numbers, attached optional sensors, replacement history and independent subsystem identities.');
  } else if (category === 'operational' && view === 'Condition') {
    block(content, 'No unit condition established', 'No verified battery condition, active firmware, configured operating mode, health/status or current reading exists in this case-study corpus. Product capabilities must not be displayed as actual device state.', ['Source audit (I04)', 'I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md']);
  } else if (category === 'operational' && view === 'Communications') {
    block(content, 'Documented capability', 'The product design includes data logging, Wi-Fi communication and a manufacturer platform. No active connection, session, signal quality or deployed CSAPI service was verified.', i08);
  } else if (category === 'operational' && view === 'Map') {
    block(content, 'No verified deployment', 'The research did not establish a physical Kit location or a confirmed association between an individual unit and a registered platform Device. No map pin is drawn.');
  } else if (category === 'activity' && view === 'Table') {
    block(content, 'No verified activity rows', 'The frozen example notebook includes references to platform IDs 18486–18489 but has zero saved outputs. There are no authenticated Observations, Commands or System Events for a particular Kit.', ['Source audit (I04)', 'I04_Independent_Evidence_Audit_and_Gate_A_v0.1_27OCT2026.md']);
    block(content, 'What the review prevented', 'A product table cannot be used as measured DataStream metadata. Parent-level discovery does not necessarily identify the direct producing System. Actual observation times and results cannot be invented.', i12);
  } else if (category === 'activity' && view === 'Charts') {
    block(content, 'No actual measurements to chart', 'A manufacturer-supported output channel is not a historical Observation. We intentionally show no mock trends or fabricated values.');
  } else if (category === 'commands') {
    block(content, 'No command evidence', 'This case study did not verify device tasking capabilities, an executable ControlStream, command parameters, requests or status. The existing Commands tabs are retained solely as wireframe navigation.');
  } else if (category === 'management' && view === 'Record') {
    block(content, 'Identity is unresolved', 'A product model, a platform registration ID, a MAC address, a token and a physical unit identifier have different roles. The advanced-station hardware-ID guidance cannot be transferred automatically to a basic SCK2.3.', i08);
    block(content, 'Software Component ≠ physical component', 'The vendor backend Component is a Device–Sensor-definition database association. It must not be blindly modeled as a physical subsystem.');
  } else if (category === 'management' && view === 'Configuration') {
    block(content, 'Options vs selected state', 'Manufacturer and firmware sources describe available sensor variants and methods. None proves which option or firmware version a particular Kit ran.', i06);
  } else if (category === 'management' && view === 'Sources') {
    block(content, 'Reproducible evidence', 'Four original manufacturer/project repositories were pinned by full commit; 60 source-native facts were recorded, with 34 independently audited. That supports documented design, not measured field-unit operation.', ['Pinned source corpus (I02)', 'I02_Versioned_Source_Corpus_Register_v0.1_27OCT2026.md']);
    block(content, 'DIM vs CSAPI vs proof', 'A concept can be meaningful, a standard can accommodate it, and yet no source-verified resource can be populated. The finished case study has a conditional Gate D assessment.', ['I13 final case study', 'I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md']);
  }
}

export function renderResourceDetailsSmartCitizen(container: HTMLElement): void {
  renderResourceDetailsTemplate(container, {
    pageTitle: 'Smart Citizen Kit 2.3 · DIM research test drive',
    pageIntro: 'A guided reading of the completed 13-step study inside the existing Resource Details wireframe. Manufacturer design evidence is kept separate from unknown real-unit state.',
    renderBlankContent({categoryId, view, content}) { renderCaseContent(content, categoryId, view); return true; },
    sourceSummary: 'Study standing, source records and limitations',
    sourceDescription: 'This is a standalone, source-linked product-design demonstration. It reuses the 560 × 440 wireframe, and does not fetch a real device, mint an identifier, provide operational readings or assert application-profile conformance.',
    designRecord: 'Research/DIM_Profile_V2/Case_Studies/Real_Equipment_DIM_Validation/I13_Integrated_Smart_Citizen_Case_Study_and_Gate_D_v0.1_28OCT2026.md',
  });
  const frame = container.querySelector<HTMLElement>('.rd-module');
  const title = frame?.querySelector<HTMLElement>('.rd-resource-name');
  if (title) title.textContent = 'Smart Citizen Kit 2.3 · product design';
  const fields = frame?.querySelectorAll<HTMLElement>('.rd-identity-fields dd');
  if (fields && fields.length >= 3) {
    fields[0].textContent = 'Manufacturer-described sensing equipment';
    fields[1].textContent = 'Physical individual: not verified';
    fields[2].textContent = 'Pinned Smart Citizen documentation / firmware';
  }
  const footer = frame?.querySelector<HTMLElement>('.rd-module-footer span');
  if (footer) footer.textContent = 'Research case · no live unit or readings';
}
