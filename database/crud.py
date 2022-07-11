import pyodbc
from typing import List, Literal, Any


def getCursorConnect() -> tuple[pyodbc.Connection, pyodbc.Cursor]:
    # server = "server"
    # database = "databaseName"
    # username = "user"
    # password = "password"
    # strConnect = "Driver={SQL Server Native Client 11.0};Server="+server+";Database="+database+";UID="+username+";PWD="+ password"
    strConnect = "Driver={SQL Server Native Client 11.0};Server=LUANNPC\SQLEXPRESS;Database=Faculdade;Trusted_Connection=yes;"
    connect = pyodbc.connect(strConnect)
    cursor = connect.cursor()
    return cursor, connect


def read(column: str, table: str, limit: int = 10) -> (List[Any] | Literal[False] | None):
    sql = f"SELECT TOP ({limit}) {column} FROM {table}"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        output = cursor.fetchall()
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        if output:
            return output
        else:
            return None
    finally:
        connect.close()


def insert(table: str, column: str, value: str) -> bool:
    sql = f"INSERT INTO {table} ({column}) VALUES ({value})"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        return True
    finally:
        connect.close()


def delete(table: str, conditional: str, input: str) -> bool:
    sql = f"DELETE FROM {table} WHERE {conditional} = '{input}'"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        return True
    finally:
        connect.close()


def update(table: str, column: str, value: str, conditional: str, registration: str) -> bool:
    sql = f"UPDATE {table} SET {column} = '{value}' WHERE {conditional} = '{registration}'"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        return True
    finally:
        connect.close()

def returnExists(column: str, table: str, conditional: str, input: str) -> bool:
    sql = f"SELECT {column} FROM {table} WHERE {conditional} = '{input}'"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        output = cursor.fetchall()
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        if len(output) != 0:
            return True
        return None
    finally:
        connect.close()