from fastapi import FastAPI

from buienradar import Buienradar

app = FastAPI()


@app.get("/forecast")
async def get_forecast(
    lattitude: str = "52.334288", longitude: str = "5.525928"
) -> dict:
    buienradar = Buienradar(longitude=longitude, lattitude=lattitude)
    return {"data": buienradar.get_precipitation_text()}


@app.get("/next_rain")
async def get_next_rain(
    lattitude: str = "52.334288", longitude: str = "5.525928"
) -> dict:
    buienradar = Buienradar(longitude=longitude, lattitude=lattitude)
    return {"data": buienradar.get_next_rain_moment()}
