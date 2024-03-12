# DFP stock analysis

### 1. Installing Packages.
 
The only additional package needing to be installed to run our project code is Pandas-DateReader
 
To install this package, in the console of a Spyder python prompt type:
 
**conda install -c anaconda pandas-datareader**
 
Once pandas_datereader has been installed, the script is ready to be fun.

To run the JS file example, you will need to: **npm install axios cheerio papaparse plotly.js**
 
### 2. Running the Program.
 
Our Python program imports a few packages and then defines the main program function. The program prompts a user for a four-character “ticker” used to choose a stock. It then prompts the user for a start date and an end date to display the data. Both dates must be in the format “YYYY-MM-DD” to have the program run properly.
 
### 3. Exiting the Program.
 
Suppose the user inputs an invalid format type for the input. In that case, the program will continue to prompt the user to try again, displaying the error message “Invalid Inputs, Please Try Again!” After the user successfully inputs valid formats for the stock and dates, the program will display the correct plots and exit. To display a new stock, the user must re-run the program.
