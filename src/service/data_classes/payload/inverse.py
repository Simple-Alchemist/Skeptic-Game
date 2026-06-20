from .interface import ItemPayloadInterface
from ....core import ItemType
from attrs import define

@define(kw_only=True)
class InversePayload(ItemPayloadInterface):
    
    item_type: ItemType
    previous_shell_damage: int 
    new_shell_damage: int 
