# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules
import csv
import mysql.connector as con

# Functions
def InsertDataTrain():
    """
    InsertDataTrain() -> Inserts all the Train details in the train_info Table
    Parameters -> None
    """
    try:
        # Establishing connection to the database
        mn = con.connect(host="localhost",
                         user="root",
                         password="admin@123",
                         database="railway")
        cur = mn.cursor()
        
        # Replace the path below with the absolute path of the file on your computer
        csv_file_path = "D:/1/Bhanu/Tharun/Railway-Management/Assets/Train_details.csv"  # Use forward slashes for paths
        
        inserted_rows = 0
        total_rows = 0

        try:
            with open(csv_file_path) as csv_data:
                csv_reader = csv.reader(csv_data, delimiter=",")
                
                # Reading and inserting data row by row
                for row in csv_reader:
                    cur.execute(
                        'INSERT INTO train_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)
                    inserted_rows += 1
                    total_rows += 1
            
            # Committing the Changes
            mn.commit()  
            print("Data inserted successfully!")
        
        except FileNotFoundError:
            print("CSV file not found. Please check the file path and try again.")
            print("Current path:", csv_file_path)
        except Exception as e:
            print("An error occurred while inserting data:", str(e))
        
        # Verifying row count
        cur.execute("SELECT COUNT(*) FROM train_info")
        result = cur.fetchone()
        db_row_count = result[0] if result else 0
        
        if db_row_count == total_rows:
            print(f"All {total_rows} rows from the CSV file have been successfully inserted into the database.")
        else:
            print(f"Discrepancy found: {total_rows} rows in CSV file, but {db_row_count} rows in database.")
    
    except con.Error as err:
        print("Error connecting to MySQL:", str(err))
    
    finally:
        # Ensuring the connection is closed
        if 'mn' in locals() and mn.is_connected():
            cur.close()
            mn.close()
            print("MySQL connection is closed")

# You can call the function like this:
# InsertDataTrain()
InsertDataTrain()
