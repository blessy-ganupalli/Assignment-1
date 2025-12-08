
def calculate_dynamic_price(
    base_fare,
    remaining_seats_percentage,
    time_to_departure_hours,
    demand_level
):
    price = base_fare

    if remaining_seats_percentage < 20:
        price += price * 0.30      # +30%
    elif remaining_seats_percentage < 50:
        price += price * 0.15      # +15%

    if time_to_departure_hours < 24:
        price += price * 0.40      # +40%
    elif time_to_departure_hours < 72:
        price += price * 0.20      # +20%

    demand_level = demand_level.lower()
    if demand_level == "high":
        price += price * 0.25
    elif demand_level == "medium":
        price += price * 0.10

    return round(price, 2)

# main.py

from fastapi import FastAPI
from pricing_engine import calculate_dynamic_price

app = FastAPI(title="Dynamic Pricing Engine API")

@app.get("/")
def home():
    return {"message": "Dynamic Pricing Engine API is working!"}


@app.get("/calculate_price")
def calculate_price(
    base_fare: float,
    remaining_seats_percentage: float,
    time_to_departure_hours: float,
    demand_level: str
):
    final_price = calculate_dynamic_price(
        base_fare,
        remaining_seats_percentage,
        time_to_departure_hours,
        demand_level
    )

    return {
        "base_fare": base_fare,
        "remaining_seats_percentage": remaining_seats_percentage,
        "time_to_departure_hours": time_to_departure_hours,
        "demand_level": demand_level,
        "final_price": final_price
    }
