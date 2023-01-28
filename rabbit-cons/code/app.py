#!/usr/bin/env python
import pika
import os
from time import strftime

brokerhost = os.getenv('BROKER', 'localhost')
brokerport = os.getenv('BROKERPORT', 5672)
exchange = os.getenv('EXCHANGE', 'demo')
topics = os.getenv('TOPICS', '#')

print(' [x] (R) Consumer started. Press Ctrl+C to stop.')

def callback(ch, method, properties, body):
    print(" [x] (R) " + strftime("%Y-%m-%d %H:%M:%S") + " / %r: %r" % (method.routing_key, body))

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=brokerhost, port=brokerport))
    channel = connection.channel()
    channel.exchange_declare(exchange=exchange, exchange_type='topic')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=topics)
    print(' [x] (R) Subscribed for ' + str(topics) + ' on ' + brokerhost + ':' + str(brokerport) + '. Listening ...')
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
except Exception as ex:
    print(str(ex))
except KeyboardInterrupt:
    pass
finally:
    if connection is not None:
        connection.close()

print('  [x] (R) ... closed.')