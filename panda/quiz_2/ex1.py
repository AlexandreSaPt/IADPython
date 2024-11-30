import numpy as np

print("Initial value:", end="")
init_value = float(input())


print("Final value:", end="")
final_value = float(input())

print("Number of values:", end="")
n_value = float(input())

interval = (final_value - init_value) / (n_value - 1)

data = np.arange(init_value, final_value + interval / 2, interval, dtype=np.float64 )

data = data**2

sum = np.round((data.sum()), decimals=2)

print(f"Sum of the array: ", end="")
print(sum)


