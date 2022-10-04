
from multiprocessing import connection
import queue
from cmath import e
import pika

def connectToHost():
    try:
        parameters = pika.ConnectionParameters("localhost")
        return pika.BlockingConnection(parameters)
    except Exception as  e: print('Error:' + e)

def createExchange():
    
    connection = connectToHost()

    try:
        channel = connection.channel()
        channel.exchange_declare(exchange='e.messenger', 
                            exchange_type='direct', 
                            passive= False,
                            durable=True,
                            auto_delete=False, 
                            internal=False,
                            arguments=None)
        closeConnection(connection)
        print("The Exchange was created successfully")
    except Exception as e: print('Error:' + e)

def createQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_declare(queue='q.messenger',
                            passive= False,
                            durable= True,
                            auto_delete= False,
                            arguments=None)
        closeConnection(connection)
        print("The Sum Queue was created successfully")
    except Exception as e: print('Error' + e)

def bindingQueueToExchange():
    connection = connectToHost()
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.queue_bind(queue='q.messenger' ,
                            exchange='e.messenger',
                            routing_key='Hi')
        closeConnection(connection)
        print("The binding was successfully")
    except Exception as e: print('Error' + e)
    
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)

def deleteExchangeAndQueue():
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.exchange_delete(exchange="e.calculate", if_unused= False)
        channel.queue_delete(queue="q.sum")
        closeConnection(connection)
    except: print('Delete Exchange and Queue encountered a problem')
    