from typing import Set
from typing_extensions import Final

# 集合型データを生成する (重複する値は含まれない)
a: Final[Set[int]] = {1, 2, 3, 3, 4, 5}
print(a)  # => {1, 2, 3, 4, 5}

# 既存のデータを追加する
a.add(1)
print(a)  # => {1, 2, 3, 4, 5}

# 存在しないデータを追加する
a.add(6)
print(a)  # => {1, 2, 3, 4, 5, 6}

# 積集合を得る
b: Final[Set[int]] = {3, 5, 6, 8, 10}
print(a & b)  # => {3, 5, 6}

# 和集合を得る
print(a | b)  # => {1, 2, 3, 4, 5, 6, 8, 10}
