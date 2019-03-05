import sys


def unique_string(word):
    dictionary = [False for x in range(128)]
    for char in word:
        dictionary[ord(char)] = True
        if dictionary[ord(char)]:
            return False
    return True


def permutation(a, b):
    return len(a) == len(b) and sorted(a) == sorted(b)


def urlify(in_string, in_string_length):
    return "".join("%20" if c == " " else c for c in in_string[:in_string_length])


def one_edit_away(first, second):
    if len(first) == len(second):
        diff = False
        for index, value in enumerate(first):
            if value != second[index]:
                if diff:
                    return False
                diff = True
        return True


def compress(word):
    compressed = []
    word = list(word)
    count = 0
    for index, char in enumerate(word):
        count += 1
        if index + 1 >= len(word) or char != word[index + 1]:
            compressed.append(word[index])
            compressed.append(count)
            count = 0
    return compressed


def rotate(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]):
        return False
    for i in range(len(matrix) // 2):
        first = i
        last = len(matrix) - i - 1
        for j in range(first, last):
            offset = j - first
            matrix[first][i], matrix[last - offset][first], matrix[last][last - offset], matrix[i][
                last
            ] = (
                matrix[last - offset][first],
                matrix[last][last - offset],
                matrix[i][last],
                matrix[first][i],
            )
    return matrix


# print(unique_string('cat'))
# print(permutation('dog', 'god'))
# print(urlify('mr john smith      ', 13))
# print(one_edit_away('pale', 'bale'))
# print(compress('aabcccccaaa'))
matrix = [[1, 2], [3, 4]]
print(rotate(matrix))
