import redis

r = redis.Redis(host='119.91.25.133', port=30379, db=0)
got = r.ping()
print(got)
