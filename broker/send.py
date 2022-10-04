import pika

# Connect to host
def connectToHost():
    try:
        parameters = pika.ConnectionParameters(host="localhost")
        return pika.BlockingConnection(parameters)
    except Exception as  e: print('Error:' + e)
    
# Close connection to host 
def closeConnection(connection):
    try:
        connection.close()
    except Exception as e: print('Error:' + e)

# Send the body to exchange
def send(body):
    print("inside sender")
    connection = connectToHost()
    try:
        channel = connection.channel()
        result = channel.basic_publish(exchange='e.messenger',
                                        routing_key= 'Hi',
                                        body="App1: " + body)
        closeConnection(connection)
        
    except Exception as e : print('Error:' + e)