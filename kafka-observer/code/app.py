import os
from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from flask import Flask
from time import strftime

app = Flask(__name__)

appport = os.getenv('APPPORT', 5000)

@app.route('/')
def index():
  with open('app.tpl') as f:
    template = f.read()

  facts = ""

  brokerhost = os.getenv('BROKER', "localhost:9092")
  topic = os.getenv('TOPIC', 'demo')

  try:
    print("* trying to connect ...")
    consumer = KafkaConsumer(bootstrap_servers=[brokerhost])
    print("* ... connected.")
    print("* trying to subscribe ...")
    consumer.subscribe(topic)
    print("* ... subscribed.")
    consumer.poll()
    tp = TopicPartition(topic, 0)
    end_offset = consumer.end_offsets([tp])
    last_record = list(end_offset.values())[0]
    print("* end is " + str(last_record))
    if last_record < 5:
      read_records = last_record
    else:
      read_records =5
    if read_records > 0:
      print("* will get last " + str(read_records))
      consumer.seek(tp,last_record - read_records)
      idx = 1
      for evnt in consumer:
        print("* received an event")
        print(evnt.value.decode("utf-8"))
        facts = facts + "<li>" + str(evnt.value.decode("utf-8")) + "</li>"
        idx = idx + 1
        if idx > read_records:
          break
    else:
      print("* nothing there yet")
      facts = "Not a single fact has been discovered yet. Try again later."
  except Exception as e: 
    print(e)
    facts = "Error: Something happened while trying to talk to the broker: " + brokerhost
  finally:
    if consumer is not None:
      consumer.close()
    print("* done")
      
  result = template.replace("{FACTS}", facts)

  result = result.replace("{BUILD}", strftime("%Y-%m-%d %H:%M:%S"))

  return result

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=appport)