-- 1.	In the "class" table, add a new record called "Regular". Replace all occurrences of class types "Silver" and "Gold" in the "pax" table with the class you added.

insert into class(ClassName)
values ('Regular');

update pax 
inner join class 
on pax.ClassID = class.ClassID
set pax.ClassID = (select ClassID from class where ClassName = 'Regular')
where class.ClassName IN ('Silver', 'Gold');


-- 2.	In the "aircraft" table, update all aircraft types containing "Boeing" and aircraft names containing the letters "M" or "W" with an aircraft that contains "330" in its name.

update aircraft 
inner join aircrafttype on aircraft.AircraftTypeID = aircrafttype.AircraftTypeID
set aircraft.AircraftTypeID = (select AircraftTypeID from aircrafttype where aircrafttype.AircraftName like '%330%') 
where (aircrafttype.AircraftName like '%Boeing%' OR aircrafttype.AircraftName like '%M%' OR aircrafttype.AircraftName like '%W%');

-- 3.	Write a query that displays the route IDs and distances (between airports) of all routes with above-average distance, sorted in descending order by distance.

select RouteID, Distance
from route
where Distance > (select avg(Distance) from route)
order by Distance desc;

-- 4.	Write a query to create a list of flight IDs from and to the "Heathrow" airport, sorted in descending order. 

select FlightID from flight
where RouteID in (select RouteID from route where ToAirport = (select AirportID from airport where AirportName = 'Heathrow Airport')
or FromAirport = (select AirportID from airport where AirportName = 'Heathrow Airport'))
order by FlightID desc;

-- 5.	Write a query that displays a list of all routes with above-average distance.
select RouteID, Distance
from route
where Distance > (select avg(Distance) from route)
order by Distance desc;

-- 6.	Write a query that displays a list of all flights operated by airplanes with the designation "SW" in their name.

select a_type.AircraftName, flight.FlightID
from aircraft
join aircrafttype as a_type on aircraft.AircraftTypeID = a_type.AircraftTypeID
and a_type.AircraftName like "%SW%"
join flight on aircraft.AircraftID = flight.AircraftID