# text = input("Genome : ")

texts = open("Salmonella_enterica.txt").readlines()

# text = input("text? ")

# texts = open("test.txt").readlines()
text = "".join(texts)


def skew(text):
    skew = 0
    skew_list = [0]

    for i in range(len(text)):
        if text[i] == 'C':
            skew -= 1
        elif text[i] == 'G':
            skew += 1
        else:
            pass
        skew_list.append(skew)
    return skew_list


def min_skew(text):
    skew_list = skew(text)
    minimum = min(skew_list)
    min_skew_list = []
    for i in range(len(text)):
        if skew_list[i] == minimum:
            min_skew_list.append(i)
    min_skew_list = str(min_skew_list)
    # min_skew_list = min_skew_list.replace(',', '')
    print(min_skew_list)


min_skew(text)
