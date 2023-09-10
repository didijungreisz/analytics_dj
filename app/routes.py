import threading
from flask import jsonify
from app import app
from core.kafka.kafka_producer import Producer
from core.kafka.kafka_consumer import Consumer
from core.analytics.analytics import Analytics
from config.redis_config import RedisConfig
from core.redis.redis_operations import RedisOperations

# Initialize Redis Operations
redis_ops = RedisOperations(RedisConfig.HOST, RedisConfig.PORT)

# Initialize Analytics
analytics = Analytics(redis_ops)

# Initialize Kafka Producer and start simulate_user_interactions
producer = Producer()
producer_thread = threading.Thread(target=producer.simulate_user_interactions)
producer_thread.start()

# Initialize Kafka Consumer and start consume_data
consumer = Consumer(redis_ops)
consumer_thread = threading.Thread(target=consumer.consume_data)
consumer_thread.start()


# routes for analytics functions
@app.route('/get_user_engagement/<user_id>')
def get_user_engagement(user_id):
    user_engagement = analytics.get_user_engagement(user_id)
    return jsonify({"user_engagement": user_engagement})


@app.route('/get_popular_products/<int:limit>')
def get_popular_products(limit):
    popular_products = analytics.get_popular_products(limit)
    return jsonify({"popular_products": popular_products})


@app.route('/get_event_frequency/<event_name>')
def get_event_frequency(event_name):
    event_frequency = analytics.get_event_frequency(event_name)
    return jsonify({"event_frequency": event_frequency})


@app.route('/get_user_data_by_date/<user_id>/<date>')
def get_user_data_by_date(user_id, date):
    user_data = analytics.get_user_data_by_date(user_id, date)
    return jsonify({"user_data": user_data})


@app.route('/get_user_data_between_dates/<user_id>/<start_date>/<end_date>')
def get_user_data_between_dates(user_id, start_date, end_date):
    user_data = analytics.get_user_data_between_dates(user_id, start_date, end_date)
    return jsonify({"user_data": user_data})