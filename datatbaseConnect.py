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
    for t in par:
        par_esc.append(helper.MySQLEscape(t))
    result = cursor.execute(query, par_esc)
    if (config.debug):
        pprint(result)
    return result

def insertTotalCases(date, cases, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "originalData (datetime, cases, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(cases)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

def insertPercentage1D(date, percentage, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage1d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

def insertPercentage3D(date, percentage, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage3d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

def insertPercentage5D(date, percentage, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage5d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

def insertPercentage7D(date, percentage, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage7d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

def insertDiffCases1D(date, cases, country, dbConnection):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "diff1d (datetime, cases, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(cases)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp, dbConnection)
    return

#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)