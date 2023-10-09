text_input = 'a'
find_pattern_input = "AGAGGTTAG"


# method 1
def matching(text, find_pattern):
    position = []
    for i in range(len(text) - len(find_pattern) + 1):
        if text[i: i + len(find_pattern)] == find_pattern:
            position.append(i)
    return position


print(*matching(text_input, find_pattern_input), sep=" ")

# method 2
# data = PatternMatching(find_pattern_input, text_input)
# print(*data, sep='  ')
