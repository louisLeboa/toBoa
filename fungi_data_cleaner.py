import numpy as np
import pandas as pd

#imports the fungi_data
fungi_data = pd.read_csv("0045302-181108115102211.csv",  delimiter = "\t")

## NOTE: Drops the columns of data that are not useful to us.
fungi_clean = fungi_data.drop(['datasetKey', 'kingdom', 'taxonRank', 'infraspecificEpithet', 'species','rightsHolder','license', 'mediaType', 'issue','institutionCode', 'collectionCode','catalogNumber', 'recordNumber', 'identifiedBy', 'dateIdentified', 'typeStatus', 'establishmentMeans', 'lastInterpreted', 'basisOfRecord',  'elevationAccuracy', 'depth', 'depthAccuracy', 'coordinatePrecision', 'elevation',], axis = 1)


fungi_clean.to_csv('fungi_clean.csv',  sep = "\t", encoding='utf-8', index=False)
