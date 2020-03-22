import os
import config
from pprint import pprint
import _mysql
import datatbaseConnect

def MySQLEscape(input):
    output = _mysql.escape_string(str(input))
    return output

def formatDateTime(input):
    arr = input.split('/')
    return '20' + arr[2] + '-' + arr[0] + '-' + arr[1]

def Writezero3D(date, country, region):
    try:
        if (region == ''):
            datatbaseConnect.insertPercentage3D(date, 0, country)
        else:
            datatbaseConnect.insertPercentage3D(date, 0, country + ", " + region)
    except:
        pass

def Writezero5D(date, country, region):
    try:
        if (region == ''):
            datatbaseConnect.insertPercentage5D(date, 0, country)
        else:
            datatbaseConnect.insertPercentage5D(date, 0, country + ", " + region)
    except:
        pass

def Writezero7D(date, country, region):
    try:
        if (region == ''):
            datatbaseConnect.insertPercentage7D(date, 0, country)
        else:
            datatbaseConnect.insertPercentage7D(date, 0, country + ", " + region)
    except:
        pass


#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)