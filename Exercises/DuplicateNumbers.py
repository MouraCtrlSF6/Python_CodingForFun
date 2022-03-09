def findDuplicate(num):
    for i in range(len(num)):
        repeat = 0
        for j in range(i, len(num)):
            if num[i]==num[j]:
                repeat+=1
                if repeat>1:
                    return num[i]

nums = [1,2,3,4,5,5]
print(f"repeated numeber was {findDuplicate(nums)}.")