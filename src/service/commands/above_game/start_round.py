from random import shuffle

from attrs import define, field

from ...session import Session
from ...states import ResolutionState
from ...data_classes import ActionResult, ActionType
from ..interface import AboveGameCommand


@define(kw_only=True)
class StartRound(AboveGameCommand):

    def execute(self, session: Session) -> ActionResult:

        session.change_state(new_state=ResolutionState())

        return ActionResult(

            action_type= ActionType.START_ROUND,
            is_success=True,
            )