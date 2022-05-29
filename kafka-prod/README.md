# Apache Kafka Sample Producer

## Description

Publishes random log messages with random delay (between 5 and 20 seconds) between every two messages

## Available variables

| Variable  | Description                              | Default value  |
| --------- | ---------------------------------------- | -------------- |
| BROKER    | Broker to connect to (NAME:PORT)         | localhost:9092 |
| TOPIC     | Topic to publish to (topic)              | demo           |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [-e VAR1=VALUE1 -e ...] shekeriev/kafka-prod 

# Example
docker container run -d --name prod -e BROKER=kafka:9092 -e TOPIC=demo-topic shekeriev/kafka-prod
```
