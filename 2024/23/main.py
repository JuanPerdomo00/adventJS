def find_missing_numbers(nums):
    # Code here
    nums = sorted(nums)
    return [i for i in range(1, nums[-1]) if i not in nums]


if __name__ == "__main__":
    print(find_missing_numbers([1, 2, 4, 6]))
    print(find_missing_numbers([4, 8, 7, 2]))
    print(find_missing_numbers([3, 2, 1, 1]))
    print(find_missing_numbers([5, 5, 5, 3, 3, 2, 1]))
