import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="flight"
    )
from pydantic import BaseModel
from datetime import date

class FlightSearch(BaseModel):
    Origin: str
    Destination: str
    Flight_date: date | None = None
    sort_by: str | None = None   
    from fastapi import FastAPI
from db import get_connection
from models import FlightSearch

app = FastAPI()


@app.get("/flights")
def get_all_flights():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute("SELECT * FROM flights_booking")
    flights = cur.fetchall()

    conn.close()
    return {"flights": flights}


@app.post("/search")
def search_flights(data: FlightSearch):
    
    query = """
        SELECT Flight_Id, Airlines, Price, Flight_date, Origin, Destination,
               Arrival_time, Departure_time, Seats, Seats_left, Airport
        FROM flights_booking
        WHERE Origin = %s AND Destination = %s
    """

    params = [data.origin, data.destination]

    if data.flight_date:
        query += " AND DATE(Flight_date) = %s"
        params.append(data.flight_date)

    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute(query, tuple(params))
    results = cur.fetchall()

    if data.sort_by == "price":
        results.sort(key=lambda x: x["Price"])
    elif data.sort_by == "duration":
        results.sort(key=lambda x: (
            x["Arrival_time"] - x["Departure_time"]
        ))

    conn.close()
    return {"results": results}

@app.get("/external-feed")
def simulated_airline_api():
    return {
        "external_flights": [
            {"flight": "EX101", "airline": "Air India", "price": 5500},
            {"flight": "EX202", "airline": "IndiGo", "price": 4800},
            {"flight": "EX303", "airline": "SpiceJet", "price": 6200},
        ]
    }

@app.get("/")
def home():
    return {"message": "Flight API Running Successfully!"}