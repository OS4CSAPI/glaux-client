/** Exact identifiers used in the unpublished MPSS v0.3.5 source catalogue. */
export const MPSS = 'https://schemas.example/merlin/mpss/0.3/';

/** Deliberately separate from MPSS: provisional, local application experiments. */
export const EXPERIMENT = 'https://example.invalid/glaux-client/experiment/v1/';

export const mpssGroup = (name: string): string => `${MPSS}group/${name}`;
export const mpssTerm = (name: string): string => `${MPSS}term/${name}`;
export const experimentGroup = (name: string): string => `${EXPERIMENT}group/${name}`;
export const experimentTerm = (name: string): string => `${EXPERIMENT}term/${name}`;
