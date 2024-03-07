select
(
    case when co.condition_occurrence_id::text like '-%' then 'm' || substr(co.condition_occurrence_id::text, 2) else 'p' || co.condition_occurrence_id end
) as id,
'Patient/' || (case when co.person_id::text like '-%' then 'm' || substr(co.person_id::text, 2) else 'p' || co.person_id end) as person_id,
'Encounter/' || (case when co.visit_occurrence_id::text like '-%' then 'm' || substr(co.visit_occurrence_id::text, 2) else 'p' || co.visit_occurrence_id end) as visit_occurrence_id,
to_char(co.condition_start_datetime, 'YYYY-MM-DD') || 'T' || to_char(co.condition_start_datetime, 'HH24:MI:SS') as condition_start_datetime,
con.concept_id as concept_id,
con.concept_name as concept_name
from
omop_test_20220817.condition_occurrence co
inner join omop_test_20220817.data_matrix dm
on dm.person_id = co.person_id
inner join omop_test_20220817.concept con
on con.concept_id = co.condition_concept_id
inner join omop_test_20220817.concept con_src
on con_src.concept_id = co.condition_source_concept_id
where
(
	(con_src.vocabulary_id = 'ICD10CM' and ((con_src.concept_code like 'A%') or (con_src.concept_code like 'B%')))
	or
	(con_src.vocabulary_id = 'ICD9CM' and split_part(con_src.concept_code, '.', 2) != '' and (split_part(con_src.concept_code, '.', 2))::int < 140)
)
and
(co.condition_start_datetime between (dm.anchor_time::timestamp - interval '1 month') and (dm.anchor_time::timestamp + interval '1 month'))
;
