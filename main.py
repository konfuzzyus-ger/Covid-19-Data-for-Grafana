import sys
import mysql.connector
import config
import datatbaseConnect
import csv
import time

def main():
    dbConnectCfg = {
        'user': config.db_user,
        'password': config.db_password,
        'host': config.db_host,
        'port': config.db_port,
        'database': config.db_scheme
    }
    dbConnectionRaw = mysql.connector.connect(**dbConnectCfg)
    dbConnection = dbConnectionRaw.cursor()
    pathFile = f'{config.datapath}/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    with open(pathFile, encoding="utf-8", errors="ignore", newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        totalCases = list(spamreader)
        l_main = len(totalCases)
        print('truncate')
        truncateStart = time.time()
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}diff1d ;", False, dbConnection)
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}percentage1d ;", False, dbConnection)
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}percentage3d ;", False, dbConnection)
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}percentage5d ;", False, dbConnection)
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}percentage7d ;", False, dbConnection)
        datatbaseConnect.QueryDB(f"TRUNCATE {config.db_prefix}originalData ;", False, dbConnection)
        truncateStop = time.time()
        print(f'truncate done, took {truncateStop - truncateStart} seconds')
        # percentage for one day
        dataP1 = []
        dataD1 = []
        print("percentage for one day")
        time1d = time.time()
        for i in range(1, l_main):
            len_side = len(totalCases[i])
            for j in range(4, len_side-1):
                per = 0
                if (float(totalCases[i][j]) != 0):
                    try:
                        per = ((float(totalCases[i][j+1]) / float(totalCases[i][j]))-1)*100
                    except:
                        per = ((float(totalCases[i][j]) / float(totalCases[i][j])) - 1) * 100
                try:
                    if (totalCases[i][0] == ''):
                        dataP1.append([totalCases[0][j+1], per, totalCases[i][1]])
                    else:
                        dataP1.append([totalCases[0][j+1], per, totalCases[i][1] + ", " + totalCases[i][0]])
                except:
                    pass
                diff = float(totalCases[i][j+1]) - float(totalCases[i][j])
                try:
                    if (totalCases[i][0] == ''):
                        dataD1.append([totalCases[0][j+1], diff, totalCases[i][1]])
                    else:
                        dataD1.append([totalCases[0][j + 1], diff, totalCases[i][1] + ", " + totalCases[i][0]])
                except:
                    pass
        time1dE = time.time()
        print(f"Calculation of difference and percentage 1 day took {time1dE - time1d} seconds for {len(dataP1)} datapoints")
        datatbaseConnect.insertPercentage1D(dataP1, dbConnection)
        time1dD1 = time.time()
        datatbaseConnect.insertDiffCases1D(dataD1, dbConnection)
        time1dD = time.time()
        print(f"Database took {time1dD1 - time1dE} seconds for inserting percentage 1 day and {time1dD - time1dD1} for inserting difference one day")
        # precentage for 3 days
        dataP3 = []
        print("percentage for 3 days")
        time3d = time.time()
        for i in range(1, l_main):
            len_side = len(totalCases[i])
            try:
                for j in range(4, len_side, 3):
                    per = 0
                    per1 = 0
                    per2 = 0
                    if ((float(totalCases[i][j]) != 0) & (j+1 < len_side)):
                        try:
                            per1 = ((float(totalCases[i][j+1]) / float(totalCases[i][j]))-1)*100
                        except:
                            continue
                    else:
                        if (j+1 >= len_side):
                            continue
                    if ((float(totalCases[i][j+1]) != 0) & (j + 2 < len_side)):
                        try:
                            per2 = ((float(totalCases[i][j + 2]) / float(totalCases[i][j+1])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j + 2 >= len_side):
                            continue
                    per = (per1 + per2) / 2
                    try:
                        if (totalCases[i][0] == ''):
                            dataP3.append([totalCases[0][j+1], per, totalCases[i][1]])
                        else:
                            dataP3.append([totalCases[0][j+1], per, totalCases[i][1] + ", " + totalCases[i][0]])
                    except:
                        pass
            except:
                continue
        time3dE = time.time()
        print(f"Calculation of percentage 3 days took {time3dE - time3d} seconds for {len(dataP3)} datapoints")
        datatbaseConnect.insertPercentage3D(dataP3, dbConnection)
        time3dD = time.time()
        print(f"Database took {time3dD - time3dE} seconds for inserting percentage 3 days")
        # precentage for 5 days
        dataP5 = []
        time5d = time.time()
        print("percentage for 5 days")
        for i in range(1, l_main):
            len_side = len(totalCases[i])
            try:
                for j in range(4, len_side, 5):
                    per = 0
                    per1 = 0
                    per2 = 0
                    per3 = 0
                    per4 = 0
                    if ((float(totalCases[i][j]) != 0) & (j+1 < len_side)):
                        try:
                            per1 = ((float(totalCases[i][j+1]) / float(totalCases[i][j]))-1)*100
                        except:
                            continue
                    else:
                        if (j+1 >= len_side):
                            continue
                    if ((float(totalCases[i][j+1]) != 0) & (j + 2 < len_side)):
                        try:
                            per2 = ((float(totalCases[i][j + 2]) / float(totalCases[i][j+1])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j + 2 >= len_side):
                            continue
                    if ((float(totalCases[i][j+2]) != 0) & (j + 3 < len_side)):
                        try:
                            per3 = ((float(totalCases[i][j + 3]) / float(totalCases[i][j+2])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j+3 >= len_side):
                            continue
                    if ((float(totalCases[i][j+3]) != 0) & (j + 4 < len_side)):
                        try:
                            per4 = ((float(totalCases[i][j + 4]) / float(totalCases[i][j+3])) - 1) * 100
                        except:
                            continue
                    else:
                        if  (j+4 >= len_side):
                            continue
                    per = (per1 + per2 + per3 + per4) / 4
                    try:
                        if (totalCases[i][0] == ''):
                            dataP5.append([totalCases[0][j+2], per, totalCases[i][1]])

                        else:
                            dataP5.append([totalCases[0][j+2], per, totalCases[i][1] + ", " + totalCases[i][0]])
                    except:
                        pass
            except:
                continue
        time5dE = time.time()
        print(f"Calculation of percentage 5 days took {time5dE - time5d} seconds for {len(dataP5)} datapoints")
        datatbaseConnect.insertPercentage5D(dataP5, dbConnection)
        time5dD = time.time()
        print(f"Database took {time5dD - time5dE} seconds for inserting percentage 5 days")
        # precentage for 7 days
        dataP7 = []
        print("percentage for 5 days")
        time7d = time.time()
        for i in range(1, l_main):
            len_side = len(totalCases[i])
            try:
                for j in range(4, len_side, 7):
                    per = 0
                    per1 = 0
                    per2 = 0
                    per3 = 0
                    per4 = 0
                    per5 = 0
                    per6 = 0
                    if ((float(totalCases[i][j]) != 0) & (j+1 < len_side)):
                        try:
                            per1 = ((float(totalCases[i][j+1]) / float(totalCases[i][j]))-1)*100
                        except:
                            continue
                    else:
                        if (j+1 >= len_side):
                            continue
                    if ((float(totalCases[i][j+1]) != 0) & (j + 2 < len_side)):
                        try:
                            per2 = ((float(totalCases[i][j + 2]) / float(totalCases[i][j+1])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j+2 >= len_side):
                            continue
                    if ((float(totalCases[i][j+2]) != 0) & (j + 3 < len_side)):
                        try:
                            per3 = ((float(totalCases[i][j + 3]) / float(totalCases[i][j+2])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j+3 >= len_side):
                            continue
                    if ((float(totalCases[i][j+3]) != 0) & (j + 4 < len_side)):
                        try:
                            per4 = ((float(totalCases[i][j + 4]) / float(totalCases[i][j+3])) - 1) * 100
                        except:
                            continue
                    else:
                        if (j+4 >= len_side):
                            continue
                    if ((float(totalCases[i][j+4]) != 0) & (j + 5 < len_side)):
                        try:
                            per5 = ((float(totalCases[i][j + 5]) / float(totalCases[i][j+4])) - 1) * 100
                        except:
                            continue
                    else:
                        if  (j+5 >= len_side):
                            continue
                    if ((float(totalCases[i][j+5]) != 0) & (j + 6 < len_side)):
                        try:
                            per6 = ((float(totalCases[i][j + 6]) / float(totalCases[i][j+5])) - 1) * 100
                        except:
                            continue
                    else:
                        if  (j+6 >= len_side):
                            continue
                    per = (per1 + per2 + per3 + per4 + per5 + per6) / 6
                    try:
                        if (totalCases[i][0] == ''):
                            dataP7.append([totalCases[0][j+3], per, totalCases[i][1]])
                        else:
                            dataP7.append([totalCases[0][j + 3], per, totalCases[i][1] + ", " + totalCases[i][0]])
                    except:
                        pass
            except:
                continue
        time7dE = time.time()
        print(f"Calculation of percentage 5 days took {time7dE - time7d} seconds for {len(dataP7)} datapoints")
        datatbaseConnect.insertPercentage7D(dataP7, dbConnection)
        time7dD = time.time()
        print(f"Database took {time7dD - time7dE} seconds for inserting percentage 7 days")
        # total data
        dataT = []
        print("complete data")
        timeT = time.time()
        for i in range(1, l_main):
            len_side = len(totalCases[i])
            for j in range(4, len_side):
                checkNumber = True
                try:
                    int = float(totalCases[i][j])
                except:
                    checkNumber = False
                try:
                    if (checkNumber):
                        if (totalCases[i][0] == ''):
                            dataT.append([totalCases[0][j], totalCases[i][j], totalCases[i][1]])
                        else:
                            dataT.append([totalCases[0][j], totalCases[i][j], totalCases[i][1]])
                    else:
                        if (totalCases[i][0] == ''):
                            dataT.append([totalCases[0][j], totalCases[i][j-1], totalCases[i][1]])

                        else:
                            dataT.append([totalCases[0][j], totalCases[i][j-1], totalCases[i][1] + ", " + totalCases[i][0]])
                except:
                    pass
        timeTE = time.time()
        print(f"Collection of complete data took {timeTE - timeT} seconds for {len(dataT)} datapoints")
        datatbaseConnect.insertTotalCases(dataT, dbConnection)
        timeTD = time.time()
        print(f"Database took {timeTD - timeTE} seconds for inserting complete data")
    dbConnectionRaw.commit();
    dbConnectionRaw.close()

if __name__ == '__main__':
    sys.exit(main())