import json
from ehrqc.FhirUtils import get
from ehrqc.DbUtils import getConnection


def createLocationLookup():
    print('getting connection')
    con = getConnection()

    print('creating table')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS omop_test_20220817.location_id_map (id varchar, name varchar);")
    cur.close()

    print('fetching data')
    url = 'http://superbugai.erc.monash.edu:8082/fhir/Location?organization=T001&_count=50'
    response = get(url=url)
    responseJson = json.loads(response.text)
    entries = responseJson['entry']
    for entry in entries:
        id = entry['resource']['id']
        name = entry['resource']['name']
        cur = con.cursor()
        cur.execute('INSERT INTO omop_test_20220817.location_id_map (id, name) VALUES (%s, %s)', (id, name))
        cur.close()
    print('completed loading the data')
    con.commit()
    con.close()


run_config_omop_to_fhir = [
    # {
    #     'entity': 'Organization',
    #     'type': 'migrate',
    #     'sqlFilePath': 'ehrqc/templates/sql/select/Organization.sql',
    #     'jsonTemplatePath': 'ehrqc/templates/fhir/Organization.json',
    #     'json_sql_mapping': {
    #         'id': 'id',
    #         'name': 'organization_name',
    #     },
    #     'save': True,
    #     'savePath': 'data/omop_to_fhir/organization'
    # },
    # {
    #     'entity': 'Location',
    #     'type': 'migrate',
    #     'sqlFilePath': 'ehrqc/templates/sql/select/Transfer.sql',
    #     'jsonTemplatePath': 'ehrqc/templates/fhir/Location.json',
    #     'json_sql_mapping': {
    #         'id': 'id',
    #         'name': 'careunit',
    #     },
    #     'save': True,
    #     'savePath': 'data/omop_to_fhir/location'
    # },
    # {
    #     'type': 'execute',
    #     'function': createLocationLookup
    # },
    # {
    #     'entity': 'Patient',
    #     'type': 'migrate',
    #     'sqlFilePath': 'ehrqc/templates/sql/select/Person.sql',
    #     'jsonTemplatePath': 'ehrqc/templates/fhir/Patient.json',
    #     'json_sql_mapping': {
    #         'id': 'id',
    #         'gender': 'gender',
    #     },
    #     'save': True,
    #     'savePath': 'data/omop_to_fhir/patient',
    # },
    # {
    #     'entity': 'Encounter',
    #     'type': 'migrate',
    #     'sqlFilePath': 'ehrqc/templates/sql/select/VisitOccurrence.sql',
    #     'jsonTemplatePath': 'ehrqc/templates/fhir/Encounter.json',
    #     'json_sql_mapping': {
    #         'id': 'id',
    #         'class||code': 'code',
    #         'subject||reference': 'person_id',
    #         'participant||period||end': 'visit_end_datetime',
    #         'participant||period||start': 'visit_start_datetime',
    #         'location': {
    #             'sqlFilePath': 'ehrqc/templates/sql/select/LocationListitem.sql',
    #             'jsonTemplatePath': 'ehrqc/templates/fhir/LocationListitem.json',
    #             'json_sql_mapping': {
    #                 'location||reference': 'id',
    #                 'period||start': 'intime',
    #                 'period||end': 'outtime',
    #             }
    #         }
    #     },
    #     'save': True,
    #     'savePath': 'data/omop_to_fhir/encounter',
    # },
    # {
    #     'entity': 'Observation',
    #     'type': 'migrate',
    #     'sqlFilePath': 'ehrqc/templates/sql/select/Measurement.sql',
    #     'jsonTemplatePath': 'ehrqc/templates/fhir/Observation.json',
    #     'json_sql_mapping': {
    #         'id': 'id',
    #         'code||coding||code': 'measurement_concept_id',
    #         'code||coding||display': 'measurement_concept_name',
    #         'code||text': 'measurement_concept_name',
    #         'subject||reference': 'person_id',
    #         'encounter||reference': 'visit_occurrence_id',
    #         'effectiveDateTime': 'measurement_datetime',
    #         'valueQuantity||value': 'value_as_number',
    #         'valueQuantity||unit': 'unit_concept_id',
    #         'valueQuantity||code': 'unit_concept_code',
    #     }
    # },
]


run_config_fhir_to_omop = [
    # {
    #     'entity':'Patient',
    #     'type': 'migrate',
    #     'urlQueryStringPath':'migrate/urls/Patient.url',
    #     'sqlFilePath':'migrate/sql/insert/Person.sql',
    #     'sql_json_mapping': {
    #         'id': 'id',
    #         'gender': 'gender'
    #     }
    # },
    {
        'entity':'Observation',
        'type': 'migrate',
        'urlQueryStringPath':'migrate/urls/Observation.url',
        'sqlFilePath':'migrate/sql/insert/Measurement.sql',
        'sql_json_mapping': {
            'id': 'id',
            'value_as_number': 'valueQuantity||value',
            'measurement_concept_id': 'code||coding||0||code',
            'unit_concept_id': 'valueQuantity||unit',
            'person_id': 'subject||reference',
            'visit_occurrence_id': 'encounter||reference',
            'measurement_datetime': 'effectiveDateTime',
        }
    },
]
