def findDuplicate(num):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if num[i] == num[j]:
                return num[i]
                    

nums = [1,2,3,4,5,5]
print(f"repeated numeber was {findDuplicate(nums)}.")