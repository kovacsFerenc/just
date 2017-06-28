import data_manager
import init_db


def main():
    init_db.init_db()
    init_db.create_schema()

if __name__ == '__main__':
    main()
