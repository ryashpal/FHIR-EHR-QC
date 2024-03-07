select
(case when mmt.measurement_id::text like '-%' then 'm' || substr(mmt.measurement_id::text, 2) else 'p' || mmt.measurement_id end) as id,
mmt_con.concept_id as measurement_concept_id,
mmt_con.concept_name as measurement_concept_name,
'Patient/' || (case when mmt.person_id::text like '-%' then 'm' || substr(mmt.person_id::text, 2) else 'p' || mmt.person_id end) as person_id,
'Encounter/' || (case when mmt.visit_occurrence_id::text like '-%' then 'm' || substr(mmt.visit_occurrence_id::text, 2) else 'p' || mmt.visit_occurrence_id end) as visit_occurrence_id,
to_char(mmt.measurement_datetime, 'YYYY-MM-DD') || 'T' || to_char(mmt.measurement_datetime, 'HH24:MI:SS') as measurement_datetime,
uni_con.concept_id as unit_concept_id,
uni_con.concept_code as unit_concept_code,
mmt.value_as_number as value_as_number
from
omop_test_20220817.measurement mmt
inner join omop_test_20220817.data_matrix dm
on dm.person_id = mmt.person_id
inner join omop_test_20220817.concept mmt_con
on mmt_con.concept_id = mmt.measurement_concept_id
inner join omop_test_20220817.concept uni_con
on uni_con.concept_id = mmt.unit_concept_id
where
mmt.measurement_source_value IN
    (
    '220045' -- heartrate
    , '220050', '220179' -- sysbp
    , '220051', '220180' -- diasbp
    , '220052', '220181', '225312' -- meanbp
    , '220739' -- gcseye
    , '223900' -- gcsverbal
    , '223901' -- gscmotor
    )
and 
(mmt.measurement_datetime between (dm.anchor_time::timestamp - interval '6 hour') and (dm.anchor_time::timestamp + interval '6 hour'))
and value_as_number <> 'NaN'
and value_as_number is not null
;
