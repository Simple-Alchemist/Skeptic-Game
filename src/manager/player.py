from attrs import define, field

from ..core.player import Player, PlayerException

@define
class PlayerManager:
    """
    Manages the state of all players in the game.

    This is an immutable class that holds a collection of players. Methods that
    modify the collection (e.g., adding or removing a player) will return a new
    instance of PlayerManager with the updated state.
    """

    _pool: dict[int, Player] = field(factory=dict)

    @property
    def player_pool(self) -> tuple[Player,...]:
        """
        A read-only view of the dictionary of players,
        mapping player ID to object.
        """
        return tuple(player for player in self._pool.values())

    def get_player(self, player_id: int) -> Player | None:

        try:
            return self._pool[player_id]
        
        except KeyError:

            raise PlayerException(f"Player with '{player_id}' doesn't exists")
        
    def add_player(self, player: Player) -> None:

        if player.id in self._pool:
            raise PlayerException(f"Player with '{player.id}' already exists.")
        
        self._pool[player.id] = player


    def remove_player(self, player_id: int) -> None:

        if player_id not in self._pool:
            raise PlayerException(f"Player with ID '{player_id}' not found for removal.")

        del self._pool[player_id]
    
    def clear_pool(self) -> None: 

        self._pool.clear()

