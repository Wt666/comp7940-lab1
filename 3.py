# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

def print_factor(l_factor):
    for j in l_factor:
        print("")
        for i in range(1,1+j):
            if j % i == 0:
                print(i)
print_factor(l)