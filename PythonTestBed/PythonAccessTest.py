import pyodbc
#
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\richard.henry\Documents\filev.accdb;')
cursor = conn.cursor()
cursor.execute(
'''select 
Upd_File,
TK_File,
TK_Base_Path
from filev''')
   
for row in cursor.fetchall():
    print (row[2],'\t',row[0], '\t',row[1])
