# Read the input from the file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Define a dictionary that maps each hand shape to its score
hand_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

# Define a dictionary that maps each possible outcome to its score and the correct hand shape
outcome_scores = {
    "AX": (0, "C"),  # Rock vs. loss (Scissors)
    "BX": (0, "A"),  # Paper vs. loss (Rock)
    "CX": (0, "B"),  # Scissors vs. loss (Paper)
    "AY": (3, "A"),  # Rock vs. draw (Rock)
    "BY": (3, "B"),  # Paper vs. draw (Paper)
    "CY": (3, "C"),  # Scissors vs. draw (Scissors)
    "AZ": (6, "B"),  # Rock vs. win (Paper)
    "BZ": (6, "C"),  # Paper vs. win (Scissors)
    "CZ": (6, "A"),  # Scissors vs. win (Rock)
}

# Initialize the total score to 0
total_score = 0

# Loop through each line in the input
for line in lines:
    # Split the line into two tokens
    opponent_hand, your_hand = line.split()
    
    # Get the score and correct hand shape for the outcome
    outcome_score, correct_hand = outcome_scores[opponent_hand + your_hand]
    
    # Get the score for the hand shape
    your_hand_score = hand_scores[correct_hand]
    
    # Add the score for the round to the total score
    total_score += your_hand_score + outcome_score

# Print the total score
print(total_score)
