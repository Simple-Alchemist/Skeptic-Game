from .interface import StateInterface
from ..commands.interface import CommandInterface, ItemCommandInterface, TargetPlayerCommandInterface
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType


class PlayState(StateInterface):

    def handle(self, command: CommandInterface , session: Session) -> ActionResult:

        if isinstance(command, TargetPlayerCommandInterface):
            if not session.player_turn_manager.is_player_in_order(player_id=command.target_player_id): 

                return ActionResult(
                        action_type=ActionType.TARGET_PLAYER,
                        is_success=False,
                        error_type=ErrorType.UNKNOWN_PLAYER
                    )   
    
        if isinstance(command, ItemCommandInterface):
            if not session.player_turn_manager.current_player.inventory.is_item_present(item=command.item_type): 
                return ActionResult( 

                    action_type=ActionType.USE_ITEM,
                    is_success=False,
                    error_type=ErrorType.ITEM_NOT_IN_INVENTORY
                )
        
        return command.execute(session=session)



        #At the end, change to Resolution State 

        
        

    
        
        
    
