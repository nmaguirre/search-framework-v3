from abc import ABC, abstractmethod

class SearchState(ABC):
    """
    Abstract base class for any search state.
    Must be hashable for their use in sets (e.g., visited sets for search algorithms).
    """
    
    @abstractmethod
    def __hash__(self) -> int:
        """Hash value of a state (istates must be hashable for use in sets/dictionaries)"""
        pass
    
    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Equality comparison for state checking"""
        pass
    
    @abstractmethod
    def __str__(self) -> str:
        """Human-readable representation of the state"""
        pass


