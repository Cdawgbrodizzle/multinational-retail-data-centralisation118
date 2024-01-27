import yaml, psycopg2, pandas as pd
from sqlalchemy import create_engine, text, inspect

class DatabaseConnector:
    
    def read_db_creds():
        with open("db_creds.yaml", "r") as stream:
            data_loaded = yaml.safe_load(stream)
            return data_loaded
    reader = read_db_creds()

    def init_db_engine(reader):
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = reader["RDS_HOST"]
        USER = reader['RDS_USER']
        PASSWORD = reader['RDS_PASSWORD']
        DATABASE = reader['RDS_DATABASE']
        PORT = 5432
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        return engine
    db_engine = init_db_engine(reader)
    print(db_engine)

    """def list_db_tables(db_engine):
        inspector = inspect(db_engine)
        inspector.get_table_names()
        with db_engine.execution_options(isolation_level='AUTOCOMMIT').connect() as connection:
            result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
            for row in result:
                print(row)
    list_table = list_db_tables(db_engine)

    def read_user_data(db_engine):
        with db_engine.execution_options(isolation_level='AUTOCOMMIT').connect() as connection:
            result = pd.read_sql_table('orders_table', db_engine)
            #result = pd.DataFrame("orders_table")
            isit = result.head(10)
            print(isit)
            return isit
    rud = read_user_data(db_engine)"""

    #def clean_user_data(rud):
    #drop_col = rud.dropna(inplace=True, axis=1, how="all")
    #print(drop_col)
    #clean_user_data

    #init.execution_options(isolation_level='AUTOCOMMIT').connect()
#test = DatabaseConnector()
#print(test)