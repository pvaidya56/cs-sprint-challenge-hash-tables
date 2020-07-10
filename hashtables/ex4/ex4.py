def has_negatives(a):
    #empty directory for nums list, empty list for negative numbers
    nums_list = dict()
    negative_nums = []

    #check if numbers are not zero AND negative
    for num in a:
        nums_list[num] = 1
        if num != 0 and -num in nums_list:
            #append the number, absolute value
            negative_nums.append(abs(num))

    return negative_nums


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))