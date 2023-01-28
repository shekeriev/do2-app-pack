import os
from time import sleep, strftime
from random import randrange
from kafka import KafkaProducer
from prometheus_client import start_http_server, Counter

a = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Fat', 'Slim', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong']
d = ['Eat', 'Dream', 'Like', 'Adore', 'Trow', 'Love', 'Dislike']
e = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

facts = Counter('discovered_facts', 'Discovered facts count')
spent = Counter('time_spent', 'Time spent while discovering facts')

brokerhost = os.getenv('BROKER', 'localhost:9092')
topic = os.getenv('TOPIC', 'demo')
metricport = os.getenv('METRICPORT', 8000)

print(' [x] (K) Producer started. Press Ctrl+C to stop.')

start_http_server(int(metricport))
print(' [x] (K) Metrics available on port ' + str(metricport))

try:
    producer = KafkaProducer(bootstrap_servers=[brokerhost])
    print(' [x] (K) Working for ' + topic + ' on ' + brokerhost + '. Producing ...')
    while True:
        s = a[randrange(10)] + " " + b[randrange(11)] + " Are " + c[randrange(7)] + " And " + d[randrange(6)] + " " + e[randrange(6)]
        facts.inc()
        producer.send(topic, bytes(s, encoding='utf-8'))
        producer.flush()
        print(" [x] (K) " + strftime("%Y-%m-%d %H:%M:%S") + " Sent: %r" % s)
        slp = randrange(30, 90)
        spent.inc(slp)
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