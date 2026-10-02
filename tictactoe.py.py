

def display_board(board):
    """Display the current game board."""

    print("\n")
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")
    print("\n")


def display_positions():
    """Show the position numbers before the game starts."""

    print("\nBoard positions:\n")

    print("     |     |")
    print("  1  |  2  |  3")
    print("_____|_____|_____")
    print("     |     |")
    print("  4  |  5  |  6")
    print("_____|_____|_____")
    print("     |     |")
    print("  7  |  8  |  9")
    print("     |     |")
    print()


def check_winner(board, player):
    """Check whether the given player has won."""

    winning_combinations = [
        (0, 1, 2),  # Top row
        (3, 4, 5),  # Middle row
        (6, 7, 8),  # Bottom row
        (0, 3, 6),  # Left column
        (1, 4, 7),  # Middle column
        (2, 5, 8),  # Right column
        (0, 4, 8),  # Diagonal
        (2, 4, 6)   # Diagonal
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


def check_draw(board):
    """Check whether the board is completely filled."""

    return all(position in ["X", "O"] for position in board)


def get_player_move(board, player):
    """Get and validate the player's move."""

    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): "))

            if move < 1 or move > 9:
                print("❌ Please enter a number between 1 and 9.")
                continue

            index = move - 1

            if board[index] in ["X", "O"]:
                print("❌ That position is already occupied. Choose another.")
                continue

            return index

        except ValueError:
            print("❌ Invalid input. Please enter a number between 1 and 9.")


def play_game():
    """Run one complete Tic-Tac-Toe game."""

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    current_player = "X"

    print("\n================================")
    print("       TIC-TAC-TOE")
    print("================================")

    display_positions()

    while True:

        display_board(board)

        move = get_player_move(board, current_player)

        board[move] = current_player

        
        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        
        if check_draw(board):
            display_board(board)
            print("🤝 It's a draw!")
            break

        
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    """Main program."""

    while True:

        play_game()

        print("\n--------------------------------")
        choice = input("Do you want to play again? (y/n): ").lower()

        if choice != "y":
            print("\nThanks for playing Tic-Tac-Toe! 🎮")
            print("Goodbye! 👋")
            break



if __name__ == "__main__":
    main()