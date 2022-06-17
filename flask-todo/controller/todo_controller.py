
from database import connection, connection_insert


def get_todos(user_id: str) -> list | None:
    sql = """SELECT todo.id,title,description,date_created,date_updated, status.status, todo.id FROM todo 
INNER JOIN status ON
todo.status_id=status.id
WHERE todo.user_id=%s"""
    params = (user_id,)
    results: list = connection(sql, params)

    return results

def get_status() -> list | None:
    sql = "SELECT * FROM STATUS"
    params = ()
    results: list = connection(sql, params)

    return results


def get_todo_by_id (id: str ) -> dict | None:
    sql = """SELECT id,title,description,date_created,date_updated,status_id FROM todo WHERE id=%s;"""
    params = (id,)
    
    results: list = connection(sql, params)
    print (results)
    if results == []: return None

    results = results[0] 
    return {
        'id': results[0],
        'title': results[1],
        'description': results[2],
        'date_added': results[3],
        'date_updated': results[4],
        'status_id': results[5]
    }


def add_todo(user_id: str, title: str, description: str):
    sql = """INSERT INTO todo (user_id, title, description, status_id) VALUES (%s, %s, %s,1) """
    params = (user_id,title, description)
    connection_insert (sql, params)
    
