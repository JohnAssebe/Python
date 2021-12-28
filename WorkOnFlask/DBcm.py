import mysql.connector
class ConnectionError(Exception):
    pass
class CredentialError(Exception):
    pass
class SQLException(Exception):
    pass

class UseDatabase:
    def __init__(self,config:dict)->None:
        self.configuration=config
    def __enter__(self)->'cursor':
        try:
            self.conn=mysql.connector.connect(**self.configuration)
            self.cursor=self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialError(err)
    
    def __exit__(self,exc_type,exc_value,exc_trace)->None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLException(exc_value) 
        elif exc_type:
            exc_type(exc_value)
        
        
