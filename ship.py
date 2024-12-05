class Ship:
    def __init__(self, x: int, y: int, name: str) -> None:
        """
        Initialize a ship object with given coordinates and name.
        """
        self.x = x
        self.y = y
        self.name = name
        self.sunk = False

    def got_hit(self):
        """
        Mark the ship as sunk when it gets hit.
        """
        self.sunk = True

    def has_sunk(self) -> bool:
        """
        Returns True if the ship has sunk, otherwise False.
        """
        return self.sunk

    def get_name(self) -> str:
        """
        Returns the name of the ship.
        """
        return self.name

    def get_coord(self) -> tuple[int, int]:
        """
        Returns the (x, y) coordinates of the ship.
        """
        return self.x, self.y

    def __repr__(self) -> str:
        """
        Returns a string representation of the ship.
        """
        return f"{self.name}: {'Sunk' if self.sunk else 'Afloat'}"

    @staticmethod
    def create_ships() -> list["Ship"]:
        """
        Create ships based on user input, ensuring validity.
        """
        ships = []
        print("Creating ships...")
        while len(ships) < 10:
            inp = input("> ").strip()
            if inp == "END SHIPS":
                break
            parts = inp.split()
            if len(parts) != 3:
                print("Error: <symbol> <x> <y>")
                continue

            symbol, x, y = parts[0], parts[1], parts[2]
            if not ('A' <= symbol <= 'J'):
                print("Error: symbol must be between 'A'-'J'")
                continue
            if not (x.isdigit() and y.isdigit()):
                print("Error: coordinates must be integers")
                continue

            x, y = int(x), int(y)
            if not (0 <= x < 5 and 0 <= y < 5):
                print(f"Error: ({x}, {y}) is out-of-bounds on 5x5 board")
                continue
            if any(ship.get_coord() == (x, y) for ship in ships):
                print(f"Error: ({x}, {y}) is already occupied by another ship")
                continue
            if any(ship.get_name()[-1] == symbol for ship in ships):
                print(f"Error: symbol '{symbol}' is already taken")
                continue

            ships.append(Ship(x, y, f"Ship{symbol}"))
            print(f"Success! Ship{symbol} added at ({x}, {y})")

        return ships
