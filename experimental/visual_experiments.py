import time

import colorama

colorama.init()

# Refresh-in-place line test

progress = 0
complete = 100
for i in range(complete + 1):
    progress = i
    time.sleep(0.05)
    print("\r", end="")
    if float(progress) / float(complete) < 0.5:
        print(colorama.Fore.RED, end='')
    else:
        print(colorama.Fore.GREEN, end='')
    print("Poo Counter: " + "*" * progress + " " * (complete - progress) + "(" + str(progress) + ")", end='',
          flush=True)

colorama.deinit()
