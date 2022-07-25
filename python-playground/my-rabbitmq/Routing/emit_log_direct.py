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

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()