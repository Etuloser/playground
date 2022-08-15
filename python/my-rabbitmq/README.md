# RabbitMQ

> Library reference
>
> [Messaging that just works — RabbitMQ](https://www.rabbitmq.com/#getstarted)

*rabbitmq.yaml*

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rabbitmq
  labels:
    app: rabbitmq
spec:
  containers:
    - name: rabbitmq
      image: rabbitmq:3.10-management
---
apiVersion: v1
kind: Service
metadata:
  name: rabbitmq
spec:
  type: NodePort
  selector:
    app: rabbitmq
  ports:
    - port: 5672
      targetPort: 5672 
      nodePort: 30072
      name: port1
    - port: 15672
      targetPort: 15672 
      nodePort: 30172
      name: port2
```

## Hello world

```bash
pip install pika
```

*send.py*

```python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='119.91.25.133', port=30072))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
```

*receive.py*

```python
import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='119.91.25.133', port=30072))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(
        queue='hello', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
```