from typing import Any


def build_response(success: bool, message: str, data: Any = None) -> dict:
    return {
        "success": success,
        "message": message,
        "data": data,
    }
