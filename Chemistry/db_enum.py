import sqlite3

def list_databases_and_tables(db_file):
    """
    Lists the databases (schemas) and tables in a given SQLite .db file.
    """
    try:
        # Connect to the SQLite database
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # List all tables in the database
        print(f"Tables in the database '{db_file}':\n")
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            for table in tables:
                print(f"Table: {table[0]}")
                
                # Show the schema for each table
                cursor.execute(f"PRAGMA table_info({table[0]});")
                columns = cursor.fetchall()
                print("Columns:")
                for column in columns:
                    print(f" - {column[1]} (type: {column[2]})")
                print()
        else:
            print("No tables found in the database.")

    except sqlite3.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the connection
        if connection:
            connection.close()

# Replace 'example.db' with the path to your SQLite .db file
db_file = "data.db"
list_databases_and_tables(db_file)

