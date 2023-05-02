from fastapi import FastAPI, HTTPException, Depends
from typing import List
from sqlmodel import Session, select
from uuid import UUID
from db import create_tables, engine
from model import Books, Publishers, Authors, BookCreate, BookRead, BookUpdate


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_tables()


@app.post("/books/", response_model=BookRead)
def create_book(book: BookCreate):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book


@app.get("/books/", response_model=List[BookRead])
def read_all_books():
    with Session(engine) as session:
        books = session.exec(select(Books)).all()
        return books


@app.get("/books/{id}", response_model=BookRead)
def read_books(id: UUID):
    with Session(engine) as session:
        book = session.get(Books, id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book


@app.patch("/books/{id}", response_model=BookRead)
def update_books(id: UUID, book: BookUpdate):
    with Session(engine) as session:
        books = session.get(Books, id)
        if not books:
            raise HTTPException(status_code=404, detail="Book not found")
        book_data = book.dict(exclude_unset=True)
        for key, value in book_data.items():
            setattr(books, key, value)
        session.add(books)
        session.commit()
        session.refresh(books)
        return books


@app.post("/authors/")
def create_author(aut: Authors):
    with Session(engine) as session:
        session.add(aut)
        session.commit()
        session.refresh(aut)
        return aut


@app.post("/publishers/")
def create_publisher(pub: Publishers):
    with Session(engine) as session:
        session.add(pub)
        session.commit()
        session.refresh(pub)
        return pub
