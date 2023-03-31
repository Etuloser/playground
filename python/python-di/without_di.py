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
