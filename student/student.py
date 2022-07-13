from database.crud import delete, read, insert, returnExists, update
import datetime

def convertDate(date: str) -> str:
    date = datetime.datetime.strptime(date, "%d/%m/%Y")
    date = str(f"{date.year}/{date.month}/{date.day}")
    return date

