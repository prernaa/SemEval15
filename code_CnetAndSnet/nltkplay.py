myTweet = "Who had two thumbs and is the happiest girl in the world because she might get Greys Anatomy season 4 tomorrow? Oh yeah, thats me! ;)"

# Split Tweet into sentences using punkt module
import nltk.data
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences = tokenizer.tokenize(myTweet)
print sentences
print ""


##print "NER"
### Trying NER tagging
##from nltk.tag.stanford import NERTagger
##stner = NERTagger('/usr/share/stanford-ner-3.4/classifiers/english.all.3class.distsim.crf.ser.gz', '/usr/share/stanford-ner-3.4/stanford-ner.jar')
##
##for s in sentences:
##    tokens = s.split()
##    print stner.tag(tokens)
##    print ""
    

print "POS"
# Trying POS tagging
from nltk.tag.stanford import POSTagger
stpos = POSTagger('/usr/share/stanford-postagger-3.4-eng/models/english-left3words-distsim.tagger', '/usr/share/stanford-postagger-3.4-eng/stanford-postagger.jar')
for s in sentences:
    tokens = s.split()
    print stpos.tag(tokens)
    print ""

##print "Wordnet Lematizer"
### Trying wordnet lematizer
##from nltk.stem import WordNetLemmatizer
##wnl = WordNetLemmatizer()
##for s in sentences:
##    tokens = s.split()
##    i=0
##    for t in tokens:
##       tokens[i] = wnl.lemmatize(t)
##       i=i+1
##    print tokens
##    print ""

    

##print "Lancaster Stemming"
### Trying Lancaster Stemming Algorithm
##from nltk.stem.lancaster import LancasterStemmer
##stlstem = LancasterStemmer()
##for s in sentences:
##    tokens = s.split()
##    i=0
##    for t in tokens:
##       tokens[i] = stlstem.stem(t)
##       i=i+1
##    print tokens
##    print ""

##print "Snowball English Stemmer"
##from nltk.stem.snowball import EnglishStemmer
##snowstem = EnglishStemmer()
##for s in sentences:
##    tokens = s.split()
##    i=0
##    for t in tokens:
##       tokens[i] = snowstem.stem(t)
##       i=i+1
##    print tokens
##    print ""

print "Stanford Parser"
# Trying the Stanford Parser
