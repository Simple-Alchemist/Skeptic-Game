from .interface import PayLoadInterface
from ...data_classes import States
from attrs import define, field

@define(kw_only=True)
class StateChangePayload(PayLoadInterface):
    state_then: States 
    state_now: States