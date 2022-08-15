"""
之前的例子都是一一对应,即一个消息由一个Consumer消费
发布/订阅(Pulish/Subscibe)模式:一个Producer生产消息,多个Consumer通过订阅消费,一对多关系
Exchanges
实际上,Producer并不关注他生产的消息去往哪个queue,消息与queue的绑定将由Exchanges完成
Temporary queues
在queue声明的时候给空字符串将自动生成一个临时queue,同时指定其exclusive=True讲会在连接断开时销毁这个临时queue

rabbitmqctl list_exchanges
rabbitmqctl list_bindings
"""
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')
message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()