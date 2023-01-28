from kafka import KafkaConsumer
import os
from datetime import datetime

brokerhost = os.getenv('BROKER', "localhost:9092")
topic = os.getenv('TOPIC', 'demo')

print(' [x] (K) Consumer started. Press Ctrl+C to stop ...')

try:
    consumer = KafkaConsumer(bootstrap_servers=[brokerhost])
    consumer.subscribe(topic)
    print(' [x] (K) Subscribed for ' + topic + ' on ' + brokerhost + '. Listening ...')
    for evnt in consumer:
        print(' [x] (K) ' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' / ' + str(evnt.offset) + ' / ' + str(evnt.value))
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if consumer is not None:
        consumer.close()

print(' [x] (K) ... closed.')