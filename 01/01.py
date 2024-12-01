from data import input_string
from collections import Counter

numbers = input_string.split()
    
left_list = numbers[::2] 
right_list = numbers[1::2]

left_list.sort()
right_list.sort()

total_diference = sum(abs( (int) (a) - (int) (b)) for a, b in zip(left_list, right_list))
    
print(total_diference)


right_counter = Counter(right_list)

total_ocurrences = sum(int(num) * right_counter[num] for num in left_list if num in right_list)

print(total_ocurrences)