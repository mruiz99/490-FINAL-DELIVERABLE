# Washington Suburban Transit Commission Ridership Analysis 2019-2021

## How To Use

**_Required Packages_**  
Upon cloning of the repo these will be your **requirements** to run the program:

`import pandas as pd`  
`import numpy as np`  
`import datetime`  
`import matplotlib.pyplot as plt`  
`import seaborn as sns`  
`import os`  

For this to run you must make sure you have the module `seaborn` installed through `pip install seaborn.`

**_Running the Program_**   
In the terminal type `python3 FinalProject.py`  
This will prompt you to enter the specifc county, year, and timeframe you are interested in analyzing.   
  
_Example_  
Terminal Input:  
`python3 FinalProject.py`  
Terminal Output:  
`Welcome, please choose a county:` 
`(1)Prince George's County` 
`(2)Montgomery County`

Terminal Input:  
`1`
Terminal Output:  
`What year would you like to take a look at? (2019 or 2020)`

Terminal Input:
`2019`
Terminal Output:  
`Great. What timeframe are you interested in?` 
`(1)January to Febuary`  
`(2)March to May`  
`(3)August to January`  

Terminal Input:
`1` 
Output: 
The final output will create a folder titled _Deliverables_. Within it, depending on how many times you ran the program and what data you grabbed, you will find a folder for Prince George's County that contains within it a folder named after the timeframe.  
In this example you would see something like:  
`Deliverables/PG/PGJanuaryFebruary19` 
Inside `PGJanuaryFebruary19` you will find varying analyzations such as Boarding and Alighting Trends or Route Performance Analysis


**In order to analyze more than one timeframe, year, or county, you must run the program again.**




