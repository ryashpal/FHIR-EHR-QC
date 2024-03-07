with stg1 as(
	select
	(case when per.person_id::text like '-%' then 'm' || substr(per.person_id::text, 2) else 'p' || per.person_id end) as id,
	'FN_' || (case when per.person_id::text like '-%' then 'm' || substr(per.person_id::text, 2) else 'p' || per.person_id end) as first_name,
	'LN_' || (case when per.person_id::text like '-%' then 'm' || substr(per.person_id::text, 2) else 'p' || per.person_id end) as last_name,
	lower(con.concept_name) as gender
	from
	omop_test_20220817.person per
	inner join omop_test_20220817.concept con
	on con.concept_id = per.gender_concept_id
	inner join omop_test_20220817.data_matrix dm
	on dm.person_id = per.person_id
)
select
distinct id as id,
first_value(first_name) over () as first_name,
first_value(last_name) over () as last_name,
first_value(gender) over () as gender
from stg1
;
