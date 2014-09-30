#TOP LEVEL EVALUATE FILE
import sys
sys.path.append("/Users/Prerna/Desktop/Prerna/NTU/Courses-Year4-Sem1/NLP/SemEval15/code");

import evaluate
E = evaluate.Evaluator();
pPath = "UnigramSVMIgnoreUNK-B.txt";
gPath = "../rawdata/test/gold/twitter-dev-gold-B_rmnotav.tsv";
PIdx = 0;
gIdx = 2;
E.evalPrediction(pPath, PIdx, gPath, gIdx);

print "Average Precision = ", E.getAvgPrecision();
print "Average Recall = ", E.getAvgRecall();

print "Positive Precision = ", E.getPrecision_pos();
print "Negative Precision = ", E.getPrecision_neg();
print "Neutral Precision = ", E.getPrecision_neu();

print "Positive Recall = ", E.getRecall_pos();
print "Negative Recall = ", E.getRecall_neg();
print "Neutral Recall = ", E.getRecall_neu();


print "Percentage Correct = ", E.getPercentCorrect();
