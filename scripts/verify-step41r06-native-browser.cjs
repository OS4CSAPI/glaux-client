// Read-only browser proof of one generic native CSAPI→Profile→Glaux path.
// Requires Vite and 41R-05 isolated test producer on separate loopback ports.
const assert=require('node:assert/strict');
const fs=require('node:fs');
const {chromium}=require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const app=process.env.GLAUX_BASE_URL||'http://127.0.0.1:5173';
const base=process.env.GLAUX_NATIVE_PRODUCER_BASE||'http://127.0.0.1:8015/api';
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.GLAUX_CHROMIUM_EXECUTABLE||undefined,headless:true});
 const page=await browser.newPage({viewport:{width:1280,height:900}});
 const errors=[],requests=[],verified=[];
 page.on('pageerror',e=>errors.push(e.message));
 page.on('request',r=>{if(r.url().startsWith(base))requests.push({method:r.method(),url:r.url()});});
 const check=(name,v)=>{assert(v,name);verified.push(name);};
 const wait=async phrase=>page.waitForFunction(s=>(document.querySelector('.rdp-count')?.textContent||'').includes(s),phrase);
 const panel=()=>page.locator('#rd-content-panel');
 const view=async(group,tab)=>{await page.locator('#rd-category-'+group).click();await page.locator('#rd-view-'+tab).click();};
 try{
  const url=base+'/procedures/dragino-s31-lb';
  await page.goto(app+'/?page=resource-details-profile-test&native='+encodeURIComponent(url));
  await wait('21 source claims');
  check('existing frame',await page.locator('#rd-module').count()===1);
  check('native Procedure', (await panel().innerText()).includes('NATIVE CSAPI GEOJSON FEATURE'));
  check('native and profile HTTP discovered',requests.some(r=>r.url===url)&&
    requests.some(r=>r.url.endsWith('/profiles/dim-csapi-source-evidence/v0.1'))&&
    requests.some(r=>r.url.endsWith('/evidence/dragino-s31-lb')));
  await view('management','configuration');
  const configuration=await panel().innerText();
  check('documented default vs example vs unknown',configuration.includes('configuration.documented_default')&&
    configuration.includes('SOURCE_EXAMPLE')&&configuration.includes('UNKNOWN'));
  await view('management','record');
  check('native raw feature and sidecar both retained',
    (await panel().innerText()).includes('Original native CSAPI GeoJSON Feature')&&
    (await panel().innerText()).includes('Linked producer evidence document'));
  await page.locator('#rdp-native-url').fill(base+'/systems/bennetts-point-acebpmet');
  await page.locator('#rdp-load-native').click();
  await wait('37 source claims');
  check('same frame now historical System',await page.locator('#rd-module').count()===1&&
    (await page.locator('.rdp-count').innerText()).includes('Native CSAPI System'));
  check('two originals four copies',(await page.locator('.rdp-count').innerText()).includes('2 original source-event anchors')&&
    (await page.locator('.rdp-count').innerText()).includes('4 historical experiment copies'));
  await view('activity','table');
  const activity=await panel().innerText();
  check('NOAA originals and exact QA/derived/unknown preserved',activity.includes('CSV line 10130')&&
    activity.includes('CSV line 10418')&&activity.includes('"<0> "')&&
    activity.includes('DERIVED')&&activity.includes('UNKNOWN'));
  await view('operational','equipment');
  const equipment=await panel().innerText();
  check('station point not sensor coordinates',equipment.includes('location.station_position')&&
    equipment.includes('location.probe_position'));
  await view('operational','map');
  check('no invented per-probe map pin',await page.locator('.rd-map-empty').count()===1);
  // The producer's original data is unchanged. Corrupt one linked response in
  // transit to prove a real browser refuses mismatched Profile evidence.
  await page.route('**/api/evidence/bennetts-point-acebpmet',async route=>{
    const response=await route.fetch();
    const doc=await response.json();
    doc.describes.uid='urn:invalid:other-native-resource';
    await route.fulfill({response,json:doc});
  });
  await page.locator('#rdp-load-native').click();
  await wait('Native raw-only');
  check('browser rejects mismatched UID and does not render qualified source claims',
    (await page.locator('.rdp-count').innerText()).includes('identity') &&
    (await panel().innerText()).includes('Native CSAPI feature — raw-only fallback') &&
    !(await panel().innerText()).includes('Source-original reports — count each original ONCE'));
  await page.unroute('**/api/evidence/bennetts-point-acebpmet');
  check('read-only local producer requests',requests.length>=6&&requests.every(r=>r.method==='GET'));
  check('no browser script errors',errors.length===0);
  fs.mkdirSync('artifacts',{recursive:true});
  fs.writeFileSync('artifacts/step41r06-native-browser.json',JSON.stringify({
    checks:verified.length,result:'passed',checked:verified,requests,errors,
    scope:'isolated native CSAPI/linked project Profile/one Glaux client, not full OGC ATS or original issuer proof',
  },null,2));
  process.stdout.write(JSON.stringify({checks:verified.length,result:'passed',requests:requests.length},null,2)+'\n');
 }finally{await browser.close();}
})().catch(e=>{process.stderr.write(String(e.stack||e)+'\n');process.exitCode=1;});
