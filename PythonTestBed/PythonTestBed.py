#!/usr/bin/env python
import os
import pathlib
import subprocess
import pyodbc
from PythonFTPTest import download_file
import csv

filepath="C:/Users/richard.henry/IBM/tpftoolkit42/SetTPFToolkitEnvVars.bat"
p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

stdout, stderr = p.communicate()
rc = p.returncode
print (rc) # is 0 if success

# environmental variables
PROD = False
tpfhome = ''
tpfshare = ''
tpfproj = ''
tpfwrks = ''
userprofile = ''
prod_server = 'http://tpftoolkitdeploy.prod.tvlport.com'
devl_server = 'http://tpftoolkitdeploy.dv.tvlport.com'
wsptemp = "wsptemp/"
docs = os.path.join(os.environ['USERPROFILE'], "Documents/")
if bool(PROD) == True:
    tk_deploy_update = prod_server+'/update/'
else:
    tk_deploy_update = devl_server+'/update/'
#tk_path = docs+wsptemp
# print(os.environ.get('TPFHOME','Not Populated'))
tpfhome = os.environ.get('TPFHOME','Not Populated')
tpfshare = os.environ.get('TPFSHARE','Not Populated')
tpfproj = os.environ.get('TPFPROJ','Not Populated')
tpfwrks = os.environ.get('TPFWRKS','Not Populated')

if tpfhome != 'Not Populated':
   tpfhome = os.environ.get('TPFHOME')
else:
   program64 = os.environ['ProgramW6432'] 
   #temp for testing 
   os.environ['TPFHOME'] = docs + '/IBM/TPF Toolkit v4x' 
   # os.environ['TPFHOME'] = program64 + '/IBM/TPF Toolkit v4x'
   tpfhome = os.environ.get('TPFHOME')


if tpfshare != 'Not Populated':
   tpfshare = os.environ.get('TPFSHARE')
else:
   os.environ['TPFSHARE'] = '/Config/tpfshare'
   tpfshare = os.environ.get('TPFSHARE')

if tpfproj != 'Not Populated':
   tpfproj = os.environ.get('TPFPROJ')
else:
   os.environ['TPFPROJ'] = '/Config/project/'
   tpfproj = os.environ.get('TPFPROJ')

if tpfwrks != 'Not Populated':
   tpfwrks = os.environ.get('TPFWRKS')
else:
   userprofile = os.environ['USERPROFILE']
   #temp for testing 
   os.environ['TPFWRKS'] = userprofile + '/IBM/tpftoolkit42/eclipse/workspace2'
   #os.environ['TPFWRKS'] = userprofile + '/IBM/tpftoolkit42/eclipse/workspace/'
   tpfwrks = os.environ.get('TPFWRKS')
  
print(tpfhome)
print(tpfshare)
print(tpfproj)
print(tpfwrks)

rc = 0;

#conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\richard.henry\Documents\filev.accdb;')
#cursor = conn.cursor()
#cursor.execute(
#'''select 
#Upd_File,
#TK_File,
#TK_Base_Path
#from filev''')
full_qual_filev = docs + 'filev_lc.csv'
print(full_qual_filev)
with open(full_qual_filev) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:   
#for row in cursor.fetchall():
        if row['Upd_File'] [0] != '#':
            if row['TK_Base_Path'] == 'TPFHOME':
               tk_path_file = pathlib.Path(tpfhome + '/' + row['Upd_File'])
               download_file(tk_deploy_update + row['Upd_File'],tk_path_file)
            elif row['TK_Base_Path'] == 'TPFSHARE':
                tk_path_file = pathlib.Path(tpfhome + tpfshare + '/' + row['Upd_File'])
                download_file(tk_deploy_update + row['Upd_File'],tk_path_file)
            elif row['TK_Base_Path'] == 'PROJECT':
                tk_path_file = pathlib.Path(tpfhome + tpfproj + '/' + row['Upd_File'])
                download_file(tk_deploy_update + row['Upd_File'],tk_path_file)
            elif row['TK_Base_Path'] == 'ECLIPSEWRKSPC':
                tk_path_file = pathlib.Path(tpfwrks+ '/' + row['Upd_File'])
                download_file(tk_deploy_update + row['Upd_File'],tk_path_file)
            else:
                print('VC0100 Location Unknown')
            
       
print("VC0120 Travelport Toolkit refreshed")