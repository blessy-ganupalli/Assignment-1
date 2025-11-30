create database flight;
use flight;
Table-1
create table flights_booking(
    Flight_Id varchar(10),
    Airlines varchar(30),
    Price Decimal (10,2),
    Flight_date DateTime,
    Origin varchar(30),
    Destination varchar (30),
    Arrival_time Datetime,
    Departure_time Datetime,
    Seats INT,
    Seats_left INT,
    Airport varchar(50)
);

Insert into flights_booking(
    Flight_Id,
    Airlines, 
    Price,
    Flight_date, 
    Origin,
    Destination, 
    Arrival_time, 
    Departure_time, 
    Seats,
    Seats_left,
    Airport
)

Values (
    'A1',
    'Indigo',
     2500,
    '2025-12-17',
    'Mumbai',
    'Delhi',
    '2025-12-17 10:00:00',
    '2025-12-17 12:00:00',
    180,
    96,
    'Mumbai International Airport'
);

Insert into flights_booking Values (
    'A2',
    'Indigo',
     3000,
    '2025-12-20',
    'Delhi',
    'Mumbai',
    '2025-12-20 01:00:00',
    '2025-12-20 02:00:00',
    180,
    120,
    'Indira Gandhi International Airport'
);

Insert into flights_booking values (
    'A3',
    'Air Lines',
     5000,
    '2025-12-24',
    'Mumbai',
    'Hyderabad',
    '2025-12-24 08:00:00',
    '2025-12-24 09:30:00',
    200,
    179,
    'Mumbai International Airport'
);

Show tables;

Alter
Alter table flights_booking
add primary key (Flight_Id);

Delete
Delete from flights_booking
where Flight_Id = 'A3';
Limit 1;

Delete from bookings
where Flight_Id = 'A2';

Select
Select * from Flights_booking;

Table-2
Create table bookings (
Booking_Id Varchar(10) Primary key,
Flight_Id Varchar(10),
Passanger_name Varchar(50),
Seats_booked INT,
Booking_date Date,
Price_paid decimal(10,2),
Foreign key (Flight_Id) references flights_booking(Flight_Id)
);


insert into bookings (Booking_Id,
Flight_Id,
Passanger_name,
Seats_booked,
Booking_date,
Price_paid)
Select
'B1',
'A1',
'John',
'2',
'2025-12-17',
2 * Price 
From flights_booking
where Flight_Id = 'A1';

insert into bookings (Booking_Id,
Flight_Id,
Passanger_name,
Seats_booked,
Booking_date,
Price_paid)
Select
'B2',
'A2',
'Ram',
'1',
'2025-12-20',
1 * Price 
From flights_booking
where Flight_Id = 'A2';

select * from bookings;

insert into bookings (Booking_Id,
Flight_Id,
Passanger_name,
Seats_booked,
Booking_date,
Price_paid)
Select
'B3',
'A3',
'Kavya',
'4',
'2025-12-24',
4 * Price 
From flights_booking
where Flight_Id = 'A3';


SELECT WITH CONDITIONS
SELECT * FROM flights_booking where destination = 'Delhi';
SELECT * FROM bookings WHERE Passanger_name = 'John';

ORDER BY
SELECT * FROM flights_booking ORDER BY Price ASC;
SELECT * FROM bookings ORDER BY Booking_date DESC;

UPDATE 
UPDATE flights_booking
SET Price = 6500
WHERE Flight_Id = 'A1';

UPDATE bookings
SET Seats_booked = 20
WHERE Booking_Id = 'B1';

DELETE 
DELETE FROM bookings
WHERE Booking_Id = 'B3';

INNER JOIN
SELECT 
    b.Booking_Id,
    b.Passanger_name,
    b.Seats_booked,
    f.Flight_Id,
    f.Origin,
    f.Destination,
    f.Price
FROM bookings b
INNER JOIN flights_booking f 
    ON b.Flight_Id = f.Flight_Id;


LEFT JOIN
SELECT 
    b.Booking_Id,
    b.Passanger_name,
    b.Seats_booked,
    b.Flight_Id,
    f.Origin,
    f.destination,
    f.price
FROM bookings b
LEFT JOIN flights_booking f 
    ON b.Flight_Id = f.Flight_Id;



RIGHT JOIN
SELECT 
    f.Flight_Id,
    f.Origin,
    f.Destination,
    f.Price,
    b.Booking_Id,
    b.Passanger_name,
    b.Seats_booked
FROM flights_booking f
RIGHT JOIN bookings b 
    ON f.Flight_Id = b.Flight_Id;


FULL OUTER JOIN 
SELECT 
    b.Booking_Id,
    b.Passanger_name,
    b.Seats_booked,
    f.Flight_Id,
    f.Origin,
    f.Destination,
    f.Price
FROM bookings b
LEFT JOIN flights_booking f 
    ON b.Flight_Id = f.Flight_Id


Join by Origin and Destination
SELECT fb.Flight_Id, fb.Origin, fb.Destination, b.Booking_Id
FROM flights_booking fb
LEFT JOIN bookings b
    ON fb.Origin = 'Delhi' AND fb.Destination = 'Mumbai';


Join by Airlines
SELECT 
    fb.Flight_Id,
    fb.Airlines,
    SUM(b.Seats_booked) AS Total_Seats_Booked
FROM flights_booking fb
LEFT JOIN bookings b
    ON fb.Flight_Id = b.Flight_Id
GROUP BY fb.Flight_Id, fb.Airlines;