from . import StateInterface, RoundManagerState, GameOverState, PlayState
from ..commands import CommandInterface
from ..session import Session
from ..data_classes import ActionResult, ActionType, ErrorType, States


class ResolutionState(StateInterface):

    @property
    def name(self) -> States:
        return States.RESOLUTION_STATE

    def handle(self, command: CommandInterface, session: Session) -> ActionResult:

        return ActionResult(
            action_type=ActionType.RANDOM_CMD, 
            is_success=False, 
            error_type=ErrorType.CURRENTLY_IN_RESOLUTION_STATE)    
    
    def enter(self, session: Session) -> None:

        ptm = session.player_turn_manager

        #A bit of clean Up
        for player in ptm.all_player:
               if not player.is_alive(): 
                   ptm.remove_player(player_id=player.id)
        
        #Checking whether the game is over or not
        if len(ptm.all_player) < 2:
            
            session.change_state(new_state=GameOverState())
            return 
        
        #Condition for Moving to RoundManagerState
        if session.shotgun.is_magazine_empty(): 
           
           for player in session.player_turn_manager.all_player:
               player.inventory.clear_inventory()

           session.change_state(new_state=RoundManagerState())
           return


        #Else -> Continue Transitioning to PlayState

        max_skips = len(ptm.all_player)  # Safety: avoid infinite loop
        skips = 0
        while skips < max_skips and ptm.current_player.is_cuffed():
            ptm.current_player.hand_uncuff()
            ptm.advance()
            skips += 1

        session.change_state(new_state=PlayState())


