"""
    4334번: 평균은 넘겠지
    Create by Kim Gayoun on 2022-03-23
"""
if __name__ == "__main__":
    C = int(input())

    for i in range(C):
        nums = list(map(int, input().split()))
        del(nums[0])

        avg = sum(nums) / len(nums)
        i   = 0
        for n in nums:
            if n > avg: i = i + 1


        print("{:.3f}%".format(round(i / len(nums) * 100, 3)))

