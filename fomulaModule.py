# Table Structure >>
# CREATE TABLE al_students (id INT(10) PRIMARY KEY, fname VARCHAR(32), sname VARCHAR(32), fullname VARCHAR(50), regnum CHAR(7) NOT NULL, class VARCHAR(10))



def updateData(table, findColumn, findValue, changeColumn, changeValue):
    # formula = "UPDATE al_students SET age = 13 WHERE name ='bob'"
    formula = f"UPDATE {table} SET {changeColumn} = '{changeValue}' WHERE {findColumn} = '{findValue}'"
    return formula


def addToTableFormula():
    Formula = "INSERT INTO al_students (id, fname, sname, fullname, regnum, class) VALUES (%s, %s, %s, %s, %s, %s)"
    return Formula
