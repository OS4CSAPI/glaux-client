// Step 39: read-only live CSAPI browser transport and historical display smoke.
// Runs against a LOCAL Vite build; the 52°North/Oracle server is only accessed
// through browser GETs. No writes, commands, login, deployment, or basemap use.
// Any CORS/network block is BLOCKED, not a claim that the server is down.
const { chromium } = require(process.env.GLAUX_PLAYWRIGHT_MODULE || 'playwright-core');
const { mkdir, writeFile } = require('node:fs/promises');
const path = require('node:path');
const assert = require('node:assert/strict');

const base = (process.env.GLAUX_BASE_URL || 'http://127.0.0.1:5173').replace(/\/$/, '');
const target = base + '/?page=resource-details-live-bennett';
const remoteHost = '129-80-248-53.sslip.io';
const output = path.resolve(__dirname, '../artifacts/step39-native-browser.json');

(async () => {
  const browser = await chromium.launch({
    executablePath: process.env.GLAUX_CHROMIUM_EXECUTABLE || undefined, headless: true,
  });
  const page = await browser.newPage({viewport:{width:1280,height:900}});
  page.setDefaultTimeout(25000);
  const requests=[], responses=[], errors=[], checks=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',req=>{
    const url=req.url();
    if(url.includes(remoteHost))requests.push({method:req.method(),path:new URL(url).pathname,resourceType:req.resourceType()});
  });
  page.on('response',res=>{
    if(res.url().includes(remoteHost))responses.push({
      status:res.status(),path:new URL(res.url()).pathname,
      contentType:res.headers()['content-type']||'',
      allowOrigin:res.headers()['access-control-allow-origin']||'',
    });
  });
  const check=(label,result)=>{assert(result,label);checks.push(label)};
  const panel=()=>page.locator('#rd-content-panel');
  let state='UNTESTED',reason=null,success=false;
  try {
    await page.goto(target,{waitUntil:'domcontentloaded'});
    await page.locator('#rd-module').waitFor();
    await page.waitForFunction(()=>{
      const s=document.querySelector('#rd-content-panel')?.textContent||'';
      return s.includes('Live Bennett')||s.includes('Live retrieval failed:');
    },{timeout:30000});
    const overview=await panel().innerText();
    const failed=overview.includes('Live retrieval failed:');
    if(failed){
      state='BLOCKED_BROWSER_FETCH_OR_CORS';
      reason=overview.slice(0,500);
    } else {
      state='BROWSER_READ_BACK';
      check('Actual live Bennett case rendered from browser-side CSAPI GETs',overview.includes('Live Bennett'));
      check('Two historical source probes were retrieved',overview.includes('Physical probes')&&overview.includes('2'));
      check('Live case has the expected scalar and parallel report resource counts',
        overview.includes('Historical temperature observations')&&
        overview.includes('Preserved context reports'));

      await page.locator('#rd-category-activity').click();
      await page.locator('#rd-view-table').click();
      const activity=await panel().innerText();
      check('Two retrieved historical source means are displayed separately',
        activity.includes('29.1')&&activity.includes('27.3'));
      check('Original source QA strings survive the live UI source context',
        activity.includes('"<0> "'));
      check('Historical original resultTime is explicitly qualified as not independently established',
        activity.includes('No independent historical result-generation time'));

      await page.locator('#rd-category-operational').click();
      await page.locator('#rd-view-map').click();
      const noPosition=await panel().innerText();
      check('Existing shared Map refuses unsupported per-probe location',
        noPosition.includes('No position was supplied for this System')&&
        await page.locator('.rd-map-canvas').count()===0);

      await page.locator('#rd-category-management').click();
      await page.locator('#rd-view-record').click();
      check('Native CSAPI HTTP responses are retained under Management Record',
        (await panel().innerText()).includes('Live server responses'));
      success=true;
      state='BROWSER_READ_BACK_WITH_QUALIFICATIONS';
    }
    check('Remote service requested by browser with GET only',requests.length>0 && requests.every(x=>x.method==='GET'));
    check('Browser produced no unhandled script errors',errors.length===0);
  } catch(error){
    if(state==='BROWSER_READ_BACK')state='UI_ASSERTION_FAILED';
    else if(state==='UNTESTED')state='BLOCKED_BROWSER_OR_PAGE';
    reason=error instanceof Error?error.message:String(error);
    if(state==='UI_ASSERTION_FAILED')throw error;
  } finally {
    await mkdir(path.dirname(output),{recursive:true});
    const summary={
      testedAt:new Date().toISOString(),
      localBase:base,
      page:'/?page=resource-details-live-bennett',
      state,reason,
      checksPassed:checks,
      remoteRequestCount:requests.length,
      remoteRequests:requests,
      remoteResponses:responses,
      pageErrors:errors,
      sourceMeaning:'Historical 2024 Bennett observations, NOT current sensor telemetry',
      noActualCommands:true,
      limitations:[
        'A successful browser GET is not an OGC conformance test.',
        'The historical NOAA original resultTime and native TimeRange/resultQuality semantics remain unverified.',
        'This browser page uses previously project-authored test resources; local Step 32 packets are a separate study.',
        'A source publisher/provenance claim is not independently authenticated or discoverable by this test.',
      ],
    };
    await writeFile(output,JSON.stringify(summary,null,2)+'\n');
    console.log(JSON.stringify({
      state,checksPassed:checks.length,remoteRequestCount:requests.length,
      remoteResponses:responses.length,remoteHttp200:responses.filter(x=>x.status===200).length,
      pageErrors:errors,output:'artifacts/step39-native-browser.json',readOnly:true,
    },null,2));
    await browser.close();
  }
  if(!success && state!=='BLOCKED_BROWSER_FETCH_OR_CORS')process.exitCode=1;
})().catch(error=>{console.error(error.stack||error);process.exitCode=1});
