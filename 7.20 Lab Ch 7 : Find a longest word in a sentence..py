def findLongestWord(a_str):
    x = a_str.split(" ")
    max = x[0]
    for i in range(len(x)):
        if len(x[i]) >= len(max):
            max = x[i]
    return max

print(findLongestWord("Apples and bees and functions"))