# Python code to generate lots of CPU calculations on a Raspberry Pi

def heavy_computation():
    result = 0
    for i in range(10**7):  # You can increase this range for more computations
        result += i * i  # Perform some heavy computation, you can change this operation
    return result

# Perform heavy computation
result = heavy_computation()
print("Result:", result)
