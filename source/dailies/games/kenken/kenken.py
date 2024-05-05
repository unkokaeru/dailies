"""kenken.py: A game of KenKen, inheriting from the Game class."""

from ...config.dialogue_en import DialogueEn
from ...logs.setup_logging import setup_logging
from ..game_infrastructure import Game

kenken_logger = setup_logging()


class KenKen(Game):
    def __init__(self, name: str, description: str, instructions: str) -> None:
        """
        Initialise the KenKen game.

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
        >>> kenken = KenKen(
        ...     "KenKen",
        ...     "This is a game of KenKen.",
        ...     "Instructions for the game."
        ... )

        Notes
        -----
        This class initialises the KenKen game with a name, description, and instructions.
        """
        super().__init__(
            DialogueEn.KENKEN_NAME,
            DialogueEn.KENKEN_DESCRIPTION,
            DialogueEn.KENKEN_INSTRUCTIONS,
        )

        # TODO: Implement the KenKen game.
