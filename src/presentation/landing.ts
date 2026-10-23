export function renderLanding(container: HTMLElement, libraryStatus: string): void {
  container.innerHTML = `
    <p class="eyebrow">OS4CSAPI experimental prototype</p>
    <h1>Glaux Client</h1>
    <p class="intro">Evaluating standards-based sensor-system integration,
      profile-aware interpretation, and operator-centered interfaces.</p>
    <section aria-labelledby="purpose">
      <h2 id="purpose">A foundation for comparison</h2>
      <p>Future work will compare generic CSAPI, SensorML, and SWE Common access
        with MERLIN domain information model and Managed Physical Sensing Systems
        (MPSS) profile interpretation of the same server-hosted information.</p>
      <p>TRSS unattended ground sensors and McQ OmniSense II motivate this
        evaluation. Their distinct source meaning must remain intact.</p>
    </section>
    <section aria-labelledby="status">
      <h2 id="status">Bootstrap only</h2>
      <p>No TRSS or OmniSense integration is complete, and no profile benefit has
        been demonstrated. There are no live requests or device controls.</p>
      <p id="library-status"></p>
      <p>Existing Overview, Equipment, and Condition wireframes are the intended
        future starting scope, subject to consulting their actual source materials.</p>
    </section>
    <footer>
      <p>Intended for possible future contribution to the Glaux effort.
        No adoption or endorsement by DGIWG or another organization is claimed.</p>
      <a href="/THIRD_PARTY_NOTICES.txt">Third-party notices</a>
    </footer>
  `;

  const status = container.querySelector('#library-status');
  if (!status) {
    throw new Error('The landing page library-status element is missing.');
  }
  status.textContent = libraryStatus;
}
