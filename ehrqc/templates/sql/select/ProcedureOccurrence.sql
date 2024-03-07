select
(
    case when po.procedure_occurrence_id::text like '-%' then 'm' || substr(po.procedure_occurrence_id::text, 2) else 'p' || po.procedure_occurrence_id end
) as id,
to_char(po.procedure_datetime, 'YYYY-MM-DD') || 'T' || to_char(po.procedure_datetime, 'HH24:MI:SS') as procedure_datetime,
con.concept_code as concept_code,
con.concept_name as concept_name,
'Patient/' || (case when po.person_id::text like '-%' then 'm' || substr(po.person_id::text, 2) else 'p' || po.person_id end) as person_id,
'Encounter/' || (case when po.visit_occurrence_id::text like '-%' then 'm' || substr(po.visit_occurrence_id::text, 2) else 'p' || po.visit_occurrence_id end) as visit_occurrence_id
from
omop_test_20220817.procedure_occurrence po
inner join omop_test_20220817.concept con
on con.concept_id = po.procedure_concept_id
inner join omop_test_20220817.data_matrix dm
on dm.person_id = po.person_id
where
con.vocabulary_id = 'SNOMED'
and
(po.procedure_datetime between (dm.anchor_time::timestamp - interval '6 hour') and (dm.anchor_time::timestamp + interval '6 hour'))
;
