"""This File is under development"""

from attrs import define, field

from ...session import Session
from ..interface import ItemCommandInterface
from ...data_classes import ActionResult, ActionType, ErrorType, InversePayload
from ....core import LiveShell, BlankShell, ShellInterface, ItemException, ItemType

@define(kw_only=True)
class InverseShellItemCommand(ItemCommandInterface):

    _item_type: ItemType = field(init=False, default=ItemType.INVERSE_SHELL, repr=False)

    @property
    def item_type(self) -> ItemType:
        return self._item_type
    
    def execute(self, session: Session) -> ActionResult:
        
        current_player = session.player_turn_manager.current_player

        shotgun = session.shotgun

        
        previous_shell, new_shell = None, None

        if shotgun.current_loaded_shell().damage >= 1: 
            previous_shell = shotgun.unload_shell()
            new_shell = BlankShell()
            shotgun.load_shells([new_shell])

        elif shotgun.current_loaded_shell().damage < 1: 
            previous_shell = shotgun.unload_shell()
            new_shell = LiveShell()
            shotgun.load_shells([new_shell])
        
        current_player.inventory.remove_item(item=self._item_type)

        if (previous_shell is None) or (new_shell is None):
            return ActionResult(
                action_type=ActionType.USE_ITEM,
                is_success=False,
                error_type=ErrorType.INVALID_SHELL_STATE  
            )

        return ActionResult(

            action_type=ActionType.LOADING_DOUBLE_DAMAGE_SHELL,
            is_success=True,
            payload=InversePayload(item_type=self._item_type, previous_shell_damage=previous_shell.damage, new_shell_damage=new_shell.damage)
            # in the payload, show the previous shell 
        )

        