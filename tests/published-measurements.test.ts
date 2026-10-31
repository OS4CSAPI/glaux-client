import { expect, test } from 'vitest';
import { descriptions, examples, measurementRows, measures, readingText } from '../src/profile/published-measurements';

test('preserves the example readings and does not turn ClimaVue capabilities into observations',()=>{
  expect(measures.map(r=>[r.field.name,readingText(r)])).toEqual([
    ['temperature','27.2 °C'], ['relativeHumidity','56.6 %'], ['PanelTemp','25.91098 °C'],
    ['airTemperature','No reading supplied'], ['humiditySensorTemperature','No reading supplied']]);
});
test('air is shared across makes, but neither equipment temperature qualifies as air temperature',()=>{
  const air='http://vocab.nerc.ac.uk/standard_name/air_temperature/';
  expect(measures.filter(r=>r.field.definition===air).map(r=>r.value)).toEqual([27.2,undefined]);
  expect(new Set(measures.filter(r=>r.context!=='S31-LB probe example').map(r=>r.field.definition)).size).toBe(3);
});
test('wrong source or output and duplicate values are rejected; zero is a real number, not missing',()=>{
  const logger=examples[1];
  expect(()=>measurementRows(descriptions,[{...logger,context:descriptions[2].context}])).toThrow();
  expect(()=>measurementRows(descriptions,[{...logger,output:descriptions[2].output.name}])).toThrow();
  expect(()=>measurementRows(descriptions,[logger,logger])).toThrow();
  const row=measurementRows(descriptions,[{...logger,values:{PanelTemp:0}}]).find(r=>r.field.name==='PanelTemp');
  expect(readingText(row!)).toBe('0 °C');
});
