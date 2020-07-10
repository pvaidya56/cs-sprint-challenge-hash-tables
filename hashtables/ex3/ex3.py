def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    intersections = dict()

    for array in arrays:
        for num in array:
            if num in intersections:
                intersections[num] += 1
            else:
                intersections[num] = 1
        

    return [data[0] for data in intersections.items() if data[1] == len(arrays)]



if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
