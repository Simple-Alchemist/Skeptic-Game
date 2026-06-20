from .interface import StateInterface
from ..commands import CommandInterface
from ..commands.core_game import InitCommand
from ..session import Session
from data_classes import ActionResult, ActionType, ErrorType


class RoundManagerState(StateInterface):

    def handle(self, command: CommandInterface, session: Session) -> ActionResult:

        ...

        
        

    
        
        
    
