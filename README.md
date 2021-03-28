# Election Analysis for the Colorado Board of Elections

## Overview
   This project is to satisfy the requirements for the third challenge in the Data Analysis Bootcamp. For this, the task is to analyze/audit the results of a Colorado election. Tom and Seth are helping by reviewing the python code being written to programmatically review the data quickly and provide results as to the number of votes cast, the quantity per county, total votes per candidate, percentage of county votes, and the overall winner; among other tallied items to be shown here.
   Two outputs are shown below, one from the terminal and the other that is located in the txt report file. Spacing for each is setup differently to as requested by the team. Results of the analysis are the same.
![Terminal Printout](https://github.com/summerstime/election-Analysis/blob/main/Resources/screenshot_terminal_output.png) 
![Report Txt File](https://github.com/summerstime/election-Analysis/blob/main/Resources/screenshot_txt_output_file.png) 

## Election Audit Results
   Python code was written in Visual Studio. Utilization of for-loops and if-statements helped cycle through the data contained in a csv file, named Election_results.csv. Here is a sample of that code.
   ![Sample of Code](https://github.com/summerstime/election-Analysis/blob/main/Resources/screenshot_of_csv_reader.png)
### How many votes were cast in this congressional election?
   -A total of 369,711 votes were cast in this election.
### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   -Jefferson county had 38,855 votes which is 10.5% of the total votes.
   -Denver county had 306,055 votes which is 82.8% of the total votes.
   -Arapahoe county had 24,801 votes which is 6.7% of the total votes.
### Which county had the largest number of votes?
   -Denver county overwhemingly had the greatest number of votes with 82.8% of the total vote count.
### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   -Charles Casper Stockham had 85,213 votes which is 23.0% of the total votes.
   -Diana DeGette had 272,892 votes which is 73.8% of the total votes.
   -Raymon Anthony Doane had 11,606 votes which is 3.1% of the total votes.
### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   -Diana DeGette overwhemingly had the greatest number of votes with 73.8% of the total vote count.

## Summary
The results of this analysis were quickly obtained through the use of Python and Visual Studio. This basic code can be adjusted and made useful for other elections. There is a basic format the csv file needs to maintain or adjust the code to fit the indexing of each row in the new file. A user input could be utilized to request which column the county, candidate, etc. are located. This would make the code more adaptable without changing the code for each election analysis.

Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

Deliverable 3 Requirements
Structure, Organization, and Formatting (6 points)
The written analysis has the following structure, organization, and formatting:

There is a title, and there are multiple sections. (2 pt)

Each section has a heading. (2 pt)

Links to images are working, and code is formatted and displayed correctly. (2 pt)

Analysis (14 points)
The written analysis has the following:

Overview of Election Audit

The purpose of this election analysis audit is well defined. (3 pt)
Election Audit Results

There is a bulleted list where each election outcome is addressed. (7 pt)
Election Audit Summary

There is a statement to the election commission that explores how this script can be used for any election, with two examples for modifying the script. (4 pt)
