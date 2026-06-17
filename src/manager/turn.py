from __future__ import annotations

from collections import deque

from attrs import Factory, define, evolve, field
from attrs.validators import in_

from ..core.player import Player, PlayerException

@define
class TurnManager:
    """Manages the turn order and direction of play for players in the game.
    It is an immutable class; all methods that modify the order or direction
    return a new TurnManager instance.
    """

    _order: deque[int] = field(default=Factory(deque), init=False)
    _direction: int = field(
        default=1,
        converter=int,
        validator=in_((-1, 1)),
        init=False
    )

    @property
    def current_player_id(self) -> int:
        
        try:
            return self._order[0] 

        except IndexError:
            raise PlayerException("Couldn't retrieve the current player.")

    @property
    def turn_order(self) -> tuple[int, ...]:

        return tuple(self._order)

    def remove_player_id(self, player_id: int) -> None:

        try:

            self._order.remove(player_id)

        except ValueError:
            raise PlayerException("There is no player with this ID.")

    def add_player_id(self, player_id: int) -> None:

        if  player_id in self._order:
            raise PlayerException("couldn't able to add the player")

        self._order.append(player_id)

    def advance(self, turns: int = 1) -> None:

        self._order.rotate(-(turns  * self._direction))

    def reverse_order(self) -> None:
 
        self._direction = self._direction * -1
