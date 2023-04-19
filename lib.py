from typing import Callable

import uvicorn
from fastapi import FastAPI

decorated_functions = set()


def expose(func: Callable):
    decorated_functions.add(func)

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def run_server():
    app = FastAPI()
    method_list: set[Callable] = decorated_functions
    for method in method_list:
        app.add_api_route(
            f"/api/{method.__name__}",
            method,
            methods=["POST"]
        )
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )
