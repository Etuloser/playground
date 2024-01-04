# Redis Connect Example

> Library reference
>
> https://redis.io/docs/connect/clients/python/

## redis测试服务器

https://dashboard.render.com/r/red-cmb4ghda73kc73bp9mq0

## redis-py

### 安装

```bash
pip install redis
```

### 连接

注意`rediss://`开头的链接串要配置`ssl=True`

```bash
r = redis.Redis(
    host="singapore-redis.render.com",
    port=6379,
    ssl=True,
    username="red-cmb4ghda73kc73bDECBA",
    password="COZN3YxrE3xllU0gUaMyJEG5cKmABCED",
)
```