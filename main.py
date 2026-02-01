#!/usr/bin/python3

"""
A simple web-service for testing purposes.
"""

# pylint: disable="import-error"

import uvicorn
from fastapi import FastAPI

from current_date import get_date

app = FastAPI()


@app.get("/")
async def get_greetings(option: str, user: str | None = None):
    """
    Returns either a simple greeting
    or the current date and time.

    :param option: "greet" or "date
    :type option: str
    :param user: username
    :type user: str | None
    """
    if option == "greet":
        return {"message": f"Hello, {user}!"}

    return {"message": get_date()}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
