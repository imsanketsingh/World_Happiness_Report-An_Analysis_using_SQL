import pandas as pd
import re
import math

def makeTXTFile(report, i):
    column_names = ', '.join([re.sub(r'[\s:()\-.+]+', '_', col) for col in report.columns])
    mySQLSyntax = 'INSERT INTO Report_{}({})'.format(i, column_names)
    mySQLSyntax += '\nVALUES '
    for index, row in report.iterrows():
        mySQLSyntax+='('
        for column_name in report.columns:
            value = row[column_name]
            if isinstance(value, str):
                 value= "'" + value + "'"
            elif isinstance(value, (float, int)) and math.isnan(value):
                value = 'NULL'
            mySQLSyntax+=str(value)
            mySQLSyntax+=','
        mySQLSyntax= mySQLSyntax[:-1]
        mySQLSyntax+='),\n'
    mySQLSyntax= mySQLSyntax[:-2]
    mySQLSyntax+= ';\n'
    file = open("report_{}.txt".format(i), "w")
    file.write(mySQLSyntax)
    file.close()
    
def SQLsyntaxForYear(i):
    report = pd.read_csv('D:/Documents/SQLworldHappinessReport/{}.csv'.format(i))
    makeTXTFile(report, i)
    
year = int(input("Enter Year: "))
SQLsyntaxForYear(year)
