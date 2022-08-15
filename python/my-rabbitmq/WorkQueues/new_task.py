"""
In this one we'll create a Work Queue that will be used to distribute time-consuming tasks among multiple workers.
一个producer生产数据,多个consumer轮询消费(round-robin)
消息确认(message acknowledgment)
auto_ack=True的时候,consumer会告诉RabbitMQ指定的信息已经收到了并被消费了,如果连接意外中断,指定消息会被视为未被消费,将可继续被其他消费者消费
"""
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    ))
print(" [x] Sent %r" % message)
connection.close()
