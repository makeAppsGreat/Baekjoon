"""
    15552번: 빠른 A+B
    Create by Kim Gayoun on 2022-03-22
"""
import sys


if __name__ == "__main__":
    nums = list()

    while True:
        i = sys.stdin.readline().split()
        
        if len(i) == 0: break
        if len(i) == 2:
            nums.append(int(i[0]))
            nums.append(int(i[1]))

    
    result = ""
    for i in range( len(nums) // 2 ): result += "{}\n".format(nums[2 * i] + nums[2 * i + 1]) 


    print(result)
