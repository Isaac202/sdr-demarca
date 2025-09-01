import os
from redis.asyncio import Redis
from dotenv import load_dotenv

load_dotenv()
redis = Redis.from_url(os.getenv("REDIS_URL"), decode_responses=True)

