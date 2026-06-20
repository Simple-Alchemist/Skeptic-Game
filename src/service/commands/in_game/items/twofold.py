from attrs import define, field

from ....session import Session
from ....data_classes import ActionResult, ActionType, ShellLoadedPayload
from ...interface import ItemCommandInterface
from .....core import ShellInterface, ItemType


@define(kw_only=True)
class TwoFoldItemCommand(ItemCommandInterface):

    _item_type: ItemType = field(init=False, default=ItemType.TWO_FOLD, repr=False)

    @property
    def item_type(self) -> ItemType:
         return self._item_type
    
    def execute(self, session: Session) -> ActionResult:
        
        current_player = session.player_turn_manager.current_player
  
        if session.shotgun.current_loaded_shell().damage >= 1: 
                session.shotgun.unload_shell()
                session.shotgun.load_shells([DoubleLiveShell()])
      
        current_player.inventory.remove_item(item=self._item_type)

        return ActionResult(

            action_type=ActionType.USE_ITEM,
            is_success=True,
            payload=ShellLoadedPayload(item_type=self._item_type, shell_loaded_damage=session.shotgun.current_loaded_shell().damage)
            # in the payload, show the previous shell 
        )
    
@define(kw_only=True, frozen=True)
class DoubleLiveShell(ShellInterface):

    _damage: int = field(default=2, init=False)

    @property 
    def damage(self) -> int:
        return self._damage
    
