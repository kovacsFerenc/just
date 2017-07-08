from data_manager import *
import os


def init_db():
    init_conn = get_connection_data('postgres')
    db_name = os.environ.get('MY_PSQL_DBNAME')

    with establish_connection(connection_data=init_conn) as conn:
        with conn.cursor() as cursor:
            try:
                drop_statement = "DROP DATABASE IF EXISTS {};".format(db_name)
                create_statement = "CREATE DATABASE {};".format(db_name)
                cursor.execute(drop_statement)
                cursor.execute(create_statement)
                print("Database created.")
            except Exception as ex:
                print("Database creation failed")
                print(ex.args)


def create_schema():
    creation_script_file = 'db_schema/01_create_schema.sql'
    execute_script_file(creation_script_file)


def insert_data():
    insert_data_script = 'db_schema/02_insert_data.sql'
    execute_script_file(insert_data_script)


def main():
    init_db()
    create_schema()
    insert_data()

if __name__ == '__main__':
    main()
