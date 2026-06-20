from typing import Protocol, runtime_checkable, TYPE_CHECKING

if TYPE_CHECKING:
    from ..session import Session
    from ..data_classes import ActionResult

from ...core import ItemType


@runtime_checkable
class CommandInterface(Protocol):

    def execute(self, session: "Session") -> "ActionResult":
        ...


@runtime_checkable
class InGameCommand(CommandInterface, Protocol):
    ...


@runtime_checkable
class AboveGameCommand(CommandInterface, Protocol):
    ...


@runtime_checkable
class ItemCommandInterface(InGameCommand, Protocol):

    _item_type: ItemType

    @property
    def item_type(self) -> ItemType:
        ...


@runtime_checkable
class TargetPlayerCommandInterface(InGameCommand, Protocol):

    _target_player_id: int

    @property
    def target_player_id(self) -> int:
        ...
