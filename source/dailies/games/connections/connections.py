"""connections.py: A game of Connections, inheriting from the Game class."""

from ...config.dialogue_en import DialogueEn
from ...logs.setup_logging import setup_logging
from ..game_infrastructure import Game

connections_logger = setup_logging()


class Connections(Game):
    def __init__(self, name: str, description: str, instructions: str) -> None:
        """
        Initialise the Connections game.

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
        >>> connections = Connections(
        ...     "Connections",
        ...     "This is a game of connections.",
        ...     "Instructions for the game."
        ... )

        Notes
        -----
        This class initialises the Connections game with a name, description, and instructions.
        """
        super().__init__(
            DialogueEn.CONNECTIONS_NAME,
            DialogueEn.CONNECTIONS_DESCRIPTION,
            DialogueEn.CONNECTIONS_INSTRUCTIONS,
        )

        # TODO: Implement the Connections game.
