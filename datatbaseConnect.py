import mysql.connector
import config
from pprint import pprint
import datetime
import helper

def QueryDB(query, fetch, cursor):
    cursor.execute(query)
    result = ''
    if (fetch):
        result = cursor.fetchall()
    if (config.debug):
        pprint(result)
    return result

def QueryDBParameter(query, par, cursor):
    par_esc = []
    for t in par:
        par_esc.append(helper.MySQLEscape(t))
    cursor.execute(query, par_esc)
    result = cursor.fetchall()
    if (config.debug):
        pprint(result)
    return result

def QueryDBParameterWOO(query, par, cursor):
    par_esc = []
    for d, p, c in par:
        date = str(helper.formatDateTime(d))
        percentage = str(p)
        country = str(c)
        par_esc.append((date,percentage,country))
    result = cursor.executemany(query, par_esc)
    if (config.debug):
        pprint(result)
    return result

def insertTotalCases(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}originalData (datetime, cases, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

def insertPercentage1D(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}percentage1d (date, percentage, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

def insertPercentage3D(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}percentage3d (date, percentage, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

def insertPercentage5D(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}percentage5d (date, percentage, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

def insertPercentage7D(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}percentage7d (date, percentage, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

def insertDiffCases1D(data, dbConnection):
    SQLReq = f"REPLACE INTO {config.db_prefix}diff1d (datetime, cases, country) VALUES ( %s , %s , %s );"
    QueryDBParameterWOO(SQLReq, data, dbConnection)

#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)