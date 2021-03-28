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

# Set the count accumulater to zero
total_votes = 0

# Print the candidate name from each row
candidate_options = []
# Candidate dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load,"r") as election_data:
     
     # Print the file object
     # print(election_data)

     # To do:Read and analyze the data here.
     file_reader = csv.reader(election_data)

     # Print the Header row
     headers = next(file_reader)

     # Print each row in the CSV file.
     for row in file_reader:
          # Add up the total of votes
          total_votes += 1
          # Print the candidate name from each row
          candidate_name = row[2]
         
          # Record the candidate name in the list
          if candidate_name not in candidate_options:
               # Add it to the list of candidates
               candidate_options.append(candidate_name)
               # Begin tracking that candidate's vote count
               candidate_votes[candidate_name] = 0

          # Add to the candidate's vote count
          candidate_votes[candidate_name] += 1

     # Determine the percentage of votes for each candidate by looping through the count
     # Iterate through the candidate list
     for candidate_name in candidate_votes:
          # Retrieve vote vount of a candidate
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes
          vote_percentage = float(votes) / float(total_votes) * 100

          # to do: print out the results
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

          # Determine winning vote count and candidate
          # Determine if the vote is greater than the winning count
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percentage = vote_percentage
               winning_count = votes
               winning_percentage = vote_percentage
               # And, set the winning_candidate equal to the candidate's candidate_name
               winning_candidate = candidate_name

     # Print out the winning candidate, count and % to the terminal     
     winning_candidate_summary = (
          f"------------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"------------------------------\n")
     print(winning_candidate_summary)

# # Print the candidate list
# print(candidate_options)

# # Print the candidate vote dictionary
# print(candidate_votes)

# # Print the total votes
# print(total_votes)          
     



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
