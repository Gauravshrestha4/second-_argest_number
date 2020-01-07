"""
Write a function that takes an array of integers given a string
as an argument and returns the second max value from the input array.
If there is no second max return -1.
1. For array ["3", "-2"] should return "-2"
2. For array ["5", "5", "4", "2"] should return "4"
3. For array ["4", "4", "4"] should return "-1" 
(duplicates are not considered as the second max)
4. For [] (empty array) should return "-1"."""

def find_second_highest(arr):
    
    if len(arr)<2: 
        return -1
    # assigning inital values to highest and second_highest 
    if arr[1]<arr[0]:
        highest=int(arr[0])
        second_highest=int(arr[1])
    else:
        second_highest=int(arr[0])
        highest=int(arr[1])
    # loop to check for second highest number 
    for x in range(2,len(arr)):
        if int(arr[x])>second_highest or second_highest==highest:
            second_highest=int(arr[x])
        elif int(arr[x])>second_highest and int(arr[x])>highest:
            second_highest=highest
            highest=int(arr[x])
        elif int(arr[x])>second_highest and int(arr[x])<highest:
            second_highest=int(arr[x])

    return str(second_highest) if second_highest!=highest else "-1"
    

print(find_second_highest(arr))
