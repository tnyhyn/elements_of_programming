def firstPrime(n):
        if (n % 2 == 0):
                return 2
        i = 3
        while(i * i <= n):
                print(n)
                if(n % i == 0):
                        return i
                i += 2
        return n

print(firstPrime(3292937))