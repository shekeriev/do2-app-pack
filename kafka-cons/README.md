# Apache Kafka Sample Consumer

## Description

Subcribes for events on a **topic** to a **broker**. Both, the topic and broker, can be managed via environment variables

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

## Sample output

Here is a sample output:

```text
 [x] (K) Consumer started. Press Ctrl+C to stop ...
 [x] (K) Subscribed for prep on kafka:9092. Listening ...
 [x] (K) 2023-01-28 11:37:50 / 276 / b'warn: ram load is 53'
 [x] (K) 2023-01-28 11:37:59 / 277 / b'info: cpu load is 40'
 [x] (K) 2023-01-28 11:38:11 / 278 / b'info: cpu load is 47'
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/kafka-cons>
