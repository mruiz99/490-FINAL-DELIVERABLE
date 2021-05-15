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
The final output will create a folder titled _Deliverables_.   
Within it, depending on how many times you ran the program and what data you grabbed, you will find a folder for Prince George's County that contains within it a folder named after the timeframe.  

In this example you would see something like:  
`Deliverables/PG/PGJanuaryFebruary19`  
Inside `PGJanuaryFebruary19` you will find varying the deliverables from our analysis such as Boarding and Alighting Trends or Route Performance analysis 


**In order to analyze more than one timeframe, year, or county, you must run the program again.**    



## Background   

When the United States declared COVID-19 a pandemic and then followed with a state of emergency, there was a mandate enacted by some states to either significantly reduce capacity or shut down “non-essential” businesses and services. Public transit services can in no way shut down because the public depends on these services to get to work, to commute around the counties, and to go home.  Montgomery County and Prince George’s County public bus transports Ride-On and The Bus had to maintain operations but now also had to adjust the way they did pickups considering the new dangers that the virus posed to the public.  Packed buses full of people were no longer a viable option and in response to the adverse conditions, the counties implemented service enhancements with the goal of increasing ridership levels.   

Our task was to conduct an analysis on the performances of the bus routes and their trends in ridership levels ranging from 2019 to the beginning of 2021. The year 2019 would be used as a baseline to compare to the rest of the data. We would then analyze the performance of the bus routes after service enhancements.  Our client is the Washington Suburban Transit Commission.  Our initial point of contact for this project is the director of the Washington Area Transit Office, Pat Pscherer.  Our initial point of contact for Prince George’s County is Chief of Transit Planning for PG County DPW&T Anthony Foster and his Planner Erick Maravilla.  Erick gave us directions and access to the Nextbus database with all the data for Prince George’s County. Terry Herron, manager for Transit Service IT for MCDOT was our point of contact for Montgomery County who gathered and deciphered how to properly analyze the data.


## Deliverables

1. Analysis of Boarding and Alighting Trends   
    1. Visuals in the forms of bar graphs
    2. Raw Data as CSV files. The files contain every listed segment for every route

2. Analysis of All Routes Performance
    1. Visuals in the forms of pie charts showcasing the results of our route performance analysis 
    2. Raw Data as CSV files. The files contain every listed segment for every route

3. Analysis of Routes That Responded Well to Service Enhancements
    1. Visuals in the forms of bar graphs
    2. Raw Data as CSV files. The files contain every listed segment for every route
