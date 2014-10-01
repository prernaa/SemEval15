import sys
sys.path.append("/Users/Prerna/Desktop/Prerna/NTU/Courses-Year4-Sem1/NLP/SemEval15/code");


import extractTypes #importing file for extracting types from input
from collections import OrderedDict # OrderedDict to sort feature names in dictionary struct

#filename = "test_input.tsv";
filename = "../rawdata/train/twitter-train-cleansed-B_rmnotav.tsv";
startColIdx = 3;

typesDict = extractTypes.extractTypes(filename, startColIdx);

#The line below does NOT work!
#OrderedDict(sorted(typesDict.items(), key=lambda t: t[0]));

print "Number of types extracted = ", len(typesDict);

#To print the types and their total number of occurrences... uncomment for speed
#for key in typesDict:
#    print key+" : ",typesDict[key]," ";

import extractFeatureVecX; #importing file for extracting feature vector X from training data
print "Feature Vector X Extraction Started";
Xfeatures = extractFeatureVecX.extractFeatureVecX(filename, startColIdx, typesDict);
print "Feature Vector X of size ", len(Xfeatures), " extracted";

labelIdx = 2;
import handleClassLabels;
print "Class Label Vector Y Extraction Started";
YLabels = handleClassLabels.extractClassLabels(filename, labelIdx);
print "Class Label Vector Y of size ", len(YLabels), " extracted";


# Training SVM
from sklearn import svm
from sklearn import linear_model
print "Declaring SVM"
#clf = svm.LinearSVC(); # linearsvc1
clf = svm.LinearSVC(class_weight='auto'); # linearsvc2
#clf = svm.SVC(cache_size = 1000, class_weight='auto', kernel = 'poly'); # Predicts all as POSITIVE :((
#clf = linear_model.SGDClassifier();  # not tried yet
print "Fitting Data To SVM"
clf.fit(Xfeatures, YLabels);
print "SVM trained"


# Saving Trained Classifier
from sklearn.externals import joblib
print "Saving SVM"
fileToSave = "UnigramSVMClassifier.joblib.pkl";
_ = joblib.dump(clf, fileToSave, compress=9);
print "Classifier SAVED!";



#### CAN BE INEFFICIENT! CAN MAKE PREDICTIONS LINE BY LINE, IF WE FACE ISSUES
# Extract feature vector from test data
testFilename = "../rawdata/test/input/twitter-dev-input-B_rmnotav.tsv"
testStartColIdx = 3
print "XTEST Feature Vector Extraction Started";
XTestFeatures = extractFeatureVecX.extractFeatureVecX(testFilename, testStartColIdx, typesDict);
print "XTEST Feature Vector of size ", len(XTestFeatures), " extracted";
#Using Trained SVM to classify data
predictedLabels = clf.predict(XTestFeatures);

#Writing predicted labels to file
writeToFile = "UnigramSVMIgnoreUNK-B.txt"
handleClassLabels.labelsToFile(predictedLabels, writeToFile);


print "SUCCESS!";
