# User Engagement Analytics System

## Description

The User Engagement Analytics System is a Python-based application that provides real-time analytics on user interactions with various e-commerce platforms.
It leverages Flask for web services, Kafka for real-time data processing, and Redis for efficient data storage.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Setup Instructions](#setup-instructions)
- [Performance Optimizations](#performance-optimizations)
- [Additional Notes](#additional-notes)

---

## Architecture Overview

The User Engagement Analytics System is designed with a modular and scalable architecture. It consists of the following components:

### Flask Application

- Located in the `app` directory.
- Handles HTTP requests and responses. The `routes.py` file defines endpoints for fetching analytics data.

### Kafka

- Acts as a message broker for real-time data processing.
- Utilized for both producing and consuming user interaction data.
- Components related to Kafka are in the `core/kafka` directory.

### Redis

- Serves as a high-performance, in-memory data store.
- Used for storing user engagement data and other analytics.
- Redis-related operations are defined in the `core/redis` directory.

### Object-Oriented Design

- The codebase follows object-oriented principles, promoting modularity and code reusability.
- Key classes include `Producer`, `Consumer`, `Analytics`, `RedisOperations`, and `InteractionFactory`.

### Parallelism and Distribution

- The system leverages threading to enable concurrent execution of tasks, enhancing performance.

### Design Patterns

- Singleton Pattern is used in `kafka_producer.py` to ensure a single instance of the Kafka producer is used throughout the application.
- Factory Pattern is implemented in `interaction_factory.py` to generate interaction data.

## Setup Instructions

Follow these steps to set up and run the User Engagement Analytics System:

1. **Docker Configuration**

   Ensure Docker is installed, then run the following command to set up services like Zookeeper, Kafka, and Redis:

   ```bash
   docker-compose up
   ```

2. **Install Dependencies**

   Install the required Python packages by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Application**

   Start the Flask application, along with Kafka and Redis:

   ```bash
   python run.py
   ```

   The application is now running and ready to receive HTTP requests.

---

### Viewing Kafka Messages

**Kafdrop Web Interface**:
   - Open a web browser and go to `http://localhost:9000`.
   - Kafdrop is a Kafka web UI that allows you to inspect Kafka topics and messages.

**Explore Topics and Messages**:
   - You'll now be able to explore the Kafka topics and view messages within each topic.

### Viewing Redis Data

**Redis Commander Web Interface**:
   - Open a web browser and go to `http://localhost:8081`.

**Explore Redis Data**:
   - You'll now be able to explore the Redis database and view keys, values, and other data.

Please ensure that Docker services (Kafka, Zookeeper, Redis) are up and running before accessing these interfaces.

## Performance Optimizations

Performance optimizations in the project include:

### Thread-based Parallelism: 
Using threads for Kafka message consumption and data simulation enables concurrent processing, improving throughput.

### Redis Caching: 
Redis is used for caching frequently accessed data like user engagement, popular products, and event frequencies, reducing database queries.

### Optimized Data Structures: 
Redis sorted sets are used to efficiently store and retrieve popular products and user interactions by date range.

### Singleton Pattern

The Singleton Pattern is employed in `kafka_producer.py` to ensure that only one instance of the Kafka producer is created and used throughout the application. This reduces overhead and promotes efficient resource utilization.


---

## Additional Notes

### Docker Considerations

Running Flask with Kafka in the same Docker container may cause issues due to resource constraints. 
Consider using separate containers for Flask and Kafka for better resource management and scalability.
Note that Flask is executed locally and is not containerized within Docker, 
unlike the other services.

### Future Improvements

- Implementing a caching layer to further optimize data retrieval.
- Error handling: Adding error handling (try-catch blocks etc.) for potential exceptions that may occur during Kafka, Redis or other operations.
- Testing: Implement unit tests and integration tests to ensure the reliability of the application.

### Special Considerations

- When deploying in production, consider load balancing across multiple Kafka brokers for scalability.

---
