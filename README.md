# Web Service Sample

A lightweight FastAPI web service for testing HTTP requests, with a simple user-authorization check backed by a YAML file. It is intended for quick validation of Power Automate Desktop or similar automation workflows.

## Overview

This project exposes a few basic endpoints and demonstrates:

- a simple GET API for greeting or returning the current date/time
- a POST API that validates a username against a YAML-based user list
- role and permission data returned for authorized users
- example usage patterns for automation tools and manual API testing

## Project structure

- `main.py` — FastAPI application and route definitions
- `current_date.py` — helper for returning the current date/time string
- `users.yaml` — username-to-role lookup used by the authorization endpoint
- `tester.py` — sample code for interacting with the service
- `pyproject.toml` — project metadata and Python dependencies

## Requirements

- Python 3.12+
- `fastapi`
- `uvicorn`
- `pyyaml`
- `requests`

## Setup

From the project root:

```bash
python -m venv .venv
. .venv/bin/activate  # Linux/macOS
# or .\.venv\Scripts\Activate.ps1  # Windows PowerShell
pip install -U pip
pip install -e .
```

If using `uv`, this is also supported:

```bash
uv sync
```

## Run the service

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The app is then available at:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/user/

## API endpoints

### GET /

Returns either a greeting or the current date/time.

Query parameters:

- `option` (required): `greet` or `date`
- `user` (optional): username used in the greeting response

Examples:

```bash
curl "http://127.0.0.1:8000/?option=greet&user=admin"
curl "http://127.0.0.1:8000/?option=date"
```

Example response:

```json
{"message": "Hello, admin!"}
```

```json
{"message": "2026-09-12 10:15"}
```

### POST /user/

Accepts a JSON body containing a username and checks it against the `users.yaml` file.

Request body:

```json
{"username": "admin"}
```

Example:

```bash
curl -X POST "http://127.0.0.1:8000/user/" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin"}'
```

Example success response:

```json
{
  "username": "admin",
  "role": "administrator",
  "permission": true,
  "expires": "2026-09-12 11:16"
}
```

Example unauthorized response:

```json
{
  "username": "unknown-user",
  "role": "Not authorized user!",
  "permission": false,
  "expires": "-"
}
```

## User data

The authorization lookup is defined in `users.yaml`:

```yaml
admin:
  role: administrator
guest:
  role: user
support:
  role: administrator
operator:
  role: user
```

Authorized users receive a role and a one-hour expiration timestamp. Unknown users are rejected with `permission: false`.

## Example automation usage

This service is useful for testing HTTP-based automation from tools like Power Automate Desktop, for example:

- sending a GET request to verify connectivity
- submitting a username to validate access rights
- checking whether a workflow receives expected JSON responses

## Maintainer

- Christoforos Chatzitheodorou
- christoforos.chatzitheodorou@gmail.com