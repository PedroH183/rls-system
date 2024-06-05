import os
from database import get_db
from sqlalchemy import text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def populate():
    def insert(filePath):
        try:
            db = get_db()
            sql_file = open(BASE_DIR + filePath, "r")
            sql = text(sql_file.read())

            db.execute(sql)
            db.commit()
        except:
            print(f"Error in file: {filePath}")

    insert("/table.sql")
    insert("/valuesTable.sql")
    insert("/roles.sql")
    insert("/grantRoles.sql")
    insert("/policy.sql")
