# Evidence Handling

## Principles

- Collect the minimum evidence required.
- Prefer synthetic records.
- Mask personal and secret data.
- Do not download complete datasets.
- Encrypt evidence at rest and in transit.
- Restrict access to named engagement personnel.
- Maintain timestamps and source context.
- Define retention and deletion dates.

## Never place in reports

- Full passwords
- Full API keys or tokens
- Session cookies
- Complete connection strings
- Complete personal records
- Government identifiers
- Payment card data
- Large database samples

## Evidence naming

```text
ENGAGEMENT-FINDINGID-YYYYMMDD-HHMMSS-artifact.ext
```

## Chain-of-custody fields

- Evidence ID
- Collector
- Date and time zone
- Source asset
- Collection method
- Original hash
- Sanitized hash
- Storage location
- Access list
- Retention deadline

## Accidental sensitive-data access

1. Stop querying.
2. Capture only minimal proof.
3. Do not browse adjacent records.
4. Notify the approved contact.
5. Follow incident and evidence instructions.
6. Document what was accessed and whether it was retained.

Use the redaction CLI as an aid, then inspect the result manually.
