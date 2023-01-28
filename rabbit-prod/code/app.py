#!/usr/bin/env python
import pika
import os
from time import sleep,strftime
from random import randrange

brokerhost = os.getenv('BROKER', 'localhost')
brokerport = os.getenv('BROKERPORT', 5672)
exchange = os.getenv('EXCHANGE', 'demo')

print(' [x] (R) Producer started. Press Ctrl+C to stop.')

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=brokerhost, port=brokerport))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange, exchange_type='topic')

    print(' [x] (R) Working against ' + exchange + ' on ' + brokerhost + ':' + str(brokerport) + '. Producing ...')

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
        routing_key = rtype + '.' + ltype
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=msg)
        print(" [x] (R) " + strftime("%Y-%m-%d %H:%M:%S") + " Sent: %r" % msg)
        slp = randrange(5,20)
        print(' [x] (R) ' + strftime("%Y-%m-%d %H:%M:%S") + ' Sleep for ' + str(slp) + ' second(s).')
        sleep(slp)
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if connection is not None:
        connection.close()