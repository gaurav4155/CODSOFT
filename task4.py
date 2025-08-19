import random

user_score = 0
computer_score = 0

print("🎮 Welcome to Rock-Paper-Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play.\n")

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice. Please try again.\n")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("✅ You win this round!")
        user_score += 1
    else:
        print("❌ You lose this round!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n🏆 Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing! 🎉")
        break
