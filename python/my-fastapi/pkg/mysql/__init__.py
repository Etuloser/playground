from sqlmodel import create_engine


class Client:
    def __init__(self) -> None:
        pass

    def new_engine(self, db_url):
        return create_engine(db_url)
