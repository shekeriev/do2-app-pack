# Apache Kafka Sample Consumer

## Description

Subcribes for messages on a topic to a broker

## Available variables

| Variable  | Description                                 | Default value  |
| --------- | ------------------------------------------- | -------------- |
| BROKER    | Broker to connect to (NAME:PORT)            | localhost:9092 |
| TOPIC     | Topic  to subscribe for (topic)             | demo           |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [-e VAR1=VALUE1 -e ...] shekeriev/kafka-cons 

# Example
docker container run -d --name cons -e BROKER=kafka:9092 -e TOPIC=demo-topic shekeriev/kafka-cons
```
