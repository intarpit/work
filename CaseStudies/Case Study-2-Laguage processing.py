import pandas as pd
import os
import matplotlib.pyplot as plt


def index(course_dir):
    indexing = pd.DataFrame(columns = ("Dir", "Name"))
    title_num = 1
    for Books in os.listdir(course_dir):
        for book in os.listdir(course_dir + "\\" + Books):
            indexing.loc[title_num] = Books, book
            title_num += 1
    # return indexing
    print(indexing[indexing.Dir == "Books"])
    print(plt.plot(indexing.Dir, indexing.Name, "bo"))
    plt.show()
    # return indexing.Name # ?To get prticular column from the panda dataframe.
            

def counting_words(book):
    """
    Counts the occurance of a word in a book and return a dictionary with all the words with the number of occurance next to it.
    """
    book_lowercase = book.lower()
    remove = ["!", ",", ".", "'", '"', ":",  "*",  "#",  "@",  ";", "(", ")", "[", "]"]

    for r in remove:
        book_lowercase = book_lowercase.replace(r, "")
    #print(book_lowercase)
    
    book_string = book_lowercase.replace("&", "and")
    book_string = book_string.replace("/", " ")
    book_string = book_string.replace("-", " ")
    #print(book_string)
    #print(book_string.find("library"))
    book_list = book_string.split(" ")
    #print(book_list)
    #print(len(book_list))

    occurance = dict()
    for word in book_list:
        #print(word)
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1
    # unique_words = len(occurance.keys())
    # total_words = sum(occurance.values())
    # return unique_words
    # return total_words
    return occurance
    # print("Unique Words = " + str(unique_words))
    # print("Total Words = " + str(total_words))
    # print(occurance)

# The below code runs .pdf or .txt format without pictures easily or the format is utf-8.
course_dir = "" #! Enter the path of the file.
index(course_dir)
# print(book)
# (unique_words, total_words, occurance) = counting_words(book)






