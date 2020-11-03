number_one = int(input())
number_two = int(input())

print(number_one if number_two < number_one else number_two)
print(number_two if number_two < number_one else number_one)
