#!/usr/bin/env python
import pika
import os
from flask import Flask
from time import sleep,strftime
from random import randrange
from threading import Thread

app = Flask(__name__)

appport = os.getenv('APPPORT', 5000)
brokerhost = os.getenv('BROKER', 'localhost')
brokerport = os.getenv('BROKERPORT', 5672)
exchange = os.getenv('EXCHANGE', 'demo')
topics = os.getenv('TOPICS', '#')

@app.route('/')
def index():
    with open('app.tpl') as f:
        template = f.read()

    facts = ""

    try:
        messages = open("/tmp/messages.log", "r")

        for r in messages.readlines():
            facts = facts + "<li>" + r + "</li>"

        messages.close()
    except:
        facts = "No data yet. Try again later."

    result = template.replace("{FACTS}", facts)

    result = result.replace("{BUILD}", strftime("%Y-%m-%d %H:%M:%S"))

    return result

def callback(ch, method, properties, body):
    messages = open('/tmp/messages.log', 'a')
    print(" [x] (R) " + strftime("%Y-%m-%d %H:%M:%S") + " / %r: %r" % (method.routing_key, body))
    messages.write(str(body.decode("utf-8"))+"\n")
    messages.close()

def longrun():
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

if __name__ == '__main__':
    p = Thread(target=longrun)
    p.start()
    app.run(host='0.0.0.0', port=appport)
    p.join()