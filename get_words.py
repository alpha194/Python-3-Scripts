'''Program that opens a txt file and returns the words split.
   Author:  J Hill
   Date:  13th May 2014
'''
def get_words_from_file(filename):
    '''Returns a list of split words from a file'''
    open_file = open(filename, 'r', encoding="utf-8")
    open_file = open_file.readlines()
    lines = [line.strip() for line in open_file]	
    values = str(lines)
    values = values.split()
    new_list = []
    for word in values:
        if word.isalpha() == True:
            new_list.append(word)		
    for word in new_list:
        print(word)

        