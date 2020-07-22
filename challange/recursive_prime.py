import sys

sys.setrecursionlimit(10**6)

prime_list = list()


def prime(n, i=2):
    if n == 2 :
        return 2
    
    if i < n :
        
        if n % i == 0 :
            return prime(n-1)
        elif i > 5 :
            print(n, end=" ")
            return prime(n-1)
        else :
            return prime(n,i+1)
        

    
prime(1000)
print(prime_list)


# def prime(n, i=2):
    
#     if (n <= 2): 
#         return True if(n == 2) else False
#     if (n % i == 0): 
#         return False
#     if (i > 5):
 
#         return True 
  
#     return prime(n, i + 1)

# for i in range(1000000):
#     if prime(i) :
#         print(i, end = " ")



# print(prime_list)




# def prime(n,counter):
#     if n <= 1 :
#         return 1
    
#     if n == 2 :
#         return [1,2]
    
#     if n > 3 and counter <= n:
        
#         if counter % 2 != 0 and counter % 3 != 0 and counter != 0 :
            
#             prime_list.append(counter)

#     if counter == n :
#         return prime_list

    
#     counter = counter + 1
#     return prime(n,counter)

# prime(20000,counter)

# print("hello")

# a = list()
# for i in range(1000000):
#     if i % 2 != 0 and i % 3 != 3 and i % 5 != 0 :
#         a.append(i)

# print(a)
