
from multiprocessing import connection
import queue
from cmath import e
import pika

# Create connection to rabbitmq running
def connectToHost():
    try:
        parameters = pika.ConnectionParameters("localhost") #if running in localhost in default port
        return pika.BlockingConnection(parameters)
    except Exception as  e: print('Error:' + e)

# create exchange where the sender will send the message
def createExchange():
    
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.exchange_declare(exchange='e.messenger', # name of the exchnage
                            exchange_type='direct', 
                            passive= False,
                            durable=True,
                            auto_delete=False, 
                            internal=False,
                            arguments=None)
        closeConnection(connection)
        print("The Exchange was created successfully")
    except Exception as e: print('Error:' + e)

# creating queue where the exchange will send the data for consumer to receive
def createQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_declare(queue='q.messenger', #name of the queue
                            passive= False,
                            durable= True,
                            auto_delete= False,
                            arguments=None)
        closeConnection(connection)
        print("The Sum Queue was created successfully")
    except Exception as e: print('Error' + e)

# Bind the Exchange to queue so it sends the data to required queue
def bindingQueueToExchange():
    connection = connectToHost()
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_bind(queue='q.messenger' , #name of the queue
                            exchange='e.messenger',#name of the exchange
                            routing_key='Hi')
        closeConnection(connection)
        print("The binding was successfully")
    except Exception as e: print('Error' + e)
    
# Close the DB connection
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)

# Delete the Exchange and queue if not required
def deleteExchangeAndQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.exchange_delete(exchange="e.calculate", if_unused= False)
        channel.queue_delete(queue="q.sum")
        closeConnection(connection)
    except: print('Delete Exchange and Queue encountered a problem')
    