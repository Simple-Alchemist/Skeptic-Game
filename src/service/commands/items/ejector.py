from attrs import define, field

from ...session import Session

from interface import ItemCommandInterface
from ...data_classes import ActionResult, ActionType,  EjectorPayload
from ....core import ItemType

@define(kw_only=True)
class EjectorItemCommand(ItemCommandInterface):

    _item_type: ItemType = field(init=False, default=ItemType.EJECTOR, repr=False)

    @property
    def item_type(self) -> ItemType:
        return self._item_type
    

    def execute(self, session: Session) -> ActionResult:
        
        current_player = session.player_turn_manager.current_player
        shotgun = session.shotgun

        ejected_shell = shotgun.unload_shell()
            
        current_player.inventory.remove_item(item=self._item_type)

        return ActionResult(

            action_type=ActionType.USE_ITEM,
            is_success=True,
            payload=EjectorPayload(item_type=self._item_type,shell_ejected_damage=ejected_shell.damage)
            # in the payload, show the previous shell 
        )