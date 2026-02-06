# Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_even(a, b):


    if (a % 2) == 0 and (b % 2) == 0:
        return min(a, b)
    else:
        return max(a, b)

print(lesser_of_two_even(2, 4))
print(lesser_of_two_even(2, 5))


# Write a function takes a two-word string and returns True if both words begin with same letter
def animal_cracker(text):


    wordlist = text.lower().split()

    return wordlist[0][0] == wordlist[1][0]

print(animal_cracker('Levelheaded llama'))
print(animal_cracker('crazy Kangaroo'))


# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def makes_twenty(n1, n2):


    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else:
        pass
    return False

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))


# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):


    first_letter = name[0:3]
    fourth_letter = name[3:]
    return first_letter.capitalize() + fourth_letter.capitalize()

print(old_macdonald("macdonald"))


# Given a sentence, return a sentence with the words reversed
def master_yoda(text):


    sentance = text.split()
    return " ".join(sentance[::-1])
print(master_yoda("i am home"))


# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):


    return (abs(100-n) <= 10) or (abs(200-n) <= 10)
print(almost_there(90))
print(almost_there(150))
print(almost_there(209))


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):


    for i in range(0, len(nums)-1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
        return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))


# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):


    result = ""
    for char in text:
        result += char*3
    return result

print(paper_doll("hello"))


# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):


    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c])-10
    else:
        return "BUST"

print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):


    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
        return total


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))


# Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):


    code = [0, 0, 7, 'x']
# code = [0,7,'x']
# code = [7,'x']
# code = ['x'] lenght = 1
    for num in nums:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))


# Write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):


# check for 0 or 1 input
    if num < 2:
        return 0

# if 2 or greater then
# store our prime number
    primes = [2]
# counting is going upto the input
    x = 3

# x is going through every number upto the input number
    while x < num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)

print(count_primes(100))
