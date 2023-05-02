from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from uuid import UUID, uuid4


class BooksBase(SQLModel):
    book_name: str = Field(max_length=100)
    book_author: UUID = Field(foreign_key="author.author_id")
    book_publisher: UUID = Field(foreign_key="publisher.publisher_id")
    book_page: int = Field()
    book_rating: int = Field()
    book_desc: str = Field(default="Description not found...")
    book_rdate: str = Field(max_length=10)

    authors: "Authors" = Relationship(back_populates="books")
    publishers: "Publishers" = Relationship(back_populates="books")


class Books(BooksBase, table=True):
    __tablename__ = 'books'

    book_id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)

    authors: "Authors" = Relationship(back_populates="books")
    publishers: "Publishers" = Relationship(back_populates="books")


class BookCreate(BooksBase):
    pass


class BookRead(BooksBase):
    book_id: UUID


class BookUpdate(SQLModel):
    book_id: Optional[UUID]
    book_name: Optional[str]
    book_author: Optional[UUID]
    book_publisher: Optional[UUID]
    book_page: Optional[int]
    book_rating: Optional[int]
    book_desc: Optional[str]
    book_rdate: Optional[str]


class Publishers(SQLModel, table=True):
    __tablename__ = 'publisher'

    publisher_id: UUID = Field(
        default_factory=uuid4, primary_key=True, index=True)
    publisher_name: str = Field(max_length=100)
    publisher_fdate: str = Field(max_length=10)
    publisher_adress: str = Field(default="Blank address")

    books: Books = Relationship(back_populates="publishers")


class Authors(SQLModel, table=True):
    __tablename__ = 'author'

    author_id: UUID = Field(default_factory=uuid4,
                            primary_key=True, index=True)
    author_name: str = Field(max_length=100)
    author_bdate: str = Field(max_length=10)

    books: Books = Relationship(back_populates="authors")
