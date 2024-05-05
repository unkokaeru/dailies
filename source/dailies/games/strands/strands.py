"""strands.py: A game of Strands, inheriting from the Game class."""

from ...config.dialogue_en import DialogueEn
from ...logs.setup_logging import setup_logging
from ..game_infrastructure import Game

strands_logger = setup_logging()


class Strands(Game):
    def __init__(self, name: str, description: str, instructions: str) -> None:
        """
        Initialise the Strands game.

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
        >>> strands = Strands(
        ...     "Strands",
        ...     "This is a game of Strands.",
        ...     "Instructions for the game."
        ... )

        Notes
        -----
        This class initialises the Strands game with a name, description, and instructions.
        """
        super().__init__(
            DialogueEn.STRANDS_NAME,
            DialogueEn.STRANDS_DESCRIPTION,
            DialogueEn.STRANDS_INSTRUCTIONS,
        )

        # TODO: Implement the Strands game.
