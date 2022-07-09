from sqlite3 import Cursor, connect
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


def read(column: str, table: str) -> (List[Any] | Literal[False] | None):
    sql = f"SELECT {column} FROM {table}"
    connect = getCursorConnect()[1]
    try:
        cursor = getCursorConnect()[0].execute(sql)
        row = cursor.fetchall()
        cursor.commit()
    except pyodbc.ProgrammingError:
        return False
    else:
        if row:
            return row
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


def delete(table: str, registration: str) -> bool:
    sql = f"DELETE FROM {table} WHERE Matricula = '{registration}'"
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
