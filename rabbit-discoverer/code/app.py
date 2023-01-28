#!/usr/bin/env python
import os
from time import sleep,strftime
from random import randrange
import pika
from prometheus_client import start_http_server, Counter

a = ['Blue', 'Black', 'Yellow', 'White', 'Green', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Red']
b = ['Tigers', 'Lions', 'Crocodiles', 'Horses', 'Donkeys', 'Dogs', 'Cats', 'Bears', 'Pandas', 'Coalas', 'Chameleons', 'Lizards']
c = ['Fat', 'Slim', 'Fast', 'Slow', 'Tall', 'Short', 'Weak', 'Strong']
d = ['Eat', 'Dream', 'Like', 'Adore', 'Trow', 'Love', 'Dislike']
e = ['Oranges', 'Bananas', 'Tomatoes', 'Potatoes', 'Onions', 'Cucumbers', 'Nuts']

facts = Counter('discovered_facts', 'Discovered facts count')
spent = Counter('time_spent', 'Time spent while discovering facts')

brokerhost = os.getenv('BROKER', 'localhost')
brokerport = os.getenv('BROKERPORT', 5672)
exchange = os.getenv('EXCHANGE', 'demo')
metricport = os.getenv('METRICPORT', 8000)

print(' [x] (R) Producer started. Press Ctrl+C to stop.')

start_http_server(int(metricport))
print(' [x] (K) Metrics available on port ' + str(metricport))

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=brokerhost, port=brokerport))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='topic')

    print(' [x] (R) Working against ' + exchange + ' on ' + brokerhost + ':' + str(brokerport) + '. Producing ...')

    while True:
        color = a[randrange(10)]
        animal = b[randrange(11)]
        msg = color + " " + animal + " Are " + c[randrange(7)] + " And " + d[randrange(6)] + " " + e[randrange(6)]
        routing_key = color.lower() + '.' + animal.lower()
        facts.inc()
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
        print(" [x] (R) " + strftime("%Y-%m-%d %H:%M:%S") + " Sent: %r" % msg)
        slp = randrange(30, 90)
        spent.inc(slp)
        print(' [x] (R) ' + strftime("%Y-%m-%d %H:%M:%S") + ' Sleep for ' + str(slp) + ' second(s).')
        sleep(slp)
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if connection is not None:
        connection.close()

print(' [x] (R) ... closed.')