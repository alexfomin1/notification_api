# Notification_api
Notification API via Django REST API

## Setting up
1. Download this project
2. Download and run docker
3. Run `docker-compose up -d --build`
4. Research the app with urls below
5. Use `docker compose stop` to stop the system


## Guide in API urls
- `api/v1/clients/` - clients list, options: GET, POST, HEAD, OPTIONS
- `api/v1/distibs/` - distribs list, options: GET, POST, HEAD, OPTIONS
- `api/v1/messages/` - messages list, options: GET, POST, HEAD, OPTIONS
- `api/v1/tags/` - tags list, options: GET, POST, HEAD, OPTIONS
- `/admin/` - admin panel with Web UI
- `/metrics/` - Prometheus metrics
- `/api/token/` - get tokens
- `/api/token/refresh/` - refresh access token with refresh token
- `/api/token/verify/` - authenticate with access token
- `/docs/` - Swagger UI documentation (Open API) format
- `http://127.0.0.1:9090` - Prometheus metrics

## Algorithm's logic:
1. Function `check()` in `scheduler/s_check/` scheduled to check new suitable ditributions every 10 seconds
2. After finding some distributions that "fit" in timeframes the module `s_form_message.py` runs in `/scheduler/`
3. Then the sending message on the API starts. `s_send.py` runs and authenticates via `auth_bearer.py` module which helps to authenticate with the given token.

## Authentication types:
- Via Web UI and admin panel at `/admin/` (instructions below)
- Via JWT token. You can get "access"&"verification" tokens at `/api/token/`. You can refresh "access" token at `/api/token/refresh/` and verify at `/api/token/verify/`

## Other features:
- Prometheous analytics (available on `/metrics/`)
- Documentation in Open API format with Swagger UI (available on `/docs/`)
- Admin panel with Web UI (available on `/admin/`)
  - Instruction for getting access to Admin Panel
    1. In project console run CMD: `python manage.py createsuperuser`
    2. Follow the instructions below
- Docker-compose file