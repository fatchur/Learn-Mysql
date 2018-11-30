import mysql.connector


class MysqlBasics():
	def __init__(self, host="localhost", user="root", password="xxxx" ):
		"""
		Creating new trainable tensor (filter) as weight
		Args:
			host:		a string, host name
			user:       a string, user name
			password:   a string, the password		
		"""
		self.host = host
		self.user = user
		self.password = password
		self.mydb = mysql.connector.connect( host=self.host, user=self.user, passwd=self.password)
		self.mycursor = self.mydb.cursor()
	
	def create_table(self, db_name, table_name, col_name_list, col_datatype_list, print_command=False):
		"""
		Method for creating a db table
		Args:
			db_name:		    a string, the db name
			table_name:         a string, the table name
			col_name_list:      a list of string comtains of column names, ex: ['id', 'name', 'age']
			col_datatype_list:  a list of string contains of column data types, ex: ['INT AUTO_INCREMENT PRIMARY KEY', 'VARCHAR(255)', 'INT']
		"""
		command_string = "CREATE TABLE " + db_name + "." + table_name + " ("
		for i in range (len(col_name_list)):
			command_string = command_string + " " + col_name_list[i] + " " + col_datatype_list[i] + ", "
		command_string = command_string[:-2]
		command_string = command_string + " )"
		if print_command:
			print ("your command string : ====>>")
			print (command_string)
		self.mycursor.execute(command_string)
		self.mydb.commit()

	def insert_data (self, db_name, table_name, col_name_list, col_value_list, print_command=False):
		"""
		Method for inserting a data to db table
		Args:
			db_name:		    a string, the db name
			table_name:         a string, the table name
			col_name_list:      a list of string comtains of column names, ex: ['name', 'age']
			col_datatype_list:	a list of contains of column values, ex: ['Shasa', 31]
		"""
		command_string = "INSERT INTO " + db_name + "." + table_name + " ("
		for i in col_name_list:
			command_string = command_string + " " + i + ", "
		command_string = command_string[:-2]
		command_string = command_string + ") VALUES ("
		for i in col_value_list:
			if isinstance(i,str):
				command_string = command_string + " '" + i + "', "
			else:
				command_string = command_string + " " + i + ", "
		command_string = command_string[:-2]
		command_string = command_string + " )"
		if print_command:
			print ("your command string : ====>>")
			print (command_string)
		self.mycursor.execute(command_string)
		self.mydb.commit()
	
	def select_data (self, db_name, table_name, target_col_name_list, condition_string, print_command=True):
		"""
		Method for retreiving data from database
		Args:
			db_name:		    	a string, the db name
			table_name:         	a string, the table name
			target_col_name_list:	a list of string comtains of column names, ex: ['name', 'age']
			condition_string:		a condition string, ex: WHERE age = 10, WHERE name LIKE '%james'
		"""
		command_string = "SELECT "
		for i in target_col_name_list:
			command_string = command_string + i + ", "
		command_string = command_string[-2] + " FROM " + db_name + "." + table_name + " " + condition_string
		if print_command:
			print (command_string)
		self.mycursor.execute(command_string)
		self.mydb.commit()

	def right_join(self):
		print ('under development')
	
	def left_join(self):
		print ('under development')

	def delete_row(self):
		print ('under development')
	
	def delete_column(self):
		print ('under development')





