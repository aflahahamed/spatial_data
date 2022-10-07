# spatial_data
This is a cron job implementation of postgres data updater and REST API for spatial data.

## Approach
The code is written using the following packages:
- Python             3.9.6
- uvicorn            0.18.3
- fastapi            0.85.0
- GeoAlchemy2        0.12.5
- uvicorn            0.18.3
- pika               1.3.0
- psycopg2           2.9.3
- requests           2.28.1
- SQLAlchemy         1.4.41
- Docker compose
## Cron Job
* To run the cron job, the details are as following:
  go to the database folder and broker folder and run the docker-compose.yml files by running the command
```
    docker-compose up
```
* Create the table in postgres using the following command:
```
CREATE EXTENSION hstore;
CREATE EXTENSION postgis;

CREATE TABLE features (
    country character(50) PRIMARY KEY NOT NULL,
    iso_code character(50),
    geom geometry(geometry, 4326)
);
```
  This will setup the posgres and rabbitmq container in local environment
  Go to the app folder and run the main file using the following command:
```
    python .\main.py
```
  This will start the cronjob which will download the data and update it into postgres db and craete a copy in geojson folder
  
## API
  Go to the api folder and run the following command:
```
  python -m uvicorn main:app --reload
```
  This will run the api in `localhost:8000`
  To test the API Open postman application
  * Read
  Put the following link
  `http://localhost:8000/country/read`
  Attach a JSON body to and send the `GET` request to create the data in the db like
  ```
  {
    "parameter":{
        "country":"Oman"
    }
  }
  ```
  * Delete
    Put the following link
  `http://localhost:8000/country/delete`
  Attach a JSON body to and send the `DELETE` request to create the data in the db like
  ```
  {
    "parameter":{
        "country":"Aruba"
    }
}
  ```
  * Update
  Put the following link
  ` http://localhost:8000/country/update`
  Attach a JSON body to and send the `PATCH` request to create the data in the db like
  ```
  {
    "parameter":{
        "country":"Oman",
        "iso_code":"IND",
        "Geometry":"[[-69.99693762899992, 12.577582098000036], [-69.93639075399994, 12.53172435100005], [-69.92467200399994, 12.519232489000046], [-69.91576087099992, 12.497015692000076], [-69.88019771999984, 12.453558661000045], [-69.87682044199994, 12.427394924000097], [-69.88809160099993, 12.417669989000046], [-69.90880286399994, 12.417792059000107], [-69.93053137899989, 12.425970770000035], [-69.94513912699992, 12.44037506700009], [-69.92467200399994, 12.44037506700009], [-69.92467200399994, 12.447211005000014], [-69.95856686099992, 12.463202216000099], [-70.02765865799992, 12.522935289000088], [-70.04808508999989, 12.53115469000008], [-70.05809485599988, 12.537176825000088], [-70.06240800699987, 12.546820380000057], [-70.06037350199995, 12.556952216000113], [-70.0510961579999, 12.574042059000064], [-70.04873613199993, 12.583726304000024], [-70.05264238199993, 12.600002346000053], [-70.05964107999992, 12.614243882000054], [-70.06110592399997, 12.625392971000068], [-70.04873613199993, 12.632147528000104], [-70.00715084499987, 12.5855166690001], [-69.99693762899992, 12.577582098000036]]"
    }
}
  ```
  * Create
  Put the following link
  `http://localhost:8000/country/create`
  Attach a JSON body to and send the `POST` request to create the data in the db like
  ```
  {
    "parameter" :{
        "country":"testin",
        "iso_code":"test",
        "Geometry":"[[-69.99693762899992, 12.577582098000036], [-69.93639075399994, 12.53172435100005], [-69.92467200399994, 12.519232489000046], [-69.91576087099992, 12.497015692000076], [-69.88019771999984, 12.453558661000045], [-69.87682044199994, 12.427394924000097], [-69.88809160099993, 12.417669989000046], [-69.90880286399994, 12.417792059000107], [-69.93053137899989, 12.425970770000035], [-69.94513912699992, 12.44037506700009], [-69.92467200399994, 12.44037506700009], [-69.92467200399994, 12.447211005000014], [-69.95856686099992, 12.463202216000099], [-70.02765865799992, 12.522935289000088], [-70.04808508999989, 12.53115469000008], [-70.05809485599988, 12.537176825000088], [-70.06240800699987, 12.546820380000057], [-70.06037350199995, 12.556952216000113], [-70.0510961579999, 12.574042059000064], [-70.04873613199993, 12.583726304000024], [-70.05264238199993, 12.600002346000053], [-70.05964107999992, 12.614243882000054], [-70.06110592399997, 12.625392971000068], [-70.04873613199993, 12.632147528000104], [-70.00715084499987, 12.5855166690001], [-69.99693762899992, 12.577582098000036]]"
              }
  }
```
  * Match
  Put the following link
  `http://localhost:8000/country/match`
  Attach a JSON body to and send the `GET` request to create the data in the db like
  ```
  {
    "parameter":{
        "country":"United"
    }
}
  ```
