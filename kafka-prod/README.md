# Apache Kafka Sample Producer

## Description

Publishes random events (log messages) on a **topic** to a **broker**. Both, the topic and broker, can be managed via environment variables. There is a random delay (between 5 and 20 seconds) between every two generated events

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

## Sample output

Here is a sample output:

```text
 [x] (K) Producer started. Press Ctrl+C to stop.
 [x] (K) Working for prep on kafka:9092. Producing ...
 [x] (K) 2023-01-28 12:16:54 Sent: 'crit: cpu load is 85'
 [x] (K) 2023-01-28 12:16:54 Sleep for 5 second(s).
 [x] (K) 2023-01-28 12:16:59 Sent: 'crit: cpu load is 86'
 [x] (K) 2023-01-28 12:16:59 Sleep for 16 second(s).
 [x] (K) 2023-01-28 12:17:15 Sent: 'crit: ram load is 82'
 [x] (K) 2023-01-28 12:17:15 Sleep for 9 second(s).
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/kafka-prod>
