from jwt import encode

def create_token(data: dict)-> str:
    return encode(payload=data, key="my_secret_key", algorithm="HS256")

def validate_token(token: str) -> dict:
    return decode(token, key="my_secret_key", algorithms=['HS256'])