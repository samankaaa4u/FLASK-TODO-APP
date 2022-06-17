import hashlib
from database import connection

def hash_password(password: str) -> str:
    return hashlib.sha512(password.encode()).hexdigest()


def login_user(username="", password="") -> dict | None:
    sql = "SELECT * FROM users WHERE username=%s AND password=%s"
    
    results = connection(sql,(username, hash_password(password),),)
    if results == []: return None

    results = results[0]
    return {
        'id': results[0],
        'username': results[1],
        'date_created': results[3],
        'date_updated': results[4]
    }
