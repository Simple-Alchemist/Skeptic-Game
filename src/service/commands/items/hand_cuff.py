

from attrs import define, field

from ...session import Session
from ...data_classes import ActionResult, ActionType, ErrorType
from interface import TargetPlayerCommandInterface, ItemCommandInterface
from core import ItemException,ItemType 

@define(kw_only=True)
class HandCuffItemCommand(ItemCommandInterface, TargetPlayerCommandInterface): #this item demands a lot

    _target_player_id: int = field(alias="target_id")
    _item_type: ItemType = field(init=False, default=ItemType.HAND_CUFF, repr=False)

    @property
    def item_type(self) -> ItemType:
        return self._item_type
    
    @property
    def target_player_id(self) -> int: 
        return self._target_player_id
    
    def execute(self, session: Session) -> ActionResult:
        
        current_player = session.player_turn_manager.current_player

        if self._target_player_id == current_player.id:
            
            return ActionResult(
                action_type=ActionType.USE_ITEM,
                is_success=False,
                error_type=ErrorType.HAND_CUFFING_YOURSELF
            )
        
        targeted_player = session.player_turn_manager.get_player(self._target_player_id)

        if targeted_player.is_cuffed:

            return ActionResult(
                action_type=ActionType.USE_ITEM,
                is_success=False,
                error_type=ErrorType.ALREADY_CUFFED
            )
            
        targeted_player.hand_cuff() 

        current_player.inventory.remove_item(item=self._item_type)

        return ActionResult(

            action_type=ActionType.USE_ITEM,
            is_success=True,
            # pay load code to be written
            )

        