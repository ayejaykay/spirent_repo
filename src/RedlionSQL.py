import urllib.request
import os

# Import pyodbc library for Microsoft Sql Server APIs
# If it is not installed on the machine, then install it

try:
    import pyodbc 
except ImportError:
    os.system("pip install pyodbc")

__location__ = os.path.dirname(os.path.realpath(__file__)) # Gives path to RedlionSQL.py directory, so that os.system calls are not called from __main__ directory

class RedlionSQL:

    def __init__(self, database, table_name) -> None:
        self.database = database
        self.table_name = table_name
        self.odbc_installer = "msodbcsql.msi"
        self.driver_str = "{ODBC Driver 18 for SQL Server}"
        self.server_str = "yk-ms-sql3.hq.corp.redlion.net"
        self.UID = "Teststand"
        self.PWD = "Redli0n$"

        try:
            self.connection = pyodbc.connect(f"Driver={self.driver_str};ENCRYPT=no;SERVER={self.server_str};DATABASE={self.database};UID={self.UID};PWD={self.PWD}")
        except pyodbc.InterfaceError as e:
            print(e)
            urllib.request.urlretrieve("https://go.microsoft.com/fwlink/?linkid=2266640", self.odbc_installer) # Link where I copied this url from --> https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16
            os.system(f'msiexec /i "{__location__}\\{self.odbc_installer}" ADDLOCAL=ALL') # Link to msiexec docs --> https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec
            os.remove(self.odbc_installer)
            try:
                self.connection = pyodbc.connect(f"Driver={self.driver_str};ENCRYPT=no;SERVER={self.server_str};DATABASE={self.database};UID={self.UID};PWD={self.PWD}")
            except pyodbc.InterfaceError:
                print("Error getting ODBC Driver. Exiting")
                exit()

        self.cursor = self.connection.cursor()
    
    ################### select_all ##################
    # Description: Fetch the entire table from the  #
    #              database.                        #
    # Params:                                       #
    #   - self: referance to class object           #
    # Returns:                                      #
    #   - Cursor Object containing specified table  #
    # Notes:                                        #
    #   - Caller will have to use pyodbc functions  #
    #     to parse data inside object variable.     #
    #################################################

    def select_all(self):
        return self.cursor.execute(f'SELECT * FROM {self.table_name}')
    
    ############### select_param_equal ##############
    # Description: Fetch table value from columns   #
    #              that are = to some particular    #
    #              value.                           #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - column_name: Name of column to pull from  #
    #                  (String)                     #
    #   - param_name: Name of column to search for  #
    #                 (String)                      #
    #   - param_value: Value of column searched     #
    #                  that should be matched.      # 
    #                  (Type determined by user)    #
    # Returns:                                      #
    #   - Cursor Object containing specified value  #
    # Notes:                                        #
    #   - param_value has no specified type to match#
    #     integers in the table.                    #
    #################################################
    
    def select_param_equal(self, column_name, param_name, param_value):
        if isinstance(param_value, str):
            param_value = self.format_to_string_literal(param_value)

        return self.cursor.execute(f'SELECT {column_name} FROM {self.table_name} WHERE {param_name} = {param_value}')
    
    ###################### insert ###################
    # Description: Insert new table entry           #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - *args: Contains all new values to be      #
    #            inserted into the table.           #
    #            (Argument List)                    #
    # Returns:                                      #
    #   - none                                      #
    # Notes:                                        #
    #   - *args is meant to be dynamic to be used   #
    #     across all tables, not just one. The func #
    #     uses build_values() to create the format  #
    #     needed for the sql query from the args    #
    #################################################

    def insert(self, *args):
        values = self.build_values(*args)
        self.cursor.execute(f'INSERT {self.table_name} VALUES {values}')
        self.cursor.commit()
    
    ###################### update ###################
    # Description: Update table with new value where#
    #              particular condition is met.     #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - param_name: Column where new value will   #
    #                 be updated. (String)          #
    #   - param_value: Value to be updated in       #
    #                  column. (Type determined by  #
    #                  user)                        #
    #   - id_name: Conditional value's column name. #
    #              (String)                         #
    #   - id_value: Conditional value to match for  #
    #               value to be written to proper   #
    #               row. (Type determined by user)  #
    # Returns:                                      #
    #   - none                                      #
    # Notes:                                        #
    #   - Function will handle different types to   #
    #     format the sql string properly.           #
    #################################################

    def update(self, param_name, param_value, id_name, id_value):
        if isinstance(param_value, str):
            param_value = self.format_to_string_literal(param_value)

        if isinstance(id_value, str):
            id_value = self.format_to_string_literal(id_value)
            
        self.cursor.execute(f'UPDATE {self.table_name} SET {param_name} = {param_value} WHERE {id_name} = {id_value}')
        self.cursor.commit()

    ############### serial_is_programmed ############
    # Description: Query DB for boolean value of    #
    #              programming status (Is/Not).     #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - serial: Serial number to query. (String)  #
    # Returns:                                      #
    #   - Boolean. Is the unit programmed or not?   #
    # Notes:                                        #
    # - Should return single value. fetchval() will #
    #   handle parsing the cursor object.           #
    #################################################

    def serial_is_programed(self, serial):
        return self.select_param_equal('UUT_STATUS', 'UUT_SERIAL_NUMBER', serial).fetchval()

    ############# serial_is_final_tested ############
    # Description: Query DB for boolean value of    #
    #              final test (Tested/Not).         #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - serial: Serial number to query. (String)  #
    # Returns:                                      #
    #   - Boolean. Is the unit final tested or not? #
    # Notes:                                        #
    # - Should return single value. fetchval() will #
    #   handle parsing the cursor object.           #
    #################################################

    def serial_is_final_tested(self, serial):
        return self.select_param_equal('FinalTest', 'Serial', serial).fetchval()

    ############ serial_is_spirent_tested ###########
    # Description: Query DB for boolean value of    #
    #              spirent test (Tested/Not).       #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - serial: Serial number to query. (String)  #
    # Returns:                                      #
    #   - Boolean. Is the unit spirent tested or    #
    #     not?                                      #
    # Notes:                                        #
    # - Should return single value. fetchval() will #
    #   handle parsing the cursor object.           #
    #################################################

    def serial_is_spirent_tested(self, serial):
        return self.select_param_equal('SPIRENT_TEST_RESULT', 'UUT_SERIAL_NUMBER', serial).fetchval()

    ############ write_test_result_to_db ############
    # Description: Write True or False for specific #
    #              test (pass/fail) for certain SN. #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - test: Which test result is being written. #
    #           (String)                            #
    #   - serial: Serial number tested. (String)    #
    #   - result: result of the test (Boolean)      #
    # Returns:                                      #
    #   - none                                      #
    # Notes:                                        #
    #   - update() wrapper.                         #
    #################################################

    def write_test_result_to_db(self, test, serial, result):
        self.update(test, result, 'UUT_SERIAL_NUMBER', serial)

    def get_model_from_serial_number(self, serial):
        return self.select_param_equal('PART_NUMBER', 'UUT_SERIAL_NUMBER', serial).fetchval()

    ################## build_values #################
    # Description: Builds insert string dynamically.#
    # Params:                                       #
    #   - self: referance to class object           #
    #   - *args: All of the values to be passed to  #
    #            insert string. (Type specified by  #
    #            user)                              #
    # Returns:                                      #
    #   - String to be appended to insert sql cmd.  #
    # Notes:                                        #
    #   - Format for insert str: (val, val, val...) #
    #################################################

    def build_values(self, *args):
        arg_values = []
        for i in args:
            if isinstance(i, str):
                i = self.format_to_string_literal(i)
            if isinstance(i, int):
                i = str(i)
            arg_values.append(i)
        value_str = "("
        value_str += ', '.join(arg_values)
        value_str += ")"
        return value_str
 
    ############  format_to_string_literal ##########
    # Description: Formats string variable to string#
    #              literals for sql commands.       #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - arg: string argument to be formatted to   #
    #          string literal (String)              #
    # Returns:                                      #
    #   - String to be reformatted.                 #
    # Notes:                                        #
    #   - Values in sql use the single quotes.      #
    #   - Should not be used for column variable    #
    #     names.                                    #
    #################################################
   
    def format_to_string_literal(self, arg):
        literal_arg = "'"
        literal_arg += arg
        literal_arg += "'"
        return literal_arg

    ######### format_to_string_literal_column #######
    # Description: Formats string variable to string#
    #              literals for sql commands.       #
    # Params:                                       #
    #   - self: referance to class object           #
    #   - arg: string argument to be formatted to   #
    #          string literal (String)              #
    # Returns:                                      #
    #   - String to be reformatted.                 #
    # Notes:                                        #
    #   - Variables in sql use the double quotes.   #
    #   - Should not be used for value variable.    #
    #################################################

    def format_to_string_literal_column(self, arg):
        literal_arg = '"'
        literal_arg += arg
        literal_arg += '"'
        return literal_arg

    def close_connection(self):
        self.cursor.close()
        self.connection.close()









# sql = RedlionSQL('Test_Engineering_NTRON', 'SpirentTester')
# sql.insert('Anthony', '17APR24', '123456', '0987654321', 'yk-testeng-l15', '0', '0', '0')
# sql.insert('Alli', '03FEB19', '0000001', '06291997', 'homecpu', '0', '0', '0')
# sql.insert('Eugene', '18APR24', '0000002', '45678989', 'hiscpu', 0, 0, 0)
# sql.update('Programming', 1, 'Serial', '1234567')
# serial_num = '1234567'
# if sql.serial_is_programed(serial_num):
#     print(f'{serial_num} passed programming')
# else:
#     print(f'{serial_num} not programmed')
# if sql.serial_is_final_tested(serial_num):
#     print(f'{serial_num} passed final test')
# else:
#     print(f'{serial_num} not final tested')
# if sql.serial_is_spirent_tested(serial_num):
#     print(f'{serial_num} passed spirent')
# else:
#     print(f'{serial_num} not spirent tested')

# print("Performing Spirent Test")
# print("Spirent test passed")
# sql.write_test_result_to_db('Spirent', serial_num, 1)

# print(f"Spirent Test Result: {sql.serial_is_spirent_tested(serial_num)}")


# ret = sql.select_all()
# for i in ret:
#     print(i)