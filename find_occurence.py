text_input = "ATCCACCATCCACCCACTATCCACCATCCACCTTCATCCACCATCCACCATCCGATCCACCGCACATCCACCCGGATCCACCCGTTATCCACCTAAAAATCCACCGTTATCCACCTCCAAATCCACCTATCCACCGCATCCACCATCCACCGATCCACCATCCACCCCTTATCCACCCTGTATCCACCGGAGATCCACCCATCCACCCAACCTTCCTCATCCACCGCCAGGATCCACCTATCCACCGCGATCACATCCACCCCAATCCACCATCCACCTAATATCCACCGAAATCCACCATCCACCATCCACCATCCACCAAATTATCCACCGTTGTATCCACCGTCCATCCACCTAAATCCACCTTATCCACCATATCCACCTATCCACCACATCCACCATCCACCAATCCACCATCCACCTTAATCCACCCTGGCGAACGGAATCCACCCTCAAGTTGATCCACCGAATCCACCGCGATCCACCATCCACCCAAGTTTGATCCACCGTCTATCCACCTTACTCATCCACCATCCACCGGAATCCACCTCGCATCCACCGTTCATCCACCCCAGAATCCACCAAATCCACCGACGATCCACCTAAATCCACCATCCACCGCGATCCACCGATCCACCTGCTCCAGGAACCTATCCACCATCCACCCATCCACCAATCCACCATCCACCATCCACCTATCCACCATCCACCATCCACCATCCACCATCCACCATCCACCAAGAATCCACCGCAATCCACCTATCCACCATCCACCGCTATCCACCGTATCCACCAGTGATCCACCATCCACCCATCCACCCGTTAGATCCACCGATCCACCATCCACCATCCACCAAAGATCCACCTTGATCCACCGGGGAATCCACCCCATCCACCAGTTCAAATCCACCATCCACCTAATCCACCATCCACCATCCACCGAAATCCACCGATCCACCAGCGATCCACCATCCACCCATTCATCCACCTATCCACCGATCCACCGATCCACCGATCCACCTATCCACC"
pattern_input = "ATCCACCAT"

# method 1
def PatternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i: i + len(pattern)] == pattern:
            count += 1
    return count

print(PatternCount(text_input, pattern_input))


# method 2
# def PatternCount(text, pattern):
#     count = start = 0
#     while True:
#         start = text.find(pattern, start) + 1
#         if start > 0:
#             count += 1
#         else:
#             return count
#
# print(PatternCount(text_input, pattern_input))


# method 3
# import re
# print(len(re.findall("(?=TATCTTCTA)",text_input)))


# method 4
# import regex as re
# def PatternCount(text, pattern):
#     return len(re.findall(pattern, text, overlapped=True))
#
# print(PatternCount(text_input,pattern_input))