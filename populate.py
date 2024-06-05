import os
from database import get_db
from sqlalchemy import text

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def populate():
    def insert(filePath):
        db = get_db()
        sql_file = open(BASE_DIR + filePath, "r")
        sql = text(sql_file.read())

        db.execute(sql)

        try:
            db.commit()
        except:
            print(f"Error in file: {filePath}")

    def tryInsert(file_path):
        try:
            insert(file_path)
        except:
            pass

    tryInsert("/table.sql")
    tryInsert("/valuesTable.sql")
    tryInsert("/roles.sql")
    tryInsert("/grantRoles.sql")
    tryInsert("/policy.sql")
