from kafka import KafkaProducer
import os
from time import sleep,strftime
from random import randrange

brokerhost = os.getenv('BROKER', 'localhost:9092')
topic = os.getenv('TOPIC', 'demo')

print(' [x] (K) Producer started. Press Ctrl+C to stop.')

try:
    producer = KafkaProducer(bootstrap_servers=[brokerhost])
    print(' [x] (K) Working for ' + topic + ' on ' + brokerhost + '. Producing ...')
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
        evnt = ltype + ': ' + rtype + ' load is ' + str(res)
        producer.send(topic, bytes(evnt, encoding='utf-8'))
        producer.flush()
        print(" [x] (K) " + strftime("%Y-%m-%d %H:%M:%S") + " Sent: %r" % evnt)
        slp = randrange(5,20)
        print(' [x] (K) ' + strftime("%Y-%m-%d %H:%M:%S") + ' Sleep for ' + str(slp) + ' second(s).')
        sleep(slp)
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if producer is not None:
        producer.close()

print(' [x] (K) ... closed.')