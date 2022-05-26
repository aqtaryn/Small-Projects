total = 0
counter = 0
while counter < 1000:
    if counter % 3 == 0:
        total += counter
    elif counter % 5 == 0:
        total += counter
    counter += 1
print(total)