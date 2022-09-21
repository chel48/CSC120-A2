"""
creates a computer object with the properties of a computer
"""
class Computer: 
    
    """
initializes the properties of the computer and makes them members of the object
"""
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int): 
        self._description = description
        self._processor_type = processor_type
        self._hard_drive_capacity = hard_drive_capacity
        self._memory = memory
        self._operating_system = operating_system
        self._year_made = year_made
        self._price = price

    """
creates a dictionary containing the properties of the computer
"""
    def _create_computer(self): 
        return {'description': self._description,
            'processor_type': self._processor_type,
            'hard_drive_capacity': self._hard_drive_capacity,
            'memory': self._memory,
            'operating_system': self._operating_system,
            'year_made': self._year_made,
            'price': self._price
    }