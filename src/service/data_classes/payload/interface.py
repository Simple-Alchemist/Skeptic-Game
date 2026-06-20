from typing import Protocol
from ....core import ItemType


class PayLoadInterface(Protocol): 

    ...

class ItemPayloadInterface(PayLoadInterface, Protocol): 

    item_type: ItemType