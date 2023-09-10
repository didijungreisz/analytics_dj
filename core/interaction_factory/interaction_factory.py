import datetime
import random

from core.interaction_factory import InteractionType


class InteractionFactory:
    @staticmethod
    def create_interaction_data():
        sites_names = ['asos', 'ebay', 'aliexpress']
        user_id = str(random.randint(1, 10))
        site_id = random.randint(1, 3)
        site_name = sites_names[site_id - 1]
        interaction_type = random.choice(list(InteractionType))
        product_id = str(random.randint(1, 100))
        interaction_data = {
            'user_id': user_id,
            'site_id': site_id,
            'site_name': site_name,
            'interaction_type': interaction_type.value,
            'product_id': product_id,
            'timestamp': datetime.datetime.now().timestamp()
        }
        return interaction_data
