import redis

r = redis.Redis(
    host="singapore-redis.render.com",
    port=6379,
    ssl=True,
    username="",
    password="",
)

r.set("foo", "bar")

print(r.get("foo"))
