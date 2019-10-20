from typing import Any


def start(self: Any) -> None:  # type: ignore[misc]
    print("Machine started")


Machine = type(
    "Machine",
    (object,),
    {"start": start},  # type: ignore[misc]
)


def run(self: Any) -> None:  # type: ignore[misc]
    print("Running!")


Car = type(
    "Car",
    (Machine, object),
    {"run": run},  # type: ignore[misc]
)

machine = Machine()  # type: ignore[misc]
machine.start()  # type: ignore[misc]
car = Car()  # type: ignore[misc]
car.start()  # type: ignore[misc]
car.run()  # type: ignore[misc]
