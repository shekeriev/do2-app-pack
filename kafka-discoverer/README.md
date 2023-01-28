# Apache Kafka Sample Producer (Discoverer)

## Description

Publishes random events (fun facts about animals) on a **topic** to a **broker**. Both, the topic and broker, can be managed via environment variables. There is a random delay (between 30 and 90 seconds) between every two generated events

In addition, it exposes Prometheus metrics. The two application related ones are counters and are **discovered_facts_total** (how many facts are discovered so far since the last start) and **time_spent_total** (how much time in seconds was spent looking for facts)

## Available variables

| Variable  | Description                              | Default value  |
| --------- | ---------------------------------------- | -------------- |
| BROKER    | Broker to connect to (NAME:PORT)         | localhost:9092 |
| TOPIC     | Topic to publish to (topic)              | demo           |
| METRICPORT| Where to expose the metrics (PORT)       | 8000           |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [--net appnet] [-e VAR1=VALUE1 -e ...] shekeriev/kafka-discoverer

# Example
docker container run -d --name discoverer --net kafkanet -p 8888:5000 -e BROKER=kafka:9092 -e TOPIC=animal-facts -e METRICPORT=5000 shekeriev/kafka-discoverer
```

## Sample output

Here is a sample output from the console:

```text
 [x] (K) Producer started. Press Ctrl+C to stop.
 [x] (K) Metrics available on port 5000
 [x] (K) Working for animal-facts on kafka:9092. Producing ...
 [x] (K) 2023-01-28 18:45:05 Sent: 'Purple Lions Are Slim And Adore Tomatoes'
 [x] (K) 2023-01-28 18:45:05 Sleep for 81 second(s).
 [x] (K) 2023-01-28 18:46:26 Sent: 'Blue Donkeys Are Slim And Adore Bananas'
 [x] (K) 2023-01-28 18:46:26 Sleep for 59 second(s).
 [x] (K) 2023-01-28 18:47:25 Sent: 'Purple Pandas Are Slim And Dream Tomatoes'
 [x] (K) 2023-01-28 18:47:25 Sleep for 56 second(s).
 [x] (K) 2023-01-28 18:48:21 Sent: 'Green Cats Are Weak And Dream Potatoes'
 [x] (K) 2023-01-28 18:48:21 Sleep for 55 second(s).
 [x] (K) 2023-01-28 18:49:16 Sent: 'Purple Chameleons Are Fat And Eat Oranges'
 [x] (K) 2023-01-28 18:49:16 Sleep for 87 second(s).
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/kafka-discoverer>
