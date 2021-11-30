# Mini-Bank-System 
__A simple program that__:
* Tells user to install mysql server. And creates a database and defines the table structure in the database.
	> Dbinit.py
* Lets the user to create a simple bank account.
	* Generates a unique account number and creates a table in the database for storing its transaction details. 
		* A kinda limitation is that names of users should be different as same account number gets generated for users having similar names.
	* Provides functions like 
		* **Check Balance**
		* **Add Money**
		* **Withdraw Money**
		* **View Transaction Details**
		* **Transfer money to another account**
		* **Reset Password**
	> MiniBankSystem.py
##### Dbinit.py:
1. *Tells user to install mysql server and setup the user account.*
2. *Asks user if mysql server is installed or not.*
3. *Determines whether user has installed mysql server or not - based on user input.*
4. *If installed, it asks for username and password to connect to the server.*
5. *On connecting successfully, it creates a database and defines the table structure in the database.*
6. *If this program doesn't generate any error message, **MiniBankSystem.py** is ready to use.*
##### MiniBankSystem.py
1. *Asks for username and password to connect to the server to get access to the database.*
2. *On connecting successfully, it asks user for creating a new account or singing in if already created.*
	* On creating a new account - it generates a unique account number and creates a table in the database for storing its transaction details.
	* On signing in - if Email and Password matches any account in the database - the above mentioned functions are provided to user.
* > A kinda **easter egg**: If you type "iamaqib" in email while signing in, you can see all the user details in the database.
> Note: If you use this for the first time - firstly run dbinit.py and on successful execution you're ready to run MiniBankSystem.py
 
