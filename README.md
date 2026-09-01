# User-Controlled Feed

## Problem

Most social feeds decide how content is ranked and delivered with limited user control. This project explores what a social feed could look like if users were given explicit control over how their content is ordered.

## Project

A full-stack social feed prototype that lets users choose how their feed is ranked.

Currently, users can switch between:

- **Latest** - shows all posts in reverse chronological order.
- **Following** - shows posts only from creators the user follows.

The selected feed mode is stored on the backend and persists across page reloads.

## Current Features

- PostgreSQL-backed users, posts, follow relationships, and feed preferences
- Latest and Following feed modes
- Persistent user feed preference
- FastAPI REST endpoints for retrieving feeds and updating preferences
- Pydantic request and response validation
- Responsive React interface
- Automated API and integration tests for feed ordering, filtering, validation, and preference persistence

## Tech Stack

- React
- TypeScript
- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest

## Testing

The backend currently includes automated tests covering:

- Chronological feed ordering
- Following-feed filtering
- Feed preference retrieval and updates
- Preference persistence
- Invalid feed modes and preference values

Run the test suite from the `backend` directory:

```bash
python3 -m pytest -v
```

## Planned

- User-directed ranking based on explicit user preferences
- Finite feed sessions with intentional stopping points
- Feed event instrumentation
- End-to-end testing
- Transparent explanations for why posts appear in the feed