from random import randint

from attrs import define

from ...session import Session
from ...data_classes import ActionResult, ActionType
from ....core import ItemType
from ..interface import AboveGameCommand

@define(kw_only=True)
class ItemDistributionCommand(AboveGameCommand):

    max_item: int = 4

    def execute(self, session: Session) -> ActionResult:

        items_available: tuple = ItemType.item_available()
        total_item: int = len(items_available)

        for player in session.player_turn_manager.all_player:

            allocate_counter = 0
            while allocate_counter < self.max_item:
                _random_pointer = randint(0, total_item-1)
                player.inventory.add_item(item=items_available[_random_pointer])
                allocate_counter +=1

        return ActionResult(

            action_type= ActionType.ITEM_DISTRIBUTION,
            is_success=True,
            #Adding a Pay load stating what is being added
            )