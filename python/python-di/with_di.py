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
