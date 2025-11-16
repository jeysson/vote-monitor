from dataclasses import dataclass

@dataclass
class Bill:  
    # The id of the bill  
    id: int

    # The name of the bill
    title: str

    # The id of the primary sponsor(of type Person)
    sponsor_id: int

