from attrs import define, field

from ...session import Session
from ...data_classes import ActionResult, ActionType, StateChangePayload, States
from ...states import RoundManagerState
from ..interface import CommandInterface



@define(kw_only=True)
class InitCommand(CommandInterface):

    def execute(self, session: Session) -> ActionResult:

        session.change_state(new_state=RoundManagerState())
        
        return ActionResult(
                action_type=ActionType.INITIALIZATION,
                is_success=True,
                payload=StateChangePayload(state_then=States.DORMANT, state_now=States.ROUND_MANAGER)
            )