# Standard access and source capture boundary

Only an offline library-availability check exists today. No endpoint is configured
and no requests are made.

Future access code belongs here and must retain original response bytes and
relevant request/response metadata independently of parsing and derived models.
Preserve media type, subject, time, units, provenance, uncertainty, and unknown
content. A parsed library object is not a substitute for the source representation.
Authentication, HTTP error handling, and pagination remain consumer responsibilities
where the library does not provide them.
