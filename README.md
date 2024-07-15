# Kafka Producer-Consumer Example with Flask REST API

This project demonstrates a simple Kafka producer-consumer setup using Python, and also provides a REST API service to access the data using Flask.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [TASK 1: Container Up, Produce And Consume Message](#task-1-container-up-produce-and-consume-message)
  - [Kafka Setup](#kafka-setup)
  - [Running the Kafka Producer](#running-the-kafka-producer)
- [TASK 2: Scrape, Produce, Consume And Save Informations](#task-2-scrape-produce-consume-and-save-imformations)
  - [Running the Kafka Consumer](#running-the-kafka-consumer)
- [REST API Service](#rest-api-service)
  - [Running the Flask REST API](#running-the-flask-rest-api)
- [API Endpoints](#api-endpoints)
- [Example Data](#example-data)
- [License](#license)

## Overview

This project consists of two main tasks:
1. **TASK 1**: Create a kafka topic with Kafka CLI command. After that, produce and consume the you written the messages.
2. **TASK 2**: Scrape data from a website and produce it to a Kafka topic. Consume messages from the Kafka topic, save them to a JSON file, and provide a REST API to access the data.

## Prerequisites

- Docker and Docker Compose
- Python 3.7 or higher
- Kafka and Zookeeper
- `pip` package installer

## Environment Setup

### 1. Create a Virtual Environment

First, create a virtual environment to manage dependencies:

        python3 -m venv venv
        source venv/bin/activate

### 2. Install Dependencies

Install the required Python packages:

        pip install -r requirements.txt


# TASK 1: Container Up, Produce And Consume Message

## Kafka Setup

1. Start Kafka and Zookeeper

Ensure you have Docker and Docker Compose installed. Use the following docker-compose.yml file to set up Kafka and Zookeeper:

        docker-compose up -d

<img width="565" alt="Screenshot 2024-07-14 at 14 40 02" src="https://github.com/user-attachments/assets/65bd2eea-344e-4460-b794-20b8db700e7e">


2. Learn Your Kafka Container ID

Use the following command to learn what is your Kafka Container ID:

        docker ps

<img width="1355" alt="Screenshot 2024-07-14 at 14 41 20" src="https://github.com/user-attachments/assets/cf0aa65e-1e42-45f5-95eb-1b91a8f8eb3b">


3. Create Kafka Topic

Use the following command to create a topic name what you want:

        docker exec -it <kafka_container_id> kafka-topics.sh --create --topic your_topic_name --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

<img width="1358" alt="Screenshot 2024-07-14 at 14 45 12" src="https://github.com/user-attachments/assets/50568d40-0519-4d19-bb7f-f1d60b0b74c1">


4. Produce Message in Kafka Topic

        docker exec -it <kafka_container_id> kafka-console-producer.sh --topic your_topic_name --bootstrap-server localhost:9092
        >`Write_your_message_here`

5. Consume Message From Kafka Topic

        docker exec -it <kafka_container_id> kafka-console-consumer.sh --topic your_topic_name --bootstrap-server localhost:9092 --from-beginning

<img width="1366" alt="Screenshot 2024-07-14 at 15 18 41" src="https://github.com/user-attachments/assets/476e95f3-e079-4d9d-bf8e-4b75900471bd">


# TASK 2: Scrape, Produce, Consume And Save Informations

1. Running the Kafka Producer

The producer scrapes data from a website and produces it to a Kafka topic.

        python producer.py

2. Running the Kafka Consumer

Run the Consumer like below:

        python consumer.py

3. Rest API Service

The Flask REST API serves the data stored in the JSON file.

Run the Flask Application:

        python app.py

## API Endpoints

- GET /products: Returns a list of all products.

Example Data

Example data format in `data.json`:

[
    {
        "name": "Bulbasaur",
        "price": "£63.00",
        "short_description": "Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun’s rays, the seed grows progressively larger.",
        "stock": "45 in stock"
    },
    {
        "name": "Ivysaur",
        "price": "£87.00",
        "short_description": "There is a bud on this Pokémon’s back. To support its weight, Ivysaur’s legs and trunk grow thick and strong. If it starts spending more time lying in the sunlight, it’s a sign that the bud will bloom into a large flower soon.",
        "stock": "142 in stock"
    }
]

License

This project is licensed under the MIT License.



