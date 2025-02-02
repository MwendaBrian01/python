# This is a simple voting system

# Welcome message
print("WELCOME TO THE IEBC VOTING SYSTEM\n")

# Registered Voters
registered_voters = {101, 102, 103, 104, 105, 106, 107}

# Candidates List
candidates = {
    "1. Raila Odinga": 0,
    "2. Babu Owino": 0,
    "3. Matiang'i": 0,
    "4. Kasongo": 0
}

# Ask for Voter ID
voter_id = int(input("Enter your Voter ID: "))

# Check if Voter ID is registered
if voter_id not in registered_voters:
    print("Invalid Voter ID! Access Denied.")
else:
    print("\nCandidates:")
    for candidate in candidates:
        print(candidate)

    # Ask for the user's vote
    vote = input("\nEnter the number of the candidate you want to vote for: ").strip()

    # Check and count the vote
    if vote == "1":
        candidates["1. Raila Odinga"] += 1
        print("You have successfully voted for Raila Odinga.")
    elif vote == "2":
        candidates["2. Babu Owino"] += 1
        print("You have successfully voted for Babu Owino.")
    elif vote == "3":
        candidates["3. Matiang'i"] += 1
        print("You have successfully voted for Matiang'i.")
    elif vote == "4":
        candidates["4. Kasongo"] += 1
        print("You have successfully voted for Kasongo.")
    else:
        print("Invalid choice. Vote not counted.")

# Display Final Results
print("\n### Voting Results ###")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes} votes")

# Determine the winner
winner = max(candidates, key=candidates.get)
print(f"\nWinner: {winner} ")
