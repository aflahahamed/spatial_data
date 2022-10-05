## spatial_data
This is a cron job implementation of postgres data updater and REST API for spatial data.

# Approach
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
* Go to the app folder and run the main file using the following command:
```
    python .\main.py
```
  This will start the cronjob which will download the data and update it into postgres db
* Go to the api folder and run the following command:
```
  python -m uvicorn main:app --reload
```
  This will run the api in `localhost:8000`
  To test the API Open postman application
  Put the following link
  `http://localhost:8000/country/create`
  Attach a JSON body to and send the POST request to create the data in the db like
  ```
  {
    "parameter" :{
        "country":"testin",
        "iso_code":"test",
        "Geometry": "0103000020E6100000010000001A000000362D7CD3CD7F51C098543BD7B8272940382D7CD3ED7B51C06810942C3E102940382D7CD32D7B51C0408D3ED7D8092940ACF97BD39B7A51C0707A3DD778FE2840705AD128557851C020A03FD738E82840A8B67CD31D7851C0181DEA81D3DA28406889277ED67851C0408D3ED7D8D5284004D97CD3297A51C030DE3BD7E8D52840342D7CD38D7B51C078673CD718DA28409E28D2287D7C51C0787A3DD778E12840382D7CD32D7B51C0787A3DD778E12840382D7CD32D7B51C0D0C541D7F8E428408AC1D128597D51C0704F42D728ED2840E6E3D128C58151C0005C982CBE0B2940623E7CD3138351C0B055ED81F30F294076A57CD3B78351C0C8163FD708132940AC44277EFE8351C0E8C541D7F8172940A028D228DD8351C0784F42D7281D2940E4E3D128458351C018DE3BD7E8252940B044277E1E8351C078FD922CDE2A2940B044277E5E8351C0E02FEB81333329404206D228D18351C0A8EA912C7E3A2940FE4AD228E98351C0E82FEB8133402940B044277E1E8351C0F0033ED7A8432940725AD128758051C0903C41D7C82B2940362D7CD3CD7F51C098543BD7B8272940"
    }
}
```
The rest of the end points are not working for now due to schema error for the geometry field datatype.
The code for them is implemented in the code base attached


