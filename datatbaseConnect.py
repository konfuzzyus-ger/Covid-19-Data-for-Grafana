import mysql.connector
import config
from pprint import pprint
import datetime
import helper

dbConnectCfg = {
    'user' : config.db_user ,
    'password' : config.db_password,
    'host' : config.db_host,
    'port' : config.db_port,
    'database' : config.db_scheme
}

def QueryDB(query, fetch):
    cnx = mysql.connector.connect(**dbConnectCfg)
    cursor = cnx.cursor()

    cursor.execute(query)
    result = ''
    if (fetch):
        result = cursor.fetchall()
    cursor.close()
    cnx.close()
    if (config.debug):
        pprint(result)
    return result

def QueryDBParameter(query, par):
    cnx = mysql.connector.connect(**dbConnectCfg)
    cursor = cnx.cursor()
    par_esc = []
    for t in par:
        par_esc.append(helper.MySQLEscape(t))
    cursor.execute(query, par_esc)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    if (config.debug):
        pprint(result)
    return result

def QueryDBParameterWOO(query, par):
    cnx = mysql.connector.connect(**dbConnectCfg)
    cursor = cnx.cursor()
    par_esc = []
    for t in par:
        par_esc.append(helper.MySQLEscape(t))
    result = cursor.execute(query, par_esc)
    cnx.commit()
    cursor.close()
    cnx.close()
    if (config.debug):
        pprint(result)
    return result

def insertTotalCases(date, cases, country):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "originalData (datetime, cases, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(cases)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp)
    return

def insertPercentage1D(date, percentage, country):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage1d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp)
    return

def insertPercentage3D(date, percentage, country):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage3d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp)
    return

def insertPercentage5D(date, percentage, country):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage5d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp)
    return

def insertPercentage7D(date, percentage, country):
    date = helper.formatDateTime(date)
    SQLReq = "INSERT INTO " + config.db_prefix + "percentage7d (date, percentage, country) VALUES ( %s , %s , %s );"
    tmp = []
    tmp.append(date)
    tmp.append(percentage)
    tmp.append(country)
    QueryDBParameterWOO(SQLReq, tmp)
    return

#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)