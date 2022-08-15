from kafka import KafkaConsumer
consumer = KafkaConsumer(
    'test',
    bootstrap_servers='119.91.25.133:30092',
    auto_offset_reset='latest'
)
for msg in consumer:
    print(msg)
