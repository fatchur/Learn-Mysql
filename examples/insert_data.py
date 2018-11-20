from mysql_utils.mysql_basics import *

# build mysql helper object 
my_mysql = MysqlBasics(host="localhost", user="root", password='aaaaa')
# set parameter values
db_name = 'pertamina'
table_name = 'safety_report'
col_name_list = ['Kamera', 'Helm', 'Jacket', 'Sepatu_safety', 'Image_path'] 
value_list = ['hikvision', 'OK', 'OK', 'Unknwn', '/home/kk.jpg']
# call insert data method
my_mysql.insert_data(db_name, table_name, col_name_list, value_list)