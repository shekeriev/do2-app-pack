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

## Sample output

Here is a sample output:

```text
 [x] (R) Producer started. Press Ctrl+C to stop.
 [x] (R) Working against prep on rabbitmq:5672. Producing ...
 [x] (R) 2023-01-28 13:04:48 Sent: 'warn: cpu load is 70'
 [x] (R) 2023-01-28 13:04:48 Sleep for 9 second(s).
 [x] (R) 2023-01-28 13:04:57 Sent: 'info: ram load is 34'
 [x] (R) 2023-01-28 13:04:57 Sleep for 5 second(s).
 [x] (R) 2023-01-28 13:05:02 Sent: 'warn: cpu load is 73'
 [x] (R) 2023-01-28 13:05:02 Sleep for 18 second(s).
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/rabbit-prod>
