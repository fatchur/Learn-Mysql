import mysql.connector


class MysqlBasics():
    def __init__(self, host="localhost", user="root", pasword="xxxx" ):
        self.host = host
        self.user = user
        self.password = password
        self.mydb = mysql.connector.connect( host=self.host, user=self.user, passwd=self.password)
        self.mycursor = self.mydb.cursor()
    
    def create_table(self, db_name, table_name, col_name_list, col_datatype_list):
        command_string = "CREATE TABLE " + db_name + "." + table_name + " ("
        for i in range (len(col_name_list)):
            command_string = command_string + " " + col_name_list[i] + " " + col_datatype_list[i] + ", "
        command_string = command_string + " )"
        print (command_string)
        self.mycursor.execute(command_string)
        self.mydb.commit()

    def insert_data (self, db_name, table_name, col_name_list, col_value_list):
        command_string = "INSERT INTO"



