from attrs import define, field

from ...session import Session
from interface import ItemCommandInterface
from ....core import ItemType
from ...data_classes import ActionResult, ActionType, ShellLoadedPayload

@define(kw_only=True)
class PeekItemCommand(ItemCommandInterface):

    _item_type: ItemType = field(init=False, default=ItemType.PEEK_SHOTGUN, repr=False)

    @property
    def item_type(self) -> ItemType:
        return self._item_type
    
    def execute(self, session: Session) -> ActionResult:
        
        current_player = session.player_turn_manager.current_player

        loaded_shell_damage = session.shotgun.current_loaded_shell().damage
        
        current_player.inventory.remove_item(item=self._item_type)

        return ActionResult(
            action_type=ActionType.USE_ITEM,
            is_success=True,
            payload=ShellLoadedPayload(item_type=self._item_type,shell_loaded_damage=loaded_shell_damage)
        )