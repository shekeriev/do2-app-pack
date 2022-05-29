# RabbitMQ Sample Consumer

## Description

Binds to a topic exchange and listens for messages based on a topic

## Available variables

| Variable   | Description                                 | Default value  |
| ---------- | ------------------------------------------- | -------------- |
| BROKER     | Broker to connect to (name)                 | localhost      |
| BROKERPORT | Broker's port to use (5672)                 | 5672           |
| EXCHANGE   | Exchange to bind to (topic)                 | demo           |
| TOPICS     | Topics to subscribe for (topic.subtopic)    | #              |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [--net appnet] [-e VAR1=VALUE1 -e ...] shekeriev/rabbit-cons 

# Example
docker container run -d --name cons --net appnet -e BROKER=rabbitmq -e BROKERPORT=5672 -e EXCHANGE=demo -e TOPICS='demo.*' shekeriev/rabbit-cons
```
