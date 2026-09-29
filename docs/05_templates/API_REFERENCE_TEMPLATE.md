# API Reference: <service name> v<version>

Base URL: `http://localhost:8000` (local demo). Auth: <none/API key/OAuth>. Format: JSON, UTF-8.

## Conventions
Errors: `{"error": {"code": "string", "message": "string"}}`. Rate limits: <n/min>. Versioning: `/v1`. Timestamps: ISO 8601 (UTC).

## Endpoints

### `POST /v1/<resource>`
Purpose: ...

Request
```json
{"text": "example input", "language": "en"}
```
Response `200`
```json
{"id": "abc123", "label": "needs_review", "confidence": 0.62, "explanation": "Reason in plain language", "human_review_required": true}
```
| Field | Type | Required | Description |
|---|---|---|---|
| text | string | yes | Input, max 2,000 chars |
| language | string | no | ISO 639-1/639-3 code |

Status codes: 200 OK | 400 invalid input | 401 unauthorised | 429 rate limited | 500 server error.

### `GET /v1/health`
Returns `{"status":"ok","version":"x.y.z"}`.

## Privacy notes
What is logged, retention, how to request deletion.

## Changelog
| Version | Date | Change |
|---|---|---|
