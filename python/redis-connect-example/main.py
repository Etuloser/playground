import redis

r = redis.Redis(
    host="singapore-redis.render.com",
    port=6379,
    username="red-cmb4ghda73kc73bp9mq0",
    password="COZN3YxrE3xllU0gUaMyJEG5cKmN6OPY",
    decode_responses=True,
)

r.set("foo", "bar")
r.get("foo")
