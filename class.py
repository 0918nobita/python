from typing_extensions import Final


class Counter:
    count = 0

    def up(self) -> None:
        self.count += 1
        return

    def down(self) -> None:
        self.count -= 1
        return


counter: Final = Counter()
print(counter.count)  # => 0
counter.up()
counter.up()
print(counter.count)  # => 2
counter.down()
print(counter.count)  # => 1
