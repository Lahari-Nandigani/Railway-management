# Railway-management

Step 1: 
first of all you need to install mysql workbench so install mysql work bench goto 
 # https://dev.mysql.com/downloads/workbench/
 here select your windows version and according to install it 
 and setup your username and password as 
 # username: root
 # passwrod: admin@123

 for this you want to know how to run and use mysql workbench 

 Step 2: 
 After installing and setup mysql workbench you need to create a schema 
 # name of the schema : railway 
 Its like database soo using railway

 Step 3: 
 use command prompt (cmd) for the folder where you want to store the files so 
 # giclone https://github.com/Lahari-Nandigani/Railway-management.git

 Step 4: 
 After cloning you will get core folder navigate to core folder 
 After navigating to core folder now  you have to find the file Inserdata.py
so now edit the InsertData.py file 
There you will see csv_file_path="something like path of the file"
so you have to replace that path where the dataset has been located in you system 
like you will find Assets folder while cloning and in that Assets folder you will find the data set 
so now copy the path of the file and paste 
# csv_file_path="Paste the path of the file"

Step 5: 
After copying that file you have to run
 # python Checks.py

Step 6: 
After running that file you have to run 
# python InsertData.py

Step 7 : 
After completion of running above two files now go to main file 
it will be named as Main.py 
so run it 
# python Main.py

Now you have to use appropriate names codes to insert the data and run the data you will get with out any errors 
At maximum you will find the error at creating the table and utilizing them so check several times that username, password , and database name are correct or not 
And is the connection established or not 
