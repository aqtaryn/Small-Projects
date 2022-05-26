gifts = ["A partridge in a pear tree.", "Two turtle doves and", "Three french hens", "Four calling birds", "Five golden rings", "Six geese a-laying", "Seven swans a-swimming", "Eight maids a-milking", "Nine ladies dancing", "Ten lords a-leaping", "Eleven pipers piping", "Twelve drummers drumming"]
days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
new_gift = []
for i in range(12):
    print("On the {} day of Christmas\nMy true love gave to me:".format(days[i]))
    new_gift.insert(0, gifts[i])
    for gift in new_gift:
        print(gift)
    print()
