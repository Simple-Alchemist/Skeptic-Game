from attrs import define, field

from ...session import Session
from ...data_classes import ActionResult, ActionType, ErrorType, ShootPayload
from ..interface import TargetPlayerCommandInterface

@define(kw_only=True)
class ShootCommand(TargetPlayerCommandInterface):

    _target_player_id: int = field(alias="target_player_id")

    @property
    def target_player_id(self) -> int: 
        return self._target_player_id
    

    def execute(self, session: Session) -> ActionResult:
        
        shotgun = session.shotgun 
        
        ptm = session.player_turn_manager
        
        fired_shell = shotgun.unload_shell()

        targeted_player = ptm.get_player(self._target_player_id)

        if targeted_player.health < fired_shell.damage:
            targeted_player.adjust_health(targeted_player.health)

        targeted_player.adjust_health(-fired_shell.damage)

        return ActionResult(

            action_type= ActionType.SHOOT,
            is_success=True,
            payload=ShootPayload(damage_dealt=fired_shell.damage)

            )


        


        


