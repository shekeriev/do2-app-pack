# RabbitMQ Sample Producer

## Description

Publishes random log messages to a topic based exchange with random delay (between 5 and 20 seconds) between every two messages

## Available variables

| Variable   | Description                              | Default value  |
| ---------- | ---------------------------------------- | -------------- |
| BROKER     | Broker to connect to (name)              | localhost      |
| BROKERPORT | Broker's port to use (5672)              | 5672           |
| EXCHANGE   | Exchange to bind to (topic)              | demo           |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [--net appnet] [-e VAR1=VALUE1 -e ...] shekeriev/rabbit-prod 

# Example
docker container run -d --name prod --net appnet -e BROKER=rabbitmq -e BROKERPORT=5672 -e TOPIC=demo shekeriev/rabbit-prod
```
