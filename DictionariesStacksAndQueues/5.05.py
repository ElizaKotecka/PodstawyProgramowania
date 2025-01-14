# A program that counts how many times each word appears in a paragraph

def count_words(paragraph):
    words_list = paragraph.split()
    word_count = {}

    for word in words_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


if __name__=='__main__':

    paragraph = "cat dog mouse cat rat cat mouse"
    word_count = count_words(paragraph)

    for word, count in word_count.items():
        print(f"{word}: {count}")

