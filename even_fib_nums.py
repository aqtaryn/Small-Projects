total = 0
previous = 0
current = 1
while current < 4.0e6:
    if current % 2 == 0:
        total += current
    temporary = current
    current += previous
    previous = temporary
print(total)