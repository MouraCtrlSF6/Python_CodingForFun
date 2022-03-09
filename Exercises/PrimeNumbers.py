def primeList(myPrimes):
    findNext = False
    i = myPrimes[len(myPrimes) - 1]
    while(findNext == False):
        i+=1
        for currentPrime in myPrimes:
            if(i%currentPrime > int(i/currentPrime)):
                myPrimes.append(i)
                findNext = True
                break
            elif i%currentPrime == 0:
                break
    return myPrimes
    
def isPrime(num, myPrimes):
    myLastPrime = myPrimes[len(myPrimes) - 1]
    for currentPrime in myPrimes:
        if num%currentPrime > int(num/currentPrime):
            return True
        elif num%currentPrime == 0:
            return False
        elif currentPrime >= myLastPrime:
            myPrimes = primeList(myPrimes)
            myLastPrime = myPrimes[len(myPrimes) - 1]
myPrimes = [2, 3, 5, 7, 11, 13, 19, 23]
num = int(input("Type a number: "))
if isPrime(num, myPrimes):
    print("Yes, ",num, " is prime")
else: print("No, ", num, " is not prime")
