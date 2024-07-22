from enum import Enum
from typing import Any, TypeAlias, TypeVar, Generic, Optional, Union

class ResultTag(Enum):
    Ok = 0
    Err = 1

T = TypeVar('T')
E = TypeVar('E')

class Ok(Generic[T]):
    def __init__(self, value: T) -> None:
        self._value = value

    def ok(self) -> Optional[T]:
        return self._value
    
    def err(self) -> Optional[E]:
        return None
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Ok) and self._value == other._value
    
    def unwrap(self) -> T:
        return self._value
    
    def unwrap_exit(self) -> T:
        return self._value

class Err(Generic[E]):
    def __init__(self, value: E) -> None:
        self._value = value

    def ok(self) -> Optional[T]:
        return None
    
    def err(self) -> Optional[E]:
        return self._value
    
    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Err) and self._value == other._value
    
    def unwrap(self) ->T:
        raise ValueError(f'Error: {self._value}')
    
    def unwrap_exit(self) -> T:
        print(f'Error: {self._value}')
        exit(0)
    
    

Result: TypeAlias = Union[Ok[T], Err[E]]

