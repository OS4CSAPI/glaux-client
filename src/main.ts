import { csapiLibraryStatus } from './data/library';
import { renderLanding } from './presentation/landing';
import './presentation/style.css';

const app = document.querySelector<HTMLElement>('#app');
if (!app) {
  throw new Error('The application mount point #app is missing.');
}

renderLanding(app, csapiLibraryStatus());
