"""mini_crossword.py: A game of Mini Crossword, inheriting from the Game class."""

from ...config.dialogue_en import DialogueEn
from ...logs.setup_logging import setup_logging
from ..game_infrastructure import Game

mini_crossword_logger = setup_logging()


class MiniCrossword(Game):
    def __init__(self, name: str, description: str, instructions: str) -> None:
        """
        Initialise the Mini Crossword game.

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
        >>> mini_crossword = MiniCrossword(
        ...     "Mini Crossword",
        ...     "This is a game of Mini Crossword.",
        ...     "Instructions for the game."
        ... )

        Notes
        -----
        This class initialises the Mini Crossword game with a name, description, and instructions.
        """
        super().__init__(
            DialogueEn.MINI_CROSSWORD_NAME,
            DialogueEn.MINI_CROSSWORD_DESCRIPTION,
            DialogueEn.MINI_CROSSWORD_INSTRUCTIONS,
        )

        # TODO: Implement the Mini Crossword game.
