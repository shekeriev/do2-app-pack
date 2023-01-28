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

## Sample output

Here is a sample output:

```text
 [x] (R) Consumer started. Press Ctrl+C to stop.
 [x] (R) Subscribed for # on rabbitmq:5672. Listening ...
 [x] (R) 2023-01-28 13:04:57 / 'ram.info': b'info: ram load is 34'
 [x] (R) 2023-01-28 13:05:02 / 'cpu.warn': b'warn: cpu load is 73'
 [x] (R) 2023-01-28 13:05:20 / 'cpu.warn': b'warn: cpu load is 74'
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/rabbit-cons>
