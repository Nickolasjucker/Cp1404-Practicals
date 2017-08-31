def main():
    str_input = str(input("Enter a sentence: ")).lower()
    counts = dict()
    words = str_input.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    longest_word = max(str_input.split(), key=len)
    width = len(longest_word)

    for key in sorted(counts.keys()):
        print("{:{}} : {}".format(key, width, counts[key]))
main()