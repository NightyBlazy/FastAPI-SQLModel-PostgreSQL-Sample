from sqlmodel import create_engine, Session, SQLModel


from sqlalchemy.orm import sessionmaker

USER = "myuser"
PASS = "123456789"
HOST = "localhost"
DB = "Test2"


engine = create_engine(
    f"postgresql://{USER}:{PASS}@{HOST}/{DB}", echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)
