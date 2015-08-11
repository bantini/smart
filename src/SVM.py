__author__ = 'nilayan'
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import os.path
from os.path import join
#SVM using Pandas
#LinearSVC.fit()
class Tweet:
    def __init__(self,t,cat):
        self.t = t
        self.cat = cat

def TwitterSVMClassifier(path,f):
    relevant = []
    categories = [0,1]
    verify_path  =  os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'input'))
    with open(join(verify_path,'Syria_relevant.txt'),'r') as r:
        for line in r:
            temp = Tweet(line,0)
            relevant.append(temp)
    with open(join(verify_path,'Syria_irrelevant.txt'),'r') as r:
        for line in r:
            temp = Tweet(line,1)
            relevant.append(temp)
    vectorizer_rel = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
    train_rel = vectorizer_rel.fit_transform(r.t for r in relevant)
    for vector in train_rel:
        print vector


TwitterSVMClassifier("","")
