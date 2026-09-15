import sqlite3
import json


def getTasks(date=None, day=None, time=None):
    if time is not None and date is None and day is None:
        raise ValueError("Time cannot be passed without Date or Day.")

    connection = sqlite3.connect("chotu.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    if time is not None:
        cursor.execute("""
            SELECT name, message
            FROM tasks
            WHERE (deadlineDate = ? OR deadlineDay = ?)
              AND deadlineTime = ?
        """, (date, day, time))
    else:
        cursor.execute("""
            SELECT name, message, deadlineTime
            FROM tasks
            WHERE deadlineDate = ?
               OR deadlineDay = ?
        """, (date, day))

    tasks = cursor.fetchall()
    connection.close()

    result = []

    for task in tasks:
        result.append({
            "name": task["name"],
            "message": task["message"],
            "time": task["deadlineTime"] if time is None else None
        })

    return json.dumps(result, indent=4)