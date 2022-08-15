"""
https://www.rabbitmq.com/tutorials/tutorial-four-python.html
exchangetype=fanout的时候,无法使用routing_key来绑定exchange和queue,因为生产者将消息广播后,每个消费者都能消费
direct模式可以绑定exchange和queue,这样消费者就能从指定routing_key来消费数据了

比如可以按日志级别对日志做不同处理,error级别存盘,info warning级别console
"""
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

severities = sys.argv[1:]
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for severity in severities:
    channel.queue_bind(
        exchange='direct_logs', queue=queue_name, routing_key=severity)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
