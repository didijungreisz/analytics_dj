import json

import redis


class RedisOperations:
    def __init__(self, host, port):
        self.redis_client = redis.StrictRedis(
            host=host,
            port=port,
            decode_responses=True
        )

    def update_value(self, key, field, increment_by):
        self.redis_client.hincrby(key, field, increment_by)

    def update_sorted_set(self, key, member, increment_by):
        self.redis_client.zincrby(key, increment_by, member)

    def store_date(self, key, interaction_data, timestamp):
        self.redis_client.zadd(key, {json.dumps(interaction_data): int(timestamp)})

    def get_value(self, key, field):
        return int(self.redis_client.hget(key, field) or 0)

    def get_sorted_set(self, key, limit=5):
        return [(member, score) for member, score in
                self.redis_client.zrevrangebyscore(key, '+inf', '-inf', start=0, num=limit, withscores=True)]

    def get_user_interactions_by_date_range(self, redis_key, start_ts, end_ts):
        return self.redis_client.zrangebyscore(redis_key, min=start_ts, max=end_ts)
