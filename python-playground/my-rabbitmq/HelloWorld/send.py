"""
In the first tutorial we wrote programs to send and receive messages from a named queue
"""
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()