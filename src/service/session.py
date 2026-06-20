from attrs import define, field

from ..core import Shotgun, PlayerTurnManager
from .states import StateInterface, RoundManagerState, ResolutionState

@define(kw_only=True)
class Session:
    
    player_turn_manager: PlayerTurnManager = field(factory=PlayerTurnManager)
    shotgun: Shotgun = field(factory=Shotgun)
    _states: StateInterface = field(init=False, factory=RoundManagerState) 

    _history: list[object] = field(init=False)#to be worked

    def change_state(self, new_state: StateInterface) -> None: 

        self._states = new_state

        if isinstance(self._states, ResolutionState): 
            self._states.enter(session=self)

    def export_snapshot(self) -> None: 
        ...
    def import_snapshot(self) -> None:
        ...
    
    def _add_history(self):
        ...

    


    