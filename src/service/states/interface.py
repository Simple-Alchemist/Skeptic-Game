from __future__ import annotations


from typing import Protocol, runtime_checkable 

from ..commands.interface import CommandInterface
from ..session import Session
from ..data_classes import ActionResult

@runtime_checkable
class StateInterface(Protocol): 

    def handle(self, command: CommandInterface, session: Session) -> ActionResult: 
        ...

    # in the handle method, always check whether the current player is hand-cuffed? or dead? 



