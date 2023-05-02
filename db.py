from sqlmodel import create_engine, Session, SQLModel


from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql://myuser:123456789@localhost/Test2", echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)
