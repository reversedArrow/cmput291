#1
select f.flight_id,f.destination
from flight f
where f.source = 'Toronto';

#2
select distinct p.name,p.nationality
from passenger p, reserve r
where p.passenger_id = r.ps_id
and r.class = 'BUS';

#3
select p.name
from passenger p, flight f, reserve r
where p.passenger_id = r.ps_id
and r.fl_id = f.flight_id
group by p.name
having count(distinct f.destination) >2;

#4
select a.airline_name
from airline a, airline_domain ad, flight f
where a.airline_name = ad.al_name
and ad.fl_id = f.flight_id
and f.destination = 'Toronto'
group by a.airline_name
limit 1;

#5
select distinct p.name
from passenger p,reserve r, flight f
where p.passenger_id = r.ps_id
and r.fl_id = f.flight_id
and f.flight_id = '1'
group by f.flight_id

union

select distinct p.name
from passenger p,reserve r, flight f
where p.passenger_id = r.ps_id
and r.fl_id = f.flight_id
and f.flight_id = '9'
group by f.flight_id;
