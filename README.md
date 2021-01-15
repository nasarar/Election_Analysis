# Election_Analysis

## Project Overview
The Colorado Board of Elections requires an election audit based on the election results data that was provided. A list of deliverables is highlighted below as per the commission requirements. 
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received the vote.
3. Calculate the total number of votes each candidate won.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the voter turnout for each county.
7. Calculate the percentage of voters from each county from the total amount.
8. Determine the county with the highest turnout. 

## Resources
- Data Source: elections_results.csv
- Software: Python 3.6.7, Visual Studio Code 1.52.1

## Results
The analysis of the election show that:
- There were 369,711 votes cast on the election.

- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

- The winner of the election was:
 - Diana DeGette with 73.8% of total voters. 

- The counties involved in the elections were:
 - Jefferson county with 38, 855 voters and 10.5% of the total voters.
 - Denver county with 306, 055 voters and 82.8% of the total voters.
 - Arapahoe county with 24, 801 voters and 6.7% of the total voters.

- The county that had the largest turnout:
 - Denver with 82.8% total participants

## Challenge Summary
The script written for the intended purposes to calculate the data given the Colorado election may also be used for any other election. It is written in such a way that it will adapt with variations to the number of candidates and/or counties involved. Below is an example as to how to use the existing script for other elections.
###### Sample Changes
Any new data can be used in the existing script as long as it is given the right path. For example, if another election is done and the file "election_results_california.csv" is used under the same "Resources" folder, then the following script should be edited.

```
# Create a filename variable to a direct or indirect path to the file
file_to_load = os.path.join('Resources', 'election_results_california.csv')
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')
```

Furthermore, if the election board does not wish to see the breakdown of the county results then use the script below. 
```
# Add our dependencies.
import csv
import os

# Create a filename variable to a direct or indirect path to the file
file_to_load = os.path.join('Resources', 'election_results.csv')
#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #  Checks that the county does not match any existing county in the county list.
        if county_name not in county_options:

            # Adds the existing county to the list of counties.
            county_options.append(county_name)

            # Tracks the county's vote count.
            county_votes[county_name] = 0    

        # Adds a vote to that county's vote count.
        county_votes[county_name] += 1


# Saves the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # Saves the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determines winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Prints the winning candidate (to terminal)
    winning_candidate_summary = (
          f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
    
    ```
