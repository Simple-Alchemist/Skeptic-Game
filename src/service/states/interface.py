from __future__ import annotations


from typing import Protocol, runtime_checkable 

from ..commands.interface import CommandInterface
from ..session import Session
from ..data_classes import ActionResult, States

@runtime_checkable
class StateInterface(Protocol): 

    @property
    def name(self) -> States:
        ...

    def handle(self, command: CommandInterface, session: Session) -> ActionResult: 
        ...



