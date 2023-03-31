# Denpandency injection and conversion of control

> Library reference
>
> [Dependency injection and inversion of control in Python — Dependency Injector 4.41.0 documentation (ets-labs.org)](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html)

什么是依赖：

```python
import os


class ApiClient:
    def __init__(self) -> None:
        self.api_key = os.getenv("API_KEY")  # <-- 依赖
        self.timeout = int(os.getenv("TIMEOUT"))  # <-- 依赖 # type:ignore


class Service:
    def __init__(self) -> None:
        self.api_client = ApiClient()  # <-- 依赖


def main():
    service = Service()  # <-- 依赖


if __name__ == "__main__":
    main()
```

以上代码中，`main`函数、`Service`对象、`ApiClient`对象耦合，依赖关系为`main <- Service <- ApiClient <- os.env`。这样写有什么问题呢？不够灵活，不便于测试。依赖关系中的任意一环出问题都会导致依赖链上的类或函数无法实例化或者测试，那么，怎么改进呢？

```python
class ApiClient:
    def __init__(self, api_key, timeout) -> None:
        self.api_key = api_key  # <-- dependency is injected
        self.timeout = timeout  # <-- dependency is injected


class Service:
    def __init__(self, api_client) -> None:
        self.api_client = api_client  # <-- dependency is injected


def main(service: Service):  # <-- dependency is injected
    pass


if __name__ == '__main__':
    main(
        service=Service(
            api_client=ApiClient(
                api_key="APIKEY",
                timeout=5
            )
        )
    )
```

这样就完成了解耦，依赖控制反转了，`main`函数、`Service`对象、`ApiClient`对象现在可以灵活的使用、测试。当然，灵活是有代价的，使用依赖注入，会有大量重复的代码，所幸，使用框架可以解决这一问题！