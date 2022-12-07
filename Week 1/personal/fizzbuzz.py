# Program Details:
# divisible by 3 , print Fizz
# divisible by 5, print Buzz
# divisible by both 3 and 5, FizzBuzz
# if divivible by none, print the number as it is

# Solution:
# 1. For number input, we use for loop
# 2. 4 conditional statement for checking divisibility

for i in range(1, 100):
    # modulo operator (%) -> remainder
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i% 5 == 0:
        print('Buzz')
    
    else:
        print(i)