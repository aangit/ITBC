# Taxi Association Database

This repository contains the design and documentation for the Taxi Association Database. The database is designed to store information about taxi drivers, vehicles, regular customers, and ride records for efficient management and operation of the taxi association.

## Database Schema

The database schema consists of the following tables:

## Drivers
Stores information about taxi drivers, including their name, middle initial, last name, ID number (JMBG), address, phone number, educational qualifications, driver's license number, and category.

## Vehicles
Keeps track of the taxi association's vehicles, including the license plate number, registration dates, make, type, year of production, engine number, chassis number, gas installation status, and mileage.

## Vehicle Assignments
Records the history of vehicle assignments, indicating which driver operated which vehicle during a specific period.

## Customers
Maintains records of the taxi association's regular customers, including a unique identification number, address, and registered phone numbers for ride ordering.

## Rides
Stores information about completed rides, including a unique identification number, start and end time of the ride, start and end address, distance traveled, the phone number and time of the call received, the driver who performed the ride, and information about the regular customer if applicable.
