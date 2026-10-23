# Standard access and source capture boundary

`client.ts` reads a supplied HTTP(S) resource with GET and no credentials. It
captures the original Fetch-exposed response bytes, decoded text, parsed JSON,
exposed headers, status, URLs, and retrieval time. A resource may advertise one
SensorML `alternate` or `describedby` link; the client follows at most one such
typed link and retains both responses. No endpoint paths are guessed.

Access code belongs here and must retain original response bytes and
relevant request/response metadata independently of parsing and derived models.
Preserve media type, subject, time, units, provenance, uncertainty, and unknown
content. A parsed library object is not a substitute for the source representation.
`standard.ts` uses the real pinned CSAPI/SensorML/SWE functions for supported
projections and separately extracts inspectable standard facts. Parser results
are not whole-schema validation. Unsupported, malformed, and unfamiliar data
remain available with source paths and warnings. Declared resource subjects and
literal source times remain separate from transport retrieval time.

HTTP and invalid-JSON errors retain any received body in `ResourceReadError.capture`.
The UI exposes it in Standard view. Browser CORS applies; authentication,
collection discovery, pagination, and writes are outside this increment.
