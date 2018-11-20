from mysql_utils.mysql_basics import *

# build mysql helper object 
my_mysql = MysqlBasics(host="localhost", user="root", password='aaaaaaa')
# set parameter values
db_name = 'pertamina'
table_name = 'safety_report'
col_name_list = ['id', 'Timestamp', 'Kamera', 'Helm', 'Jacket', 'Kacamata', 'Sarung_tangan', 'Sepatu_safety', 'Lengkap', 'Image_path'] 
col_datatype_list = ['INT AUTO_INCREMENT PRIMARY KEY', 'TIMESTAMP', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)', 'VARCHAR(255)']
# call create table method
my_mysql.create_table(db_name, table_name, col_name_list, col_datatype_list)