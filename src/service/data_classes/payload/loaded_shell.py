from .interface import ItemPayloadInterface
from ....core import ItemType
from attrs import define

@define(kw_only=True)
class ShellLoadedPayload(ItemPayloadInterface):
    item_type: ItemType
    shell_loaded_damage: int
