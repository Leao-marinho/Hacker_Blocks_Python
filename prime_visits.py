"""
HACKER BLOCKS: PRIME VISITS

PMO gives two random numbers a & b to the Prime Minister. 
PM Modi wants to visit all countries between a and b (inclusive) , 
However due to shortage of time he can't visit each and every country , 
So PM Modi decides to visit only those countries,for which country number has two divisors. 
So your task is to find number of countries Mr. Modi will visit.

Input Format
The first line contains N , no of test cases. 
The next lines contain two integers a and b denoting the range of country numbers.

Constraints
a<=1000000 & b<=1000000. N<=1000

Output Format
Output contains N lines each containing an answer for the test case.

Sample Input
2
1 10
11 20

Sample Output
4
4

@author: Luísa Maria Mesquita
"""

import math

def is_prime(x):
    result = True 

    if(x <= 1):
        result = False

    for i in range(2,int(math.sqrt(x)) + 1):
        if(x % i == 0):
            result = False
            break;

    if(result == False):
        return result
    else:
        return result


number_test_cases = int(input("Number of test cases: "))

result = ""

for i in range(0, number_test_cases):
    number_countries = 0
    input_ = input("Intervals: ")
    input_list = list(input_.split())
    a = int(input_list[0])
    b = int(input_list[1])

    if(number_test_cases > 1000 or a > 1000000 or b > 1000000):
        print("Invalid!")
    
    else:
        for j in range(a, b):
            if(is_prime(j)):
                number_countries = number_countries + 1
        
        result = result + str(number_countries) + "\n"
                      
print("Number of countries Mr. Modi will visit: " + result)   
    