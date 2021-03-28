#PyPoll.py

# Import the csv and os modules
import csv
import os

# Set path for Resources folder where the election results file is kept
    # https://help.pythonanywhere.com/pages/NoSuchFileOrDirectory/
    # https://www.youtube.com/watch?v=TRq7JbgKN2s
Resource_folder = os.path.join(os.path.dirname(__file__),"Resources") 

# Assign a variable for the file to load and the path
file_to_load = os.path.join(Resource_folder,"election_results.csv")

# Open the election results and read the file.
with open(file_to_load,"r") as election_data:
     
      # Print the file object
      print(election_data)

      # To do:Read and analyze the data here.
      file_reader = csv.reader(election_data)

     # Print the Header row
      headers = next(file_reader)
      print(headers)

     #  # Print each row in the CSV file.
     #  for row in file_reader:
     #      print(row)
     
     



# Set path for Analysis folder where the election analysis file isresults are kept
Analysis_folder = os.path.join(os.path.dirname(__file__),"Analysis")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join(Analysis_folder, "election_analysis.txt")

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
     # Write some data to the file
     txt_file.write("Counties in the Election\n")
     txt_file.write("-------------------------\n")
     txt_file.write("Arapahoe\nDenver\nJefferson")




# # close the file
# with close(file_to_load)
# # 1. The total number of votes cast

# # 2. A complete list of candidates who received votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote
