from .interface import PayLoadInterface
from ....core import ItemType
from attrs import define

@define(kw_only=True)
class EjectorPayload(PayLoadInterface):

    item_type: ItemType
    shell_ejected_damage: int

