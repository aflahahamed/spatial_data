from urllib import request
import json
import time
from importlib.machinery import SourceFileLoader
import schedule
import logging
   
# Initializing rabbitmq and postgres fucntion from other folders
rabbitmq = SourceFileLoader("config","../broker/config.py").load_module()
sender = SourceFileLoader("send","../broker/send.py").load_module()
receiver = SourceFileLoader("receive","../broker/receive.py").load_module()
postgres = SourceFileLoader("postgres","../database/postgres.py").load_module()


rabbitmq.createExchange()
rabbitmq.createQueue()
rabbitmq.bindingQueueToExchange()
# rabbitmq.deleteExchangeAndQueue

logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
log = logging.getLogger()
log.setLevel(logging.DEBUG)

while True:
    def main():
        def update_data():
            print("starting update job")
            data_url = "https://datahub.io/core/geo-countries/r/countries.geojson"
            response = request.urlopen(data_url)
            content = response.read()
            data =json.loads(content.decode("utf8"))
            with open('../geojson/mydata.json', 'w') as f:
                json.dump(data, f)
            print("Done updating data")
            
            
        print("starting main job")
        msg = "Start the file loader"
        sender.send(msg)
        received_msg = receiver.receive()
        # after specified time interval the data will be downloaded
        if (received_msg):
            update_data()
            
        # function to update the postgres database
        print("Inserting Data into postgres")
        postgres.insertDataInPostgres()
        print("Done inserting data into postgres")
    
    
    main() #Execute the function
    print("Waiting 10 minutes")
    time.sleep(600)