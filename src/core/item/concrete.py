from attrs import define, field

@define(kw_only=True)
class Item:
    """
    Item Interface Class which allows you to create Concrete Item
    
    
    Attributes:
        _id: int -> Holds a ID 
        _desc: str -> a bit of description of the item
    """
    _id: int = field(alias="id")
    _desc: str = field(alias="desc")

    @property
    def id(self) -> int: 
        
        """id property, returning the id of the item in integer"""
        return self._id

    @property
    def desc(self) -> str:

        """desc property, returning the description of the item in string"""  
        return self._desc