#N student take K apples & distribute them among each other evenly. The remaining (the undivisible) part
#remains in the basket. HOW many apples will each single student get? How many apples will remain in the
#basket? The programs reads the num N & K. It should print the two answers for the question above.


N= int(input("Enter the num of students= "))
K= int(input("Enter the num of apples= "))
apple_distributed= K//N
apples_in_basket= K%N

print(apple_distributed,)
print(apples_in_basket,)