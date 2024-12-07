# Write a program that prints the first twenty words of the Fibonacci sequence.
# The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two.

a = 0
b = 1

for _ in range(20): #nie interesuje nas wartość zmiennej pętli
    print(a, end=" ")
    a, b = b, a + b