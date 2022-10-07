from cmath import e
import pika

# Connect to host
def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        return pika.BlockingConnection(parameters)
    except e: print('Connect to localhost encountered a problem')

# Close connection if not required
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)
        
# Receive the message from queue
def receive():
    connection = connectToHost()
    channel = connection.channel()
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
