import redis


class RedisClient:

    """

    """

    def __init__(self):

        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def get(self, key: str):

        """

        :param key:
        :return:
        """

        self.redis.get(name: 'foo', 'bar')

    def set(self, key: str, value: str):

        """

        :param key:
        :param value:
        :return:
        """

