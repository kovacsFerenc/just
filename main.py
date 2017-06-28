import data_manager


def main():
    conn_data = data_manager.get_connection_data('postgres')
    with data_manager.establish_connection(connection_data=conn_data) as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT 'Hello Codecool'")
            result = cursor.fetchall()
            print(result)

if __name__ == '__main__':
    main()
