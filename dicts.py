from typing import Dict, Tuple
from typing_extensions import Final, TypedDict

MyDict: type = TypedDict(
    "MyDict", {"foo": int, "bar": int}
)

dict_a: Final[MyDict] = {"foo": 0, "bar": 42}
print(dict_a)  # => {'foo': 0, 'bar': 42}

dict_a["foo"] = 100
print(dict_a)  # => {'foo': 100, 'bar': 42}

dict_b: Dict[str, Tuple[int, int, str]] = {
    "a": (1, 2, "hello"),
    "b": (3, 4, "hey"),
}
print(
    dict_b
)  # => {'a': (1, 2, 'hello'), 'b': (3, 4, 'hey')}

del dict_b["b"]
print(dict_b)  # => {'a': (1, 2, 'hello')}
