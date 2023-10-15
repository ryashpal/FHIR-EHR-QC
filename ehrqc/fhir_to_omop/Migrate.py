import json

from tqdm import tqdm
from datetime import datetime

from ehrqc.FhirUtils import readFhirFromUrl
from ehrqc.FileUtils import readSqlFile
from ehrqc.DbUtils import updateDb

import logging

log = logging.getLogger("EHRQC")


def fhirToOmop(entity, urlQueryStringPath, sqlFilePath, mapping, save=False, savePath='./'):
    log.info('Starting FHIR to OMOP for ' + entity)
    log.info('urlQueryStringPath: ' + urlQueryStringPath)
    log.info('sqlFilePath: ' + sqlFilePath)
    log.info('mapping: ' + str(mapping))
    log.info('save: ' + str(save))
    log.info('savePath: ' + str(savePath))
    log.info('Fetching data from FHIR')
    fhirData = readFhirFromUrl(urlQueryStringPath)
    log.debug('fhirData: ' + str(fhirData))
    log.info('Reading SQL file')
    sqlQuery = readSqlFile(sqlFilePath)
    log.debug('insertQuery: ' + str(sqlQuery))
    log.info('Performing mapping')
    paramsList = mapJsonToSql(fhirData, mapping)
    for params in paramsList:
        log.debug('params: ' + str(params))
        updatedRowsCount = updateDb(sqlQuery, params)
        log.debug('updatedRowsCount: ' + str(updatedRowsCount))
    if save:
        with open(savePath + '/' + entity + '_' + datetime.today().strftime('%Y%m%d_%H%M%S') + '.json', "w") as f:
            json.dump(fhirData, f)


def mapJsonToSql(fhirData, mapping):
    paramsList = []
    if 'entry' in fhirData:
        entries = fhirData['entry']
        for entry in entries:
            params = {}
            if 'resource' in entry:
                for key in mapping.keys():
                    childResource = entry['resource']
                    valueList = mapping[key].split('||')
                    for i in range(len(valueList) - 1):
                        index = valueList[i]
                        if index.isdigit():
                            index = int(index)
                        childResource = childResource[index]
                    params[key] = childResource[valueList[len(valueList) - 1]]
            paramsList.append(params)
    return paramsList
