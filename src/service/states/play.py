from . import StateInterface, ResolutionState
from ..commands.interface import CommandInterface, ItemCommandInterface, TargetPlayerCommandInterface, InGameCommand
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType, States


class PlayState(StateInterface):

    @property
    def name(self) -> States:
        return States.PLAY_STATE

    def handle(self, command: CommandInterface , session: Session) -> ActionResult:

        current_player = session.player_turn_manager.current_player 

        if not isinstance(command,InGameCommand):
                
                return ActionResult(
                        action_type=ActionType.RANDOM_CMD,
                        is_success=False,
                        error_type=ErrorType.INCORRECT_COMMAND
                    )  

        if isinstance(command, TargetPlayerCommandInterface):
            if not session.player_turn_manager.is_player_in_order(player_id=command.target_player_id): 

                return ActionResult(
                        action_type=ActionType.TARGET_PLAYER,
                        is_success=False,
                        error_type=ErrorType.UNKNOWN_PLAYER
                    )   
    
        if isinstance(command, ItemCommandInterface):
            if not current_player.inventory.is_item_present(item=command.item_type): 
                return ActionResult( 

                    action_type=ActionType.USE_ITEM,
                    is_success=False,
                    error_type=ErrorType.ITEM_NOT_IN_INVENTORY
                )
        
        result = command.execute(session=session)

        if result.is_success:

            session.change_state(new_state=ResolutionState())

        return result


        
        

    
        
        
    
