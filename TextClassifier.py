## Classifying whether a given text snippet is related with Apple (the company) or apple (the fruit)

##Training Data

apple_computer_train=open('apple-computers.txt','r').readlines()
apple_fruit_train=open('apple-fruit.txt','r').readlines()

stopwords = ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]

from collections import defaultdict


def get_corpus(apple_computer_train):
    corpus_computer = {}
    for line in apple_computer_train:
        words = line.strip().lower().split()
        l_w = len(words)
        for w in words:
            if w not in corpus_computer:
                corpus_computer[w] = 0
            corpus_computer[w] +=1
    return l_w, corpus_computer

n_c, c = get_corpus(apple_computer_train)
n_f, f = get_corpus(apple_fruit_train)

entire_corpus = set(c.keys()).union(set(f.keys()))

corpus_dict = {}
for word in entire_corpus:
        wfc = c.get(word,0)
        wff = f.get(word,0)
        if word in c and word in f or word in stopwords:
            corpus_dict[word] = 0.0
        else:
            corpus_dict[word] = 1 # using 1 instead of log(2)

#Building term frequency-inverse document frequency

def get_tfidf(c, entire_corpus):
    c_words = {}
    for word in c:
        value = c[word]*corpus_dict.get(word,0)
        c_words[word] = value
    return c_words

computer_dictionary = get_tfidf(c, entire_corpus)
fruit_dictionary = get_tfidf(f, entire_corpus)

##Boosting scores for certain underweighted keywords

computer_dictionary['samsung'] = 1500
fruit_dictionary['vinegar'] = 5000
fruit_dictionary['chill'] = 15

# ##################################


# def process_alchemy_dict(dct):
#     computer_bigrams = {}
#     computer_unigrams = {}
#     for word in dct['keywords']:
#         w = word['text'].lower()
#         relevance = word['relevance']
#         w_list = w.replace('apple',"").split()
#         if len(w_list) >= 1:
#             #bigram
#             computer_bigrams[(unicode(" ".join(w_list)))] = relevance
#             for word in w_list:
#                 word = unicode(normalize_word(word))
#                 if word not in computer_unigrams:
#                     computer_unigrams[word] = 0
#                 computer_unigrams[word] += float(relevance)
#     return computer_unigrams, computer_bigrams


# ##################################


# c_unigram, c_bigram = process_alchemy_dict(computer)
# c_unigram[unicode('samsung')] = 15
# c_unigram[unicode('economy')] = 1.5
# c_unigram[unicode('icahn')] = 20
# c_unigram[unicode('ipad')] = 20

# c_unigram[unicode('technology')] = 1

# ##################################


# f_unigram, f_bigram = process_alchemy_dict(fruit)

# f_unigram[unicode('vinegar')] = 1
# f_unigram[unicode('chill')] = 1

# ugs = set(f_unigram.keys())
# cgs = set(c_unigram.keys())
# common_set = cgs.intersection(ugs)
# unique_set = cgs.symmetric_difference(ugs)

# def find_bigrams(input_list):
#   return zip(input_list, input_list[1:])

# ##################################


N = int(raw_input())
testcases = []
for i in range(N):
    testcases.append(raw_input().strip())

tc = 0
for line in testcases:
    tc +=1
    p_f = 1
    p_c = 1
    words = line.lower().split()
    for word in words:
        p_c += 1*float(computer_dictionary.get(word, 0))/5479
        p_f += 1*float(fruit_dictionary.get(word, 0))/2376
    if p_c/(p_c+p_f)>0.5:
        print "computer-company"
    else:
        print "fruit"
