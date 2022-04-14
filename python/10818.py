

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print("{} {}".format(nums[0], nums[N - 1]))

