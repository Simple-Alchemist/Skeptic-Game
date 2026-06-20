from random import randint

from attrs import define

from ...session import Session
from ...data_classes import ActionResult, ActionType
from ....core import Player
from ..interface import AboveGameCommand

@define(kw_only=True)
class AddPlayerCommand(AboveGameCommand):

    id: int 
    health: int

    def execute(self, session: Session) -> ActionResult:

        session.player_turn_manager.add_player(player_obj=Player(id=self.id, health=self.health))

        return ActionResult(

            action_type= ActionType.ADD_PLAYER,
            is_success=True,
            #Adding a Pay load stating what is being added
            )