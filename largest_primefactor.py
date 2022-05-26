largest = 0
number = 600851475143
counter = 0
while counter < number:
    counter2 = 1
    flag = True
    while counter2 < counter:
        if counter2 != 1:
            if counter % counter2 == 0:
                flag = False
            counter2 += 1
    if flag == True and counter > largest:
        largest = counter
    counter += 1
print(largest)