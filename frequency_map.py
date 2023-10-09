with open("dataset_2_13 (1).txt", "r") as file:
    content = file.read()
    first_line = content.split('\n')[0]
    second_line = content.split('\n')[1]

text_input = first_line
k_input = second_line

# print(first_line)
# print(second_line)

# method 1
# def FrequentPatterns(text, k):
#     Pattern = {}
#
#     for i in range(len(text) - k):
#         k_mer = text[i: i + k]
#         if k_mer in Pattern:
#             pass
#         else:
#             Pattern[k_mer] = text.count(k_mer)
#
#     print(Pattern)
#
# FrequentPatterns(text_input, k_input)


# method 2
def frequency_table(text, kmer_len):
    freq_map = {}
    nt = len(text)
    nk = kmer_len

    for i in range(0, nt - nk):
        pattern = text[i: i + nk]
        if not freq_map.get(pattern):
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1

    return freq_map


freq_map = frequency_table(text_input, k_input)

freq_map = {k: v for k, v in sorted(freq_map.items(), key=lambda item: item[1])}

print(freq_map)

# print(max(freq_map, key=freq_map.get))
