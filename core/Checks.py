# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules
import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import core.InsertData as Insert

# MySQL credentials
YOUR_USERNAME = "root"
YOUR_PASSWORD = "admin@123"

# Functions
def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user=YOUR_USERNAME, database="railway", password=YOUR_PASSWORD)
    cur = db.cursor()
    result = None

    try:
        cur.execute("USE railway;")
    except ProgrammingError:
        print("Database does not exist!")
        result = False
    else:
        result = True

    if result:
        print("Database exists!")
    """else:
        print("Creating database with the required tables...")
        print("Please be patient!")
        cur.execute("CREATE DATABASE railway;")
        cur.execute("USE railway;")
        CreateTables()
        print("Database and tables created!")"""

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = con.connect(host="localhost", user=YOUR_USERNAME, database="railway", password=YOUR_PASSWORD)
    cur = db.cursor()

    cur.execute(
        """
        CREATE TABLE train_info (
            Train_No VARCHAR(10) NOT NULL,
            Station_Code VARCHAR(20) NOT NULL,
            Station_Name VARCHAR(30) NOT NULL,
            Arrival_Time VARCHAR(20) NOT NULL,
            Departure_Time VARCHAR(20) NOT NULL,
            Distance VARCHAR(10) NOT NULL,
            Source_Station_Code VARCHAR(20) NOT NULL,
            Source_Station_Name VARCHAR(70) NOT NULL,
            Destination_Station_Code VARCHAR(20) NOT NULL,
            Destination_Station_Name VARCHAR(60) NOT NULL
        );
        """
    )

    cur.execute(
        """
        CREATE TABLE bookings (
            Train_No INT NOT NULL,
            Passenger_Name VARCHAR(30) NOT NULL,
            Mobile_No VARCHAR(10) NOT NULL,
            Passenger_Adhaar VARCHAR(12) NOT NULL,
            Date_Of_Booking VARCHAR(20) NOT NULL,
            Booking_ID INT NOT NULL,
            Class VARCHAR(20) NOT NULL
        );
        """
    )

    Insert.InsertDataTrain()

    cur.close()
    db.close()


def CheckConnection():
    """
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the connection to the MySQL Server...")
        connection = con.connect(host='localhost', database='', user=YOUR_USERNAME, password=YOUR_PASSWORD)
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version", db_Info)

    except Error:
        print("Error connecting to MySQL Server. Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True

# Run the connection check
if CheckConnection():
    # Run the database check
    CheckDatabase()
