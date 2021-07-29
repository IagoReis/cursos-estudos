# 10 é exclusivo, ou seja, não será utilizado no loop
for c in range(0, 10):
    print(c)

print("\n\n\n")

for c in [1, 2, 3]:
    print(c)

print("\n\n\n")

for c in range(0, 1000):
    print(c)
    if(c >= 10):
        break;