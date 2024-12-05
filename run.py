from ship import Ship


def create_board() -> list[list[Ship | None]]:
    """Creates a 5x5 game board initialized with None."""
    return [[None for _ in range(5)] for _ in range(5)]


def place_ships_on_board(board: list[list[Ship | None]], ships: list[Ship]) -> None:
    """Places ships on the board based on their coordinates."""
    for ship in ships:
        x, y = ship.get_coord()
        board[y][x] = ship


def print_board(board: list[list[Ship | None]]) -> None:
    """Prints the game board."""
    for row in board:
        print(" ".join(ship.get_name()[-1] if ship and not ship.has_sunk() else "X" if ship else "." for ship in row))


def is_finished(board: list[list[Ship | None]]) -> bool:
    """Checks if all ships on the board are sunk."""
    return all(ship.has_sunk() for row in board for ship in row if ship)


def main():
    """Runs the Battleship game."""
    print("Creating ships...")
    ships = Ship.create_ships()

    # Create a 5x5 board and place ships
    board = create_board()
    place_ships_on_board(board, ships)

    print("Game started. Fire at will!")
    attempts = 10  # Limit to 10 attempts
    turns = 0

    while not is_finished(board) and turns < attempts:
        print_board(board)
        user_input = input(f"Enter X, Y coordinate [{turns + 1}/{attempts}]: ").strip()

        # Validate user input
        if not user_input or "," not in user_input:
            print("Invalid input format. Please enter coordinates as 'x, y'.")
            continue

        try:
            x, y = map(int, user_input.split(","))
        except ValueError:
            print("Invalid coordinates. Please enter integers separated by a comma.")
            continue

        # Check if the coordinates are in bounds
        if not (0 <= x < 5 and 0 <= y < 5):
            print("Invalid coordinates. Try again.")
            continue

        turns += 1
        target = board[y][x]

        if target:
            if target.has_sunk():
                print(f"Miss! Ship at ({x}, {y}) is already sunk.")
            else:
                target.got_hit()
                print(f"You sank {target.get_name()}!")
        else:
            print("Miss!")

    # Game over
    if is_finished(board):
        print("Congratulations! All ships are sunk.")
    else:
        print("Game over! You ran out of attempts.")
    print_board(board)


if __name__ == "__main__":
    main()
