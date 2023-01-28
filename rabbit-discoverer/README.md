# RabbitMQ Sample Producer (Discoverer)

## Description

Publishes random log messages (fun facts about animals) on a **topic** to a **broker**. Both, the topic and broker, can be managed via environment variables. There is a random delay (between 30 and 90 seconds) between every two generated messages

In addition, it exposes Prometheus metrics. The two application related ones are counters and are **discovered_facts_total** (how many facts are discovered so far since the last start) and **time_spent_total** (how much time in seconds was spent looking for facts)


## Available variables

| Variable   | Description                              | Default value  |
| ---------- | ---------------------------------------- | -------------- |
| BROKER     | Broker to connect to (name)              | localhost      |
| BROKERPORT | Broker's port to use (5672)              | 5672           |
| EXCHANGE   | Exchange to bind to (topic)              | demo           |
| METRICPORT | Where to expose the metrics (PORT)       | 8000           |

## Usage

```bash
# Syntax
docker container run [-d|-it] [--name fancyname] [--net appnet] [-e VAR1=VALUE1 -e ...] shekeriev/rabbit-discoverer 

# Example
docker container run -d --name discoverer --net appnet -p 8888:5000 -e BROKER=rabbitmq -e BROKERPORT=5672 -e TOPIC=demo -e METRICPORT=5000 shekeriev/rabbit-discoverer
```

## Sample output

Here is a sample output:

```text
 [x] (R) Producer started. Press Ctrl+C to stop.
 [x] (K) Metrics available on port 5000
 [x] (R) Working against demo on rabbitmq:5672. Producing ...
 [x] (R) 2023-01-28 20:09:23 Sent: 'Pink Chameleons Are Fast And Like Potatoes'
 [x] (R) 2023-01-28 20:09:23 Sleep for 59 second(s).
 [x] (R) 2023-01-28 20:10:22 Sent: 'Gray Lions Are Fast And Trow Tomatoes'
 [x] (R) 2023-01-28 20:10:22 Sleep for 47 second(s).
 [x] (R) 2023-01-28 20:11:09 Sent: 'Pink Coalas Are Slim And Adore Oranges'
 [x] (R) 2023-01-28 20:11:09 Sleep for 87 second(s).
 [x] (R) 2023-01-28 20:12:36 Sent: 'White Lions Are Slim And Adore Bananas'
 [x] (R) 2023-01-28 20:12:36 Sleep for 32 second(s).
 [x] (R) 2023-01-28 20:13:08 Sent: 'Yellow Coalas Are Weak And Adore Tomatoes'
 [x] (R) 2023-01-28 20:13:08 Sleep for 56 second(s).
 [x] (R) 2023-01-28 20:14:04 Sent: 'Purple Coalas Are Short And Like Cucumbers'
 [x] (R) 2023-01-28 20:14:04 Sleep for 49 second(s).
```

## Source code

The latest version of the source code can be obtained from here: <https://github.com/shekeriev/do2-app-pack/tree/main/rabbit-discoverer>
