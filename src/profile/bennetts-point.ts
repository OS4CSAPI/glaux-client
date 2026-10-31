export const attributionCaseKey = 'bennetts-point';

export interface AttributionRecord {
  timestamp: string;
  displayTime: string;
  property: string;
  value: number;
  unit: string;
  quality: string;
  qualityMeaning: string;
  probe: { label: string; serial: string };
}

export const attributionCase = {
  station: { name: "Bennett's Point", code: 'acebpmet' },
  model: { manufacturer: 'Campbell Scientific', designation: 'EE181', label: 'Air temperature and relative humidity probe' },
  records: [
    {
      timestamp: '2024-04-15T17:00:00Z',
      displayTime: '15 Apr 2024 · 12:00 EST',
      property: 'Air temperature',
      value: 29.1,
      unit: '°C',
      quality: '<0>',
      qualityMeaning: 'Passed initial QA/QC checks',
      probe: { label: 'Temp/RH sensor 4', serial: '222016000109CE' },
    },
    {
      timestamp: '2024-04-18T17:00:00Z',
      displayTime: '18 Apr 2024 · 12:00 EST',
      property: 'Air temperature',
      value: 27.3,
      unit: '°C',
      quality: '<0>',
      qualityMeaning: 'Passed initial QA/QC checks',
      probe: { label: 'Temp/RH sensor 3', serial: '21281600077814' },
    },
  ] satisfies AttributionRecord[],
  sources: [
    {
      label: "NOAA NERRS Bennett's Point meteorology, 2024",
      url: 'https://cdmo.baruch.sc.edu/waf/swmp_data_archives/acebpmet2024.csv',
    },
    {
      label: 'ACE Basin NERR 2024 meteorological metadata and equipment history',
      url: 'https://cdmo.baruch.sc.edu/waf/YearlyFiles/ACE%20Basin/meteorological/metadata/acemet01-12.24m.pdf',
    },
    {
      label: 'Candidate Profile — probe swap and observation attribution',
      url: 'https://github.com/OS4CSAPI/glaux-client/blob/research/dim-profile-v2/Docs/Research/DIM_Profile_V2/Candidate_Specification/CSAPI_Profile.md#which-probe-measured-the-air-temperature',
    },
  ],
  note: 'The station measurement rows contain the air-temperature value, timestamp and quality flag but not the probe serial. The serial attribution was prepared from the operator\'s dated equipment history before this display.',
} as const;
