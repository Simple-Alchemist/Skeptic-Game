# All of this code will be used in states 

       # if not ptm.is_player_in_order(player_id=self._target_id): 

        #     return ActionResult(
        #         action_type=ActionType.SHOOT,
        #         is_success=False,
        #         error_type=ErrorType.UNKNOWN_PLAYER
        #     )
# the above code is when the targetted player is not in the order 

        # if shotgun.is_magazine_empty(): 

        #    return ActionResult(
        #             action_type=ActionType.SHOOT,
        #             is_success=False,
        #             error_type=ErrorType.EMPTY_MAGAZINE
        #             )

# the above code,  when the magazine is empty 


        # if not current_player.inventory.is_item_present(item=self._item_type): 
        #      return ActionResult( 
        #           action_type=ActionType.LOADING_DOUBLE_DAMAGE_SHELL,
        #           is_success=False,
        #           error_type=ErrorType.ITEM_NOT_IN_INVENTORY
        #      )
# when the item is not present in the current's player inventory