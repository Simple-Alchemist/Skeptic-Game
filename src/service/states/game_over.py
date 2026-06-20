from . import StateInterface
from ..commands.interface import CommandInterface
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType, States


class GameOverState(StateInterface):
    
    @property
    def name(self) -> States:
        return States.GAME_OVER

    def handle(self, command: CommandInterface , session: Session) -> ActionResult:

        return ActionResult(
            action_type=ActionType.RANDOM_CMD,
            is_success=False,
            error_type=ErrorType.GAME_OVER
        ) 
        

    