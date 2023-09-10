import json
import datetime


class Analytics:
    def __init__(self, db):
        self.db = db

    def get_user_engagement(self, user_id):
        return self.db.get_value('user_engagement', user_id)

    def get_popular_products(self, limit=5):
        return self.db.get_sorted_set('popular_products', limit)

    def get_event_frequency(self, event_name):
        return self.db.get_value('event_frequencies', event_name)

    def get_user_data_by_date(self, user_id, date):
        start_date = f'{date} 00:00:00'
        end_date = f'{date} 23:59:59'

        redis_key = f'user:{user_id}:interactions'
        start_ts = int(datetime.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S').timestamp())
        end_ts = int(datetime.datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S').timestamp())

        user_data = self.db.get_user_interactions_by_date_range(redis_key, start_ts, end_ts)
        return [json.loads(data) for data in user_data]

    def get_user_data_between_dates(self, user_id, start_date, end_date):
        redis_key = f'user:{user_id}:interactions'

        start_ts = int(datetime.datetime.strptime(start_date, '%Y-%m-%d').timestamp())
        end_ts = int(datetime.datetime.strptime(end_date, '%Y-%m-%d').timestamp())

        user_data = self.db.get_user_interactions_by_date_range(redis_key, start_ts, end_ts)
        return [json.loads(data) for data in user_data]
