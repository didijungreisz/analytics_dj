import json
import time
from kafka import KafkaProducer
from core.interaction_factory.interaction_factory import InteractionFactory
from config.kafka_config import KafkaConfig


class Producer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.producer = KafkaProducer(
                bootstrap_servers=KafkaConfig.BOOTSTRAP_SERVERS,
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
        return cls._instance

    @staticmethod
    def generate_interaction_data():
        interaction_data = InteractionFactory.create_interaction_data()
        return interaction_data

    def simulate_user_interactions(self):
        while True:
            interaction_data = self.generate_interaction_data()
            self.producer.send(interaction_data['site_name'], value=interaction_data)
            self.producer.flush()
            time.sleep(8)
