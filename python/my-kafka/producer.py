from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['119.91.25.133:30092'])
for _ in range(100):
    producer.send('test', b'some_message_bytes')
producer.flush()
