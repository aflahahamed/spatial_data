import psycopg2
import psycopg2.extras
import json
import logging

'''
CREATE EXTENSION hstore;
CREATE EXTENSION postgis;

CREATE TABLE features (
    country character(50) PRIMARY KEY NOT NULL,
    iso_code character(50),
    geom geometry(geometry, 4326)
);
'''

INSERT_STATEMENT = 'INSERT INTO features (country,ISO_code,geom) VALUES (%s,%s, ST_SetSRID(ST_GeomFromGeoJSON(%s), 4326));'

def import_feature(cur,feature_data):
    if feature_data.get('type') == 'FeatureCollection':
        for feature in feature_data['features']:
            import_feature(cur, feature)
    elif feature_data.get('type') == 'Feature':
        geojson = json.dumps(feature_data['geometry'])
        for k, v in feature_data['properties'].items():
            if str(k)=="ADMIN":
                country = str(v)
            if str(k)=="ISO_A3":
                ISO_code = str(v)
        cur.execute(INSERT_STATEMENT, (country,ISO_code,geojson))


def insertDataInPostgres():
    logging.basicConfig(level=logging.DEBUG)
    con = psycopg2.connect(dbname="testing", user="testing", password="testing")
    # use hstore to log data
    psycopg2.extras.register_hstore(con)
    # truncate features table
    with con:
        with con.cursor() as cur:
            cur.execute('truncate features;')

    with open('../geojson/mydata.json','r') as f:
        handle = json.loads(f.read())
    # with handle:
    # feature_data = json.load(handle)
    # print(handle['features'])
    with con:
        with con.cursor() as cur:
            import_feature(cur, handle)
        con.commit()