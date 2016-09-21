import time

# Refresh-in-place line test

progress = 0
for i in range(10 + 1):
    progress = i
    time.sleep(0.5)
    print("\r", end="")
    print("Poo Counter: " + "*" * progress + " " * (10 - progress) + "(" + str(progress) + ")", end='', flush=True)
