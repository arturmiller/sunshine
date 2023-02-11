from fastapi import FastAPI, Body, Query
from pydantic import BaseModel
from suntime import Sun, SunTimeException
import geopy.geocoders
from dateutil import parser

app = FastAPI()


class Location(BaseModel):
    latitude: float
    longitude: float
    address: str


@app.get("/location")
async def get_location():
    return {"latitude": 37.7749, "longitude": -122.4194, "address": "San Francisco, CA"}


@app.post("/location")
async def set_location(location: Location):
    geolocator = geopy.geocoders.Nominatim(user_agent="sunrise_sunset_app")
    if location.address:
        location = geolocator.geocode(location.address)
        latitude, longitude = location.latitude, location.longitude
    else:
        latitude, longitude = location.latitude, location.longitude
    return {"latitude": latitude, "longitude": longitude, "address": location.address}


@app.get("/date")
async def get_date():
    return {"date": "2023-02-11"}


@app.post("/date")
async def set_date(date: str):
    return {"date": date}


@app.get("/sunrise-sunset")
async def get_sunrise_sunset(
    latitude: float = Query(..., description="Latitude of the location"),
    longitude: float = Query(..., description="Longitude of the location"),
    date: str = Query(
        ..., description="Date to retrieve sunrise and sunset information for"
    ),
):
    try:
        date = parser.parse(date)
        sun = Sun(latitude, longitude)
        sunrise = sun.get_sunrise_time(date=date)
        sunset = sun.get_sunset_time(date=date)
        return {"sunrise": sunrise, "sunset": sunset}
    except SunTimeException as e:
        return {"error": str(e)}
