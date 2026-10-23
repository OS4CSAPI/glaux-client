import { CSAPIResourceTypes } from '@camptocamp/ogc-client/csapi';

export function csapiLibraryStatus(): string {
  if (!CSAPIResourceTypes.includes('systems')) {
    throw new Error('The installed CSAPI library is missing the systems resource type.');
  }
  return 'Pinned CSAPI library loaded (phase-10 revision 4ca1d7d).';
}
