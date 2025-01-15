# ./src/python/apps/services/redis_service.py

import os
import redis

class RedisService:
  def __init__(self):
    self.client = redis.StrictRedis(
      host=os.getenv("REDIS_HOST", "docker.redis"),
      port=int(os.getenv("REDIS_PORT", 6379)),
      password=os.getenv("REDIS_PASSWORD", "JeSterkWachtwoord"),
      decode_responses=True,
    )

  def set_value(self, key, value, expiration=3600):
    """Set a value in Redis with an optional expiration."""
    return self.client.setex(key, expiration, value)

  def get_value(self, key):
    """Get a value from Redis."""
    return self.client.get(key)

  def delete_key(self, key):
    """Delete a key from Redis."""
    return self.client.delete(key)
