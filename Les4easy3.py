import random

result = [random.randint(-20, 20) for i in range(20) if i % 3 == 0 and i > 0 and i % 4 != 0]
print(result)
