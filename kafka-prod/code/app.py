from kafka import KafkaProducer
import os
from time import sleep
from random import randrange

brokerhost = os.getenv('BROKER', 'localhost:9092')
topic = os.getenv('TOPIC', 'demo')

print(' [*] Producer started. Working for ' + topic + ' on ' + brokerhost + '. Press Ctrl+C to stop.')

try:
    producer = KafkaProducer(bootstrap_servers=[brokerhost])
    while True:
        # determine resource type
        res = randrange(0,100)
        rtype = 'cpu'
        if res % 2 == 0:
            rtype = 'ram'
        # determine resource load
        res = randrange(0,100)
        ltype = 'info'
        if res > 50:
            ltype = 'warn'
        if res > 80:
            ltype = 'crit'
        msg = ltype + ': ' + rtype + ' load is ' + str(res)
        producer.send(topic, bytes(msg, encoding='utf-8'))
        producer.flush()
        print(" [x] Sent %r" % msg)
        slp = randrange(5,20)
        print(' [x] Sleep for ' + str(slp) + ' second(s).')
        sleep(slp)
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if producer is not None:
        producer.close()

print(' [x] ... closed.')