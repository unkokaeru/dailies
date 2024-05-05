"""game_infrastructure.py: Classes for the games to inherit from."""

from ..logs.setup_logging import setup_logging

game_infrastructure_logger = setup_logging()


class Game:
    def __init__(self, name: str, description: str, instructions: str) -> None:
        """
        Initialise the game.

        Parameters
        ----------
        name : str
            The name of the game.
        description : str
            The description of the game.
        instructions : str
            The instructions for the game.

        Examples
        --------
        >>> game = Game("Game", "This is a game.", "Instructions for the game.")

        Notes
        -----
        This class initialises the game with a name, description, and instructions.
        """
        self.name = name
        self.description = description
        self.instructions = instructions
        self.score: int | None = None

    def __name__(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.name}: {self.description}"

    def __repr__(self) -> str:
        return f"Game({self.name}, {self.description}, {self.instructions})"

    def play(self) -> None:
        """
        Play the game.

        Examples
        --------
        >>> game.play()

        Notes
        -----
        This method is used to play the game.
        """
        game_infrastructure_logger.info(f"Playing the {self.name} game.")
        print(f"{self.name}: {self.description}")
        print(f"Instructions: {self.instructions}")
        self.score = 0
