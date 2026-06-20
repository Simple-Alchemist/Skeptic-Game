from .interface import StateInterface
from ..commands import CommandInterface, AboveGameCommand
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType, States


class RoundManagerState(StateInterface):

    @property
    def name(self) -> States:
        return States.ROUND_MANAGER
    
    def handle(self, command: CommandInterface, session: Session) -> ActionResult:
        
        if not isinstance(command, AboveGameCommand): 
            return ActionResult( 
                action_type=ActionType.RANDOM_CMD,
                is_success=False, 
                error_type=ErrorType.INCORRECT_COMMAND
            )

        result = command.execute(session=session)
        
        return result

        
        

    
        
        
    
