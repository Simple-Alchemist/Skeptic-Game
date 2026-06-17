from attrs import define, field

from types import MappingProxyType
from ..core import Item, ItemException, PlayerException

@define
class InventoryManager:

    _inventory: dict[int, list[Item]] = field(factory=dict)


    @property
    def players_inventory(self) -> MappingProxyType:

        return MappingProxyType(self._inventory)
    
    def player_inventory(self,player_id: int) -> list[Item]:

        if player_id not in self._inventory:
            raise PlayerException(f"No Player with ID '{player_id}'.")
        
        return self._inventory[player_id]
        
    def register_player(self, player_id: int) -> None: 

        self._inventory[player_id] = list()

    def unregister_player(self, player_id: int) -> None: 

        if player_id not in self._inventory:
            raise PlayerException(f"Player with ID '{player_id}' not found for unregistering.")

        del self._inventory[player_id]


    def add_item(self, player_id: int, item: Item) -> None: 

        self.player_inventory(player_id=player_id).append(item)

    def remove_item(self, player_id: int, item: Item) -> None: 

        try:
            self.player_inventory(player_id=player_id).remove(item)

        except ValueError:

            raise ItemException(f"Item of '{item.id}' isn't present in the player's inventory")


    def clear_inventory(self, player_id: int) -> None: 

        self.player_inventory(player_id=player_id).clear()
        



        

