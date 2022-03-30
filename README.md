# userbase-data
Coding challenge for a software engineer job post. 

This coding challenge was written in Python programming language. When you clone the repository to your local machine, make sure all the required libraries (ArgumentParser, csv, requests) to run the app are installed.

## Run code on the terminal

In the terminal, insert this command to initiate the command line instructions (make sure you don't include the quotation marks): 

#### "python3 main.py -h"

This command will display the following instructions on the terminal:


    usage: main.py [-h] [-r] [-p]*

    A command line tool for interacting with our API*

    optional arguments:

    -h, --help     show this help message and exit
   
    -r, --read     Sends a GET request to the product API.
   
    -p, --preview  Shows us a preview of the data.

Type **python3 main.py -r** if you want to read and or, **python3 main.py -rp** to read and preview the data on the terminal.

### There's an added functionality in the application that allows the user to save the data in a csv file format:

    **python3 main.py -s**

*Please note the csv file name will be saved as userbase.csv
