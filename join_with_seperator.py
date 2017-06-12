line = 'a b c d'
y = line.split(' ')
for gram in ngrams(y,4):
    word = ' '.join(gram)