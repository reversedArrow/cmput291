.print Question 1 -xianhang
SELECT distinct sa.local_contact
FROM service_agreements sa, account_managers am, accounts ac, personnel p
WHERE sa.master_account = ac.account_no
	AND ac.account_mgr = p.pid
	AND sa.waste_type = "hazardous waste"
	AND p.name = "Dan Brown";

.print Question 2 -xianhang
SELECT distinct ac.customer_name, ac.contact_info, p.name
FROM accounts ac, account_managers am, personnel p, service_agreements sa
WHERE sa.master_account = ac.account_no
	AND ac.customer_type = "industrial"
	AND ac.account_mgr = am.pid
	and am.pid = p.pid
	and 30 > (SELECT julianday('now') - julianday(ac.end_date)
                FROM accounts ac1
				where ac1.account_no = ac.account_no);

.print Question 3 -xianhang
SELECT distinct ac.customer_name
FROM accounts ac, service_agreements sa
WHERE ac.account_no = sa.master_account
	AND sa.waste_type = "mixed waste"

INTERSECT

SELECT distinct ac.customer_name
FROM accounts ac
WHERE julianday('now') > julianday(ac.start_date) AND julianday('now') < julianday(ac.end_date)

EXCEPT

SELECT distinct ac.customer_name
from accounts ac, service_agreements sa
WHERE ac.account_no = sa.master_account
	AND sa.waste_type = "paper";

.print Question 4 -xianhang
SELECT am.manager_title as "Account Type", COUNT(*) as "Number of Services", SUM(sa.price)- SUM(sa.internal_cost) as "Profit" 
FROM account_managers am, accounts ac, service_agreements sa
WHERE am.pid = ac.account_mgr
	AND sa.master_account = ac.account_no
GROUP BY am.manager_title;

.print Question 5 -xianhang
SELECT p.name
FROM personnel p, drivers d, service_fulfillments sf
WHERE p.pid = d.pid
	AND d.pid = sf.driver_id
GROUP BY d.pid
HAVING COUNT(*) > 10;

.print Question 6 -xianhang
SELECT distinct c.container_id
FROM containers c, service_fulfillments sf
WHERE c.container_id = sf.cid_drop_off
	AND (julianday('now') - julianday(c.date_when_built)) > 365*5
GROUP BY c.container_id
HAVING 10 < COUNT(*);

.print Question 7 -xianhang
SELECT distinct c.container_id
FROM containers c
WHERE (SELECT MAX(julianday(sf.date_time)) FROM service_fulfillments sf WHERE sf.cid_drop_off = c.container_id)<(SELECT  MAX(julianday(sf.date_time)) FROM service_fulfillments sf WHERE sf.cid_pick_up = c.container_id)
UNION
select distinct c.container_id
FROM containers c
WHERE NOT exists (SELECT distinct sf.cid_drop_off FROM service_fulfillments sf WHERE sf.cid_drop_off = c.container_id);

.print Question 8 -xianhang
SELECT distinct d.pid
FROM drivers d, service_fulfillments sf
WHERE NOT EXISTS (select master_account from service_fulfillments sf1 where sf1.driver_id = d.pid except 
					select master_account from service_fulfillments sf1 where sf1.driver_id = 23769)
	  AND NOT EXISTS(select master_account from service_fulfillments sf1 where sf1.driver_id = 23769 except 
					select master_account from service_fulfillments sf1 where sf1.driver_id = d.pid)
	  AND d.pid <> 23769;

.print Question 9 -xianhang
CREATE VIEW last2_inspections_of_company_trucks(truck_id, truck_type, inspection_date) AS
SELECT * FROM(
	SELECT t.truck_id as id, t.model as "Truck Type", MAX(mr.service_date) as "Inspection Date"
	FROM trucks t, maintenance_records mr
	WHERE t.truck_id = mr.truck_id
		AND mr.description = "Inspection"
		AND NOT EXISTS (SELECT * FROM drivers d WHERE d.owned_truck_id = t.truck_id)
	GROUP BY t.truck_id
	UNION ALL
	SELECT t.truck_id as id, t.model as "Truck Type", MAX(mr.service_date) as inspection_date
	FROM trucks t, maintenance_records mr
	WHERE t.truck_id = mr.truck_id
		AND mr.description = "Inspection"
		AND NOT EXISTS (SELECT * FROM drivers d WHERE d.owned_truck_id = t.truck_id)
		AND mr.service_date < (SELECT MAX(mr1.service_date) FROM maintenance_records mr1 WHERE mr1.truck_id = t.truck_id)
	GROUP BY t.truck_id
)ORDER BY id;


.print Question 10 -xianhang
WITH t1(id, type, time_diff) AS (
	SELECT truck_id, truck_type, MAX(julianday(inspection_date)) - MIN(julianday(inspection_date))
	FROM last2_inspections_of_company_trucks
	GROUP BY truck_id
)
SELECT type as "Truck Type", MIN(time_diff) as "Minimum", MAX(time_diff) as "Maximum", avg(time_diff) as "Average"
FROM t1
GROUP BY type;
