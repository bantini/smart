import re, math, collections, itertools, os
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.classify import svm
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import SpecialEntityRemover as se
from sklearn import cross_validation

#Using Naive Bayes on set of Files 'RT_POLARITY_POS_FILE','RT_POLARITY_NEG_FILE','RT_EVALUATION_FILE'. most of the code has been copied from the Example file
POLARITY_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
RT_POLARITY_POS_FILE = os.path.join(POLARITY_DATA_DIR, 'Syria_relevant.txt')
RT_POLARITY_NEG_FILE = os.path.join(POLARITY_DATA_DIR, 'Syria_irrelevant.txt')
RT_EVALUATION_FILE = os.path.join(POLARITY_DATA_DIR, 'isis_isil_clean.txt')

#this function takes a feature selection mechanism and returns its performance in a variety of metrics
def evaluate_features(feature_select):
    posFeatures = []
    negFeatures = []
    #http://stackoverflow.com/questions/367155/splitting-a-string-into-words-and-punctuation
    #breaks up the sentences into lists of individual words
    #(as selected by the input mechanism) and appends 'pos' or 'neg' after each list
    with open(RT_POLARITY_POS_FILE, 'r') as posSentences:
        for i in posSentences:
            posWords = se.pattern_matcher(i.split())
            posWords = [feature_select(posWords), 'rel']
            posFeatures.append(posWords)
    with open(RT_POLARITY_NEG_FILE, 'r') as negSentences:
        for i in negSentences:
            negWords = se.pattern_matcher(i.split())
            negWords = [feature_select(negWords), 'irr']
            negFeatures.append(negWords)


    #selects 3/4 of the features to be used for training and 1/4 to be used for testing
    posCutoff = int(math.floor(len(posFeatures)*3/4))
    negCutoff = int(math.floor(len(negFeatures)*3/4))
    trainFeatures = posFeatures[:posCutoff] + negFeatures[:negCutoff]
    testFeatures = posFeatures[posCutoff:] + negFeatures[negCutoff:]

    #trains a Naive Bayes Classifier
    classifier = NaiveBayesClassifier.train(trainFeatures)

    #initiates referenceSets and testSets
    referenceSets = collections.defaultdict(set)
    testSets = collections.defaultdict(set)

    #puts correctly labeled sentences in referenceSets and the predictively labeled version in testsets
    for i, (features, label) in enumerate(testFeatures):
        referenceSets[label].add(i)
        predicted = classifier.classify(features)
        testSets[predicted].add(i)

    #prints metrics to show how well the feature selection did
    print 'train on %d instances, test on %d instances' % (len(trainFeatures), len(testFeatures))
    print 'accuracy:', nltk.classify.util.accuracy(classifier, testFeatures)
    print 'pos precision:', nltk.metrics.precision(referenceSets['rel'], testSets['rel'])
    print 'pos recall:', nltk.metrics.recall(referenceSets['rel'], testSets['rel'])
    print 'neg precision:', nltk.metrics.precision(referenceSets['irr'], testSets['irr'])
    print 'neg recall:', nltk.metrics.recall(referenceSets['irr'], testSets['irr'])
    classifier.show_most_informative_features(10)
    new_reference_set = collections.defaultdict(set)
    with open(RT_EVALUATION_FILE, 'r') as reader:
        for i in reader:
            words = se.pattern_matcher(i.split())
            predicted_value = classifier.classify(dict([(word, True) for word in words]))
            new_reference_set[predicted_value].add(i)
    print len(new_reference_set['rel'])
    print len(new_reference_set['irr'])

#creates a feature selection mechanism that uses all words
def make_full_dict(words):
    return dict([(word, True) for word in words])
"""
#tries using all words as the feature selection mechanism
print 'using all words as features'
evaluate_features(make_full_dict)

#scores words based on chi-squared test to show information gain (http://streamhacker.com/2010/06/16/text-classification-sentiment-analysis-eliminate-low-information-features/)
def create_word_scores():
	#creates lists of all positive and negative words
	posWords = []
	negWords = []
	with open(RT_POLARITY_POS_FILE, 'r') as posSentences:
		for i in posSentences:
			posWord = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
			posWords.append(posWord)
	with open(RT_POLARITY_NEG_FILE, 'r') as negSentences:
		for i in negSentences:
			negWord = re.findall(r"[\w']+|[.,!?;]", i.rstrip())
			negWords.append(negWord)
	posWords = list(itertools.chain(*posWords))
	negWords = list(itertools.chain(*negWords))

	#build frequency distibution of all words and then frequency distributions of words within positive and negative labels
	word_fd = FreqDist()
	cond_word_fd = ConditionalFreqDist()
	for word in posWords:
		word_fd.inc(word.lower())
		cond_word_fd['pos'].inc(word.lower())
	for word in negWords:
		word_fd.inc(word.lower())
		cond_word_fd['neg'].inc(word.lower())

	#finds the number of positive and negative words, as well as the total number of words
	pos_word_count = cond_word_fd['pos'].N()
	neg_word_count = cond_word_fd['neg'].N()
	total_word_count = pos_word_count + neg_word_count

	#builds dictionary of word scores based on chi-squared test
	word_scores = {}
	for word, freq in word_fd.iteritems():
		pos_score = BigramAssocMeasures.chi_sq(cond_word_fd['pos'][word], (freq, pos_word_count), total_word_count)
		neg_score = BigramAssocMeasures.chi_sq(cond_word_fd['neg'][word], (freq, neg_word_count), total_word_count)
		word_scores[word] = pos_score + neg_score

	return word_scores

#finds word scores
word_scores = create_word_scores()
#finds the best 'number' words based on word scores
def find_best_words(word_scores, number):
	best_vals = sorted(word_scores.iteritems(), key=lambda (w, s): s, reverse=True)[:number]
	best_words = set([w for w, s in best_vals])
	return best_words

#creates feature selection mechanism that only uses best words
def best_word_features(words):
	return dict([(word, True) for word in words if word in best_words])
"""
#numbers of features to select
#numbers_to_test = [10, 100, 1000, 10000, 15000]
#tries the best_word_features mechanism with each of the numbers_to_test of features
#for num in numbers_to_test:
#print 'evaluating best %d word features' % (num)
#best_words = find_best_words(word_scores, num)
#evaluate_features(best_word_features)
print 'using all words as features'
evaluate_features(make_full_dict)
