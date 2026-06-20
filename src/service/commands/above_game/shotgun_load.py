from random import shuffle

from attrs import define, field

from ...session import Session
from ....core import LiveShell, BlankShell
from ...data_classes import ActionResult, ActionType, ErrorType
from ..interface import AboveGameCommand


@define(kw_only=True)
class ShotgunLoad(AboveGameCommand):

    lives: int 
    blanks: int 
    random: bool = True

    def execute(self, session: Session) -> ActionResult:

        magazine_list: list = list()

        for _ in range(0, self.lives): 
            magazine_list.append(LiveShell())

        for _ in range(0, self.blanks):
            magazine_list.append(BlankShell())

        if self.random: 
            shuffle(magazine_list)

        session.shotgun.load_shells(magazine_list)
        

        return ActionResult(

            action_type= ActionType.LOAD_SHELL,
            is_success=True,
            )