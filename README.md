# Election Analysis for the Colorado Board of Elections

## Overview
   This project is to satisfy the requirements for the third challenge in the Data Analysis Bootcamp. For this, the task is to analyze/audit the results of a Colorado election. Tom and Seth, who are the requesters of this analysis, are helping by reviewing the python code being written to programmatically review the data quickly and provide results as to the number of votes cast, the quantity per county, total votes per candidate, percentage of county votes, and the overall winner; among other tallied items to be shown here.
   Two outputs are shown below, one from the terminal and the other that is located in the txt report file, Elections Analysis.txt. Spacing for each is setup differently to match the request by the team. Results of the analysis are the same.

#### Terminal Printout of the Results
![Terminal Printout](https://github.com/summerstime/Election_Analysis/blob/main/Resources/Screenshot_Terminal_Output.png) 

#### Txt Report Printout of the Results
![Report Txt File](https://github.com/summerstime/Election_Analysis/blob/main/Resources/Screenshot_Txt_Output_File.png) 

## Election Audit Results
   Python code was written in Visual Studio. Utilization of for-loops and if-statements helped cycle through the data contained in a csv file, named Election_results.csv. Here is a sample showing the code used to read the csv file.
   
#### Sample of Code (CSV Reader)
![Sample of Code](https://github.com/summerstime/Election_Analysis/blob/main/Resources/Screenshot_of_CSV_Reader.png)

### Total Votes Received
   * A total of 369,711 votes were cast in this election.
### County Totals Breakdown
   * Jefferson county had 38,855 votes which is 10.5% of the total votes.
   * Denver county had 306,055 votes which is 82.8% of the total votes.
   * Arapahoe county had 24,801 votes which is 6.7% of the total votes.
### County with largest Turnout
   * Denver county overwhelmingly had the greatest number of votes with 82.8% of the total vote count.
### Candidate Totals Breakdown
   * Charles Casper Stockham had 85,213 votes which is 23.0% of the total votes.
   * Diana DeGette had 272,892 votes which is 73.8% of the total votes.
   * Raymon Anthony Doane had 11,606 votes which is 3.1% of the total votes.
### **Winning Candidate**
   * **Diana DeGette overwhelmingly had the greatest number of votes with 73.8% of the total vote count.**

## Summary of the Analysis Process
The results of this analysis were quickly obtained through the use of Python and Visual Studio. This basic code can be adjusted and made useful for other elections. There is a basic format the csv file needs to maintain or adjust the code to fit the indexing of each row in the new layout of the election csv file. One modification of the code could be to add user input questions to request which column the county, candidate, etc. are located. This would make the code more adaptable without changing the code for each election analysis. Another modification could be more user input for different aspects for the analysis, such as state, proposal/referendum type, etc. Making the code adjustable to the need of the analysis.

#### Challenges Experienced During Analysis
The reading of the csv file was difficult since the suggested code was not able to find the necessary file. After many attempts to get the code to read the file, Google was utilized to find other options. A combination of websites offered a way to read the csv file, so the processing of the data continued. 
The second challenge was getting the different displays to show as requested. The Visual Studio terminal treated the code, such as a new line, differently than the txt_file.write function. Adding \n at the right locations, took some time; but all was figured out.  
