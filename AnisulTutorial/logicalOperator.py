'''
num1 = 50
num2 = 40
num3 = 100

if num1 > num2 and num1 > num3:
    print("Num1 is highest", num1)

elif num2 > num1 and num2 > num3:
    print("Num2 is highest", num2)

else:
    print("Num3 is highest", num3)

letter = 'g'

if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    print("It is vowel.")
else:
    print("It is consonant.")


# Point grade with 'and' operator.
points = 63

if points >= 90:
    print("You've got A")

elif points>=80 and points<90:
    print("You've got B")

elif points>=70 and points<80:
    print("You've got C")

else:
    print("You failed this class.")

'''

# with chain comparison signs
points = 65

if points >= 90:
    print("You've got A")

elif 80 <= points < 90:
    print("You've got B")

elif 70 <= points < 80:
    print("You've got C")

else:
    print("You failed this class.")
