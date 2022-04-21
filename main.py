# Peter's Problem 2022 No.7

count = 0
valid_nums = []

def are_digits_odd(num):
    for digit in str(num):
        if int(digit) % 2 == 0:
            return False
    return True
    
def is_valid(num):
    if num % 9 == 0 and are_digits_odd(num):
        return True
        

for num in range(100, 1000):
    if is_valid(num):
        count += 1
        valid_nums.append(num)

print(f"Answer = {count}")
print(valid_nums)

