from cmath import e
import pika

def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        return pika.BlockingConnection(parameters)
    except e: print('Connect to localhost encountered a problem')

def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)
    
def send(body):
    connection = connectToHost()
    try:
        channel = connection.channel()
        channel.basic_publish(exchange='e.messenger',
                                        routing_key= 'Hi',
                                        body="App2: " + body)
        closeConnection(connection)
        
    except Exception as e : print('Error:' + e)
        
def receive():
    connection = connectToHost()
    channel = connection.channel()
    print("inside receiver")
    channel.queue_declare(queue='q.messenger',
                            passive= False,
                            durable= True,
                            auto_delete= False,
                            arguments=None)

    def callback(ch, method, properties, body):
        return (body)

    msg = channel.basic_consume(queue='q.messenger', on_message_callback=callback, auto_ack=True)
    return msg
    
    channel.start_consuming()
