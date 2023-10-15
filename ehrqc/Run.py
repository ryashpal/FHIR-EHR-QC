from ehrqc.omop_to_fhir import Migrate as MigrateOmopToFhir
from ehrqc.config import RunConfig as RunConfig


if __name__ == "__main__":

    import logging
    import sys

    log = logging.getLogger("EHRQC")
    log.setLevel(logging.INFO)
    format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(format)
    log.addHandler(ch)

    for config in RunConfig.run_config_omop_to_fhir:
        if config['type'] == 'migrate':
            MigrateOmopToFhir.omopToFhir(
                entity=config['entity'],
                sqlFilePath=config['sqlFilePath'],
                jsonTemplatePath=config['jsonTemplatePath'],
                mapping=config['json_sql_mapping'],
                save=config['save'],
                savePath=config['savePath']
                )
        elif config['type'] == 'execute':
            config['function']()

    # for config in RunConfig.run_config_fhir_to_omop:
    #     if config['type'] == 'migrate':
    #         Migrate.fhirToOmop(
    #             entity=config['entity'],
    #             urlQueryStringPath=config['urlQueryStringPath'],
    #             sqlFilePath=config['sqlFilePath'],
    #             mapping=config['sql_json_mapping'],
    #             )
