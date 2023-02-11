# Sunshine

A webapp that shows the user when the sunrise and sunset is for the location of the user. The user can set the latitude and longitude with an interactive geographic map or by setting the address. The user can also select a certain date, but the default is the current day.

## Features
- Show sunrise and sunset times for a given location
- Ability to set the latitude and longitude with an interactive geographic map or by setting the address
- Option to select a date, with the current day as default

## Requirements
- Python 3.7+
- FastAPI
- Uvicorn
- Python-dateutil
- Astral

## Usage
```Bash
poetry run uvicorn app.main:app --reload
```

## Testing
```Bash
poetry run python -m pytest
```

## Linting and formatting
```Bash
poetry run black .
poetry run ruff .
```