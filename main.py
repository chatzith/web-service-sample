#!/usr/bin/python3

"""
A simple web-service for testing purposes.
"""

# pylint: disable="import-error"
# pylint: disable="too-few-public-methods"

from datetime import datetime, timedelta

import uvicorn
import yaml
from fastapi import FastAPI
from pydantic import BaseModel

from current_date import get_date

with open("users.yaml", encoding="ascii") as f:
    users = yaml.safe_load(f)


class UserData(BaseModel):
    """
    HTTP Post data validation.
    """

    username: str


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


@app.post("/user/")
async def get_user(data: UserData) -> dict:
    """
    Returns the user access permission data.

    :param data: username
    :type data: dict
    """

    item_dict = data.model_dump()

    if item_dict["username"] in users:
        item_dict["role"] = users[item_dict["username"]]["role"]
        item_dict["permission"] = True
        item_dict["expires"] = (datetime.now() + timedelta(hours=1)).strftime(
            "%Y-%m-%d %H:%M"
        )
    else:
        item_dict["role"] = "Not authorized user!"
        item_dict["permission"] = False
        item_dict["expires"] = "-"

    return {**item_dict}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
