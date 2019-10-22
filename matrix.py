import numpy as np

a = np.array([1, 2, 3])  # type: ignore[misc]

print(a.shape)  # type: ignore[misc] # => (3,)
