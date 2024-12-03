numbers = [14,7,12,87,64,234,1]

def insertionsorting():
    for a in range (0, len(numbers)):
        minimumitem = 10000000000
        for i in range(a, len(numbers)):#here no -1 is required because the final item doesn't need to be compared to anything
            if numbers[i] < minimumitem:
                minimumitem = numbers[i]
                numbers[a], numbers[i] = numbers[i], numbers[a]
            
        print(numbers)

insertionsorting()