-- 1.	Write a query that displays the airport name, terminal count, and total number of routes for airports with more than two terminals. 
-- Sort the results in descending order by the number of routes and ascending order by the number of terminals.

select airport.AirportName, airport.NumTerminals, count(route.RouteID) as number_of_routes
from airport
join route on airport.AirportID = route.FromAirport or airport.AirportID = route.ToAirport
where airport.NumTerminals > 2
group by airport.AirportName
order by number_of_routes desc, airport.NumTerminals asc;

-- 2.	Write a query that displays the number of flights flying on the longest route.

select count(*) as number_of_flights
from flight
join route on flight.RouteID = route.RouteID
where route.Distance = (select max(Distance) from route);

-- 3.	Find the names of all aircraft types, as well as the total number of those aircraft, used by the airline using a LEFT JOIN. Sort the results in descending order by the number of aircraft.

select REGEXP_SUBSTR(aircrafttype.AircraftName, '^[^ ]+') as airplane_type, count(aircraft.AircraftTypeID) as number_airplane_types
from aircrafttype
left join aircraft on aircrafttype.AircraftTypeID = aircraft.AircraftTypeID
group by airplane_type
order by number_airplane_types desc;

-- 4.	Find the names of all aircraft types, as well as the total number of those aircraft, used by the airline using a RIGHT JOIN. Sort the results in descending order by the number of aircraft.

select REGEXP_SUBSTR(aircrafttype.AircraftName, '^[^ ]+') as airplane_type, count(aircraft.AircraftTypeID) as number_airplane_types
from aircrafttype
right join aircraft on aircrafttype.AircraftTypeID = aircraft.AircraftTypeID
group by airplane_type
order by number_airplane_types desc;

-- 5.	Write a query that displays the day of the week and the number of flights on that day, given that the number of flights is greater than the average.

select flightdep.DepDay as dayy, count(flightdep.FlightID) as flights
from flightdep
group by dayy
having count(flightdep.FlightID) > (select avg(flights) from (select count(flightdep.FlightID) as flights from flightdep group by flightdep.DepDay) as counts)
order by flights desc;

-- 6.	Write queries to create lists of flight IDs from and to the "Heathrow" airport, sorted in descending order.

select FlightID from flight
where RouteID in (select RouteID from route where ToAirport = (select AirportID from airport where AirportName = 'Heathrow Airport')
or FromAirport = (select AirportID from airport where AirportName = 'Heathrow Airport'))
order by FlightID desc;