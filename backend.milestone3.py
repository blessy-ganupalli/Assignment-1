from fastapi import FastAPI, HTTPException
import random, string
from database import get_db

app = FastAPI()

# Generate PNR
def generate_pnr():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Simulated payment
def payment_gateway():
    return random.choice([True, True, True, False])  # mostly success

# BOOK FLIGHT
@app.post("/book")
def book_flight(flight_id: str, passenger_name: str, seats: int, price_per_seat: int):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    try:
        db.start_transaction()

        total_price = seats * price_per_seat
        payment_status = payment_gateway()

        if not payment_status:
            raise HTTPException(status_code=400, detail="Payment Failed")

        pnr = generate_pnr()

        cursor.execute("""
            INSERT INTO bookings (pnr, flight_id, passenger_name, seats, total_price, status)
            VALUES (%s, %s, %s, %s, %s, 'CONFIRMED')
        """, (pnr, flight_id, passenger_name, seats, total_price))

        db.commit()

        return {
            "message": "Booking Successful",
            "PNR": pnr,
            "amount": total_price
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        db.close()

# CANCEL BOOKING
@app.delete("/cancel/{pnr}")
def cancel_booking(pnr: str):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(
        "UPDATE bookings SET status='CANCELLED' WHERE pnr=%s",
        (pnr,)
    )

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="PNR not found")

    db.commit()
    cursor.close()
    db.close()

    return {"message": "Booking Cancelled"}

# BOOKING HISTORY
@app.get("/bookings")
def get_bookings():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM bookings")
    data = cursor.fetchall()

    cursor.close()
    db.close()
    return data