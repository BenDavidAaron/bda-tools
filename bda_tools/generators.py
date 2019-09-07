from typing import Iterable, Any
from inspect import isgenerator
from itertools import islice

class Caching_Generator(object):
    """Wraps a generator and lazily caches returned objects.
    The cache can be iterated over multiple times, unlike a standard generator.
    """
    def __init__(self, gen: Iterable) -> None:
        self.generator: Iterable[Any] = gen
        self.cache: List[Any] = []

    def __iter__(self) -> Iterable:
        self._position = 0
        return self
    
    def __next__(self) -> Any:
        if len(self.cache) > self._position:
            item = self.cache[self._position]
        else:
            item = next(self.generator)
            self.cache.append(item)
        self._position += 1 
        return item
        
            
