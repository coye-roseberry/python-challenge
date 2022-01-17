
#Import 
import os
import csv


#Declare
election_data = os.path.join("Resources","election_data.csv")

vote_list = []
candidate_list = []
vote_dict1 = {}
vote_dict2= {}
vote_check = []





#Read in file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
#Calculate total Number of votes

    #add votes to List
    for vote in csvreader:
        vote_list.append(vote[2])
    #set variable to length of voterId list
    total_votes = len(vote_list)


#Populate Candidate list
    for unique_candidate in vote_list:
        if unique_candidate not in candidate_list:
            candidate_list.append(unique_candidate)
    
    

    candidateCounter = 1
    for candidate in candidate_list:
        info_list = []
        info_dict = {}
        candidate_name = candidate
        info_list.append(candidate_name)
        info_dict["name"] = candidate_name
        #Count votes by candidate in vote list
        candidate_vote = vote_list.count(candidate)
        info_list.append(candidate_vote)
        info_dict["votes"] = candidate_vote
        #Calculate percentage of total votes
        candidate_percentage = round((candidate_vote/total_votes)*100)
        info_list.append(candidate_percentage)
        info_dict["percentage"] = candidate_percentage

        vote_dict1[candidateCounter] = info_list
        candidateCounter = candidateCounter + 1
        vote_dict2[candidate] = info_dict





#Determine Winner based on popular vote
### Following approach works but is less precise since grabbing index from list and not value based on key (if list ever got scrambled)
    ###vote_holder1= 0


    #for key, value in vote_dict1.items():
    #    if value [1] > vote_holder1:
    #        vote_holder1 = value[1]
     #       winner = value[0]

    #print(winner)








### Following method pulls by dict key
    vote_holder2 = 0
    for v in vote_dict2.values():
        numOfVotes=v.get('votes')

        if numOfVotes > vote_holder2:
            vote_holder2 = numOfVotes
            electionWinner = v.get('name')
    print(vote_holder2)
    print(electionWinner)





#Save Results to variable
printOutList = [

"Election Results",
"-------------------------",
f"Total Votes: {total_votes}",
"-------------------------",
f'{vote_dict1[1][0]}: {vote_dict1[1][2]:.3f}% ({vote_dict1[1][1]})',
f'{vote_dict1[2][0]}: {vote_dict1[2][2]:.3f}% ({vote_dict1[2][1]})',
f'{vote_dict1[3][0]}: {vote_dict1[3][2]:.3f}% ({vote_dict1[3][1]})',
f"{vote_dict1[4][0]}: {vote_dict1[4][2]:.3f}% ({vote_dict1[4][1]})",
'-------------------------',
f'Winner: {electionWinner}',
'-------------------------'
]
# Write to file
with open('PyPoll_output.txt', 'w') as electionOuput:
    for line in printOutList:
        electionOuput.write(line)
        electionOuput.write('\n')
    #print(electionOuput.read())
#Print Results
with open('PyPoll_output.txt', 'r') as electionOuput:
    print(electionOuput.read())



