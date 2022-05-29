from kafka import KafkaConsumer
import os

brokerhost = os.getenv('BROKER', "localhost:9092")
topic = os.getenv('TOPIC', 'demo')

print(' [*] Consumer started. Subscribed for ' + topic + ' on ' + brokerhost + '. Press Ctrl+C to stop.')

try:
    consumer = KafkaConsumer(bootstrap_servers=[brokerhost])
    consumer.subscribe(topic)
    for message in consumer:
        print(' [x] ' + str(message))
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if consumer is not None:
        consumer.close()

print(' [x] ... closed.')