# Library API FastAPI-SQLModel Sample

A simplified Library API FastAPI and SqlModel that connects to Postgresql based on the prior API I made with Django
Note: Even if there's multiple models inside, I only made API routes with Books model 'cause I'm lazy. But if you want to make them, you can do it in similar manner. And if you want to use it with different database(like SQLite or MySQL) you can just change the connection string in 'db.py' and voila!

## How to use:

1. Create and activate Python virtual environment
2. Install required libraries with `pip install -r requirements.txt` command inside root directory
3. Change the connection string parameters to the way you want
4. Run `uvicorn main:app --reload`
