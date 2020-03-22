import os
import config
from pprint import pprint
import _mysql

def MySQLEscape(input):
    output = _mysql.escape_string(str(input))
    return output

def formatDateTime(input):
    arr = input.split('/')
    return '20' + arr[2] + '-' + arr[0] + '-' + arr[1]

#### DO NOT CHANGE ####
if __name__ == "__main__":
    exit(1)