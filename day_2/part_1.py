# Read the input from the file
with open("input.txt", "r") as f:
    lines = f.readlines()

# Define a dictionary that maps each hand shape to its score
hand_scores = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

# Define a dictionary that maps each possible outcome to its score
outcome_scores = {
    "AX": 3,  # Rock vs. Rock (draw)
    "BX": 0,  # Paper vs. Rock (loss)
    "CX": 6,  # Scissors vs. Rock (win)
    "AY": 6,  # Rock vs. Paper (win)
    "BY": 3,  # Paper vs. Paper (draw)
    "CY": 0,  # Scissors vs. Paper (loss)
    "AZ": 0,  # Rock vs. Scissors (loss)
    "BZ": 6,  # Paper vs. Scissors (win)
    "CZ": 3,  # Scissors vs. Scissors (draw)
}

# Initialize the total score to 0
total_score = 0

# Loop through each line in the input
for line in lines:
    # Split the line into two tokens
    opponent_hand, your_hand = line.split()
    
    # Get the score for the hand shapes
    opponent_hand_score = hand_scores[opponent_hand]
    your_hand_score = hand_scores[your_hand]
    
    # Get the score for the outcome
    outcome_score = outcome_scores[opponent_hand + your_hand]
    
    # Add the score for the round to the total score
    total_score += your_hand_score + outcome_score

# Print the total score
print(total_score)
