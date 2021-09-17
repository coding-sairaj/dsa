# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max_number = int(input())
odd_list = list(range(1, max_number + 1))
print([x for x in odd_list if x % 2])