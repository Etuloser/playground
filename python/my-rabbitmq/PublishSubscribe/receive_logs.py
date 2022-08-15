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

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')


result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()