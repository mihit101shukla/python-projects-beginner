def count_overlapping(a, b):
    counter = 0
    for nums in a:
        for char in nums:
            if b <= char:
                counter += 1
            if nums[0] >= b:
                break
    return counter
print(count_overlapping([[1,2],[5,8],[6,9]], 7))