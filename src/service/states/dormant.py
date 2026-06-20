from .interface import StateInterface
from ..commands import CommandInterface
from ..commands.core_game import InitCommand
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType


class DormantState(StateInterface):

    def handle(self, command: CommandInterface, session: Session) -> ActionResult:

        if not isinstance(command, InitCommand):
            return ActionResult(
                action_type=ActionType.INITIALIZATION,
                is_success=False,
                error_type=ErrorType.INCORRECT_COMMAND
            )
        
        result = command.execute(session=session)

        return result
        

    
        
        
    
