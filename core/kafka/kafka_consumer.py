import json
from kafka import KafkaConsumer
from config.kafka_config import KafkaConfig


class Consumer:
    def __init__(self, db_ops):
        self.consumer = KafkaConsumer(
            bootstrap_servers=KafkaConfig.BOOTSTRAP_SERVERS,
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )
        self.consumer.subscribe(KafkaConfig.TOPICS)
        self.db_ops = db_ops

    def update_user_engagements(self, user_id):
        self.db_ops.update_value('user_engagement', user_id, 1)

    def update_popular_products(self, product_id):
        self.db_ops.update_sorted_set('popular_products', product_id, 1)

    def update_event_frequencies(self, interaction_type):
        self.db_ops.update_value('event_frequencies', interaction_type, 1)

    def store_date(self, interaction_data, timestamp, user_id):
        redis_key = f'user:{user_id}:interactions'
        self.db_ops.store_date(redis_key, interaction_data, timestamp)

    def process_interaction_data(self, interaction_data):
        user_id = interaction_data['user_id']
        interaction_type = interaction_data['interaction_type']
        product_id = interaction_data['product_id']
        timestamp = interaction_data['timestamp']

        self.update_user_engagements(user_id)
        self.update_popular_products(product_id)
        self.update_event_frequencies(interaction_type)
        self.store_date(interaction_data, timestamp, user_id)

    def consume_data(self):
        for message in self.consumer:
            print(message.value)
            interaction_data = message.value
            self.process_interaction_data(interaction_data)
