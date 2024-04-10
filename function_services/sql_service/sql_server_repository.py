from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import json
import asyncio

class SQLConnection:

    _engine = None

    def __init__(self, conn):
        self._connection_string = conn
        self._engine = create_engine(self._connection_string, echo=True)        

    def select_scalar(self, query = 'SELECT @@version'):
        
        with self._engine.connect() as connection:
            result = connection.execute(text(query)) 
            data = result.scalar()
        return data
    
    def select_scalar_option2(self, query = 'SELECT @@version'):
        connection = self._engine.connect()
        
        result = connection.execute(text(query)) #returns a CursorResult object
        row = result.fetchone()

        if row is not None:
            data = row[0]

        connection.close()

        return data
    
    def select_table(self):

        Session = sessionmaker(bind=self._engine)
        session = Session()

        result = session.execute(text("SELECT * FROM [Learning_Database].[dbo].[Countries]"))

        rows = result.fetchall()
        # Get column names from the result set
        column_names = result.keys()
        # Create a list to store dictionaries for each row
        result_dicts = []
        
        for row in rows:
            
            row_dict = dict(zip(column_names, row))
            result_dicts.append(row_dict)

        session.close()

        json_data = json.dumps(result_dicts)

        return json_data
