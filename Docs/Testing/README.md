# Testing

Destination for test plans, acceptance criteria, evaluation methods, and concise
results linked to supporting evidence. No new evaluation method or profile
benefit is established by creating this folder.

Current checks and commands are documented in the [root README](../../README.md#setup).
The [offline CSAPI smoke tests](../../tests/csapi.smoke.test.ts) exercise the actual
pinned library; the [CI workflow](../../.github/workflows/ci.yml) runs installation,
type-checking, tests, and production build. The
[bootstrap CI run](https://github.com/OS4CSAPI/glaux-client/actions/runs/39970543341)
passed these checks for commit `1641f23d4981bceb94c62e80df94ee1fbe9af88b`;
it does not demonstrate device integration or a profile advantage.

Keep executable tests and fixtures in their appropriate code directories.
Link to those sources and dated, revision-specific evidence rather than copying
them into documentation or presenting planned checks as completed results.

The [browser verification record](BROWSER_VERIFICATION.md) contains the original
23-check regression and the 44-check power-arrangement run, with actual results,
selected screenshots, and reproducible commands. The current offline test/build
status and live-deployment boundary are in [CURRENT_WORK](../Plans/CURRENT_WORK.md).

Return to the [documentation index](../README.md).
