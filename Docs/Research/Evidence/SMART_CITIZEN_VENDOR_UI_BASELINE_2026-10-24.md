# Smart Citizen vendor presentation baseline

Recorded 24 October 2026 for the Smart Citizen integration study. This record fixes two first-party presentation examples before the CSAPI adapter and Glaux comparison are implemented. The screenshots are historical documentation examples and are not represented as current views of public registration 19639.

## Why these figures were selected

Smart Citizen's Data Platform documentation states that its website provides near-real-time device-data exploration with contextual information such as maps and keywords. The onboarding guide instructs users to visit the Kit after it begins publishing and then scroll down to perform basic explorations. The Data Tools guide separately describes the Smart Citizen Map as the classic map with simple time-series plots and metric comparisons and describes a JavaScript dashboard with status, filtering, customizable time series, WebSocket notifications, and CSV download. These statements provide first-party descriptions of intended presentation roles rather than requiring the study to infer them from pixels alone.

## Figure 6 source: core platform measurement exploration

| Field | Record |
| --- | --- |
| Local study file | `Docs/Research/Studies/Smart_Citizen/figures/smart_citizen_platform_basic_exploration.png` |
| Source repository | `fablabbcn/smartcitizen-docs` |
| Source revision | `cf918c306474112f99ccf21bcbe869b9865b0823` |
| Source path | `docs/assets/images/onboarding_10.png` |
| Git blob | `f600ff9726fc127c325f5abadb5b75e00074493b` |
| Image properties | PNG, 2784 × 1778 pixels, 767,030 bytes |
| Source page | https://docs.smartcitizen.me/guides/getting-started/onboarding-your-kit/, “Visit your Kit” |
| Changes | None to source pixels or bytes; Word display scaling only |

The screenshot visibly shows Smart Citizen kit page 14410, the device name “Hola,” a 44 percent battery indication, and “LAST DATA RECEIVED: JULY 14, 2021 - 12:58.” Its top measurement strip includes light, noise, air temperature, humidity, barometric pressure, PM2.5, PM10, and PM1 with values and units. PM2.5 is selected in the detail area with a property explanation, a 2 µg/m³ value, date controls, and a time-series graph. These visible facts describe the historical documentation example only.

## Figure 7 source: Smart Citizen custom dashboard

| Field | Record |
| --- | --- |
| Local study file | `Docs/Research/Studies/Smart_Citizen/figures/smart_citizen_custom_dashboard.png` |
| Source repository | `fablabbcn/smartcitizen-docs` |
| Source revision | `cf918c306474112f99ccf21bcbe869b9865b0823` |
| Source path | `docs/assets/images/dashboard.png` |
| Git blob | `8057e992f064fb3d0edfd7a94cd1b4e3c1dbd2d0` |
| Image properties | PNG, 2560 × 1468 pixels, 309,762 bytes |
| Source page | https://docs.smartcitizen.me/data/data-tools/, “Web tools”; also used in the “Live demos” dashboard guide |
| Changes | None to source pixels or bytes; Word display scaling only |

The screenshot identifies device “ERLIO” as “Smart Citizen Kit 2.1 with Urban Sensor Board.” Visible panels show temperature at 23°C and humidity at 63 percent, identify SHT31 beside both quantities, and plot multi-day trends dated 23–29 June 2022; the lower edge also shows PM2.5 and PM10 headings and current values. The Data Tools documentation characterizes this dashboard as a separate JavaScript dashboard rather than the classic Smart Citizen Map. It is therefore retained as an alternate official presentation example, not as a substitute for a current selected-device capture.

## Rights and attribution

The source repository publishes a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license, and the Smart Citizen documentation site also publishes a GNU Free Documentation License notice except where otherwise noted. The existing paper figure-source record retains both general notices because the inspected image contexts do not identify an image-specific override or reconcile the two notices. Both screenshots remain credited to Smart Citizen / Fab Lab Barcelona and are reproduced without pixel alteration. Their inclusion does not imply Smart Citizen endorsement of MERLIN, Glaux, or the conclusions of this study.

## Experimental boundary

Figures 6 and 7 establish source-provider presentation context before the standards-based reconstruction is available. They do not provide a matched comparison because they depict different historical devices and times from public registration 19639. The study will attempt to obtain a contemporaneous selected-registration view for Figure 8 if the public interface can reproduce the relevant evidence; if it cannot, that limitation will be reported explicitly. Figures 9 and 10 remain reserved for the executed Glaux comparison and CSAPI relationship/source-to-display trace.
