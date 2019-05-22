# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 22:08:05 2019

@author: Vincent Zhao
"""

import numpy as np

#matrix1 = np.genfromtxt('Similarity_Matrix_type2_1.csv', delimiter=',')
#matrix2 = np.genfromtxt('Similarity_Matrix_type2_2.csv', delimiter=',')
#matrix3 = np.genfromtxt('Similarity_Matrix_type2_3.csv', delimiter=',')
#
#test1 = np.genfromtxt('Similarity_Matrix_test_type2_1.csv', delimiter=',')
#test2 = np.genfromtxt('Similarity_Matrix_test_type2_2.csv', delimiter=',')
#test3 = np.genfromtxt('Similarity_Matrix_test_type2_3.csv', delimiter=',')
#
##set1 = np.genfromtxt('Similarity_Matrix_Users_type2_1.csv', delimiter=',')
##set2 = np.genfromtxt('Similarity_Matrix_Users_type2_2.csv', delimiter=',')
##set3 = np.genfromtxt('Similarity_Matrix_Users_type2_3.csv', delimiter=',')
#
#pos1 = np.genfromtxt('Similarity_Matrix_tp_type2_1.csv', delimiter=',')
#pos2 = np.genfromtxt('Similarity_Matrix_tp_type2_2.csv', delimiter=',')
#pos3 = np.genfromtxt('Similarity_Matrix_tp_type2_3.csv', delimiter=',')

matrix1 = np.genfromtxt('Similarity_Matrix_normal_1.csv', delimiter=',')
matrix2 = np.genfromtxt('Similarity_Matrix_normal_2.csv', delimiter=',')
matrix3 = np.genfromtxt('Similarity_Matrix_normal_3.csv', delimiter=',')

test1 = np.genfromtxt('Similarity_Matrix_test_normal_1.csv', delimiter=',')
test2 = np.genfromtxt('Similarity_Matrix_test_normal_2.csv', delimiter=',')
test3 = np.genfromtxt('Similarity_Matrix_test_normal_3.csv', delimiter=',')

#set1 = np.genfromtxt('Similarity_Matrix_Users_normal_1.csv', delimiter=',')
#set2 = np.genfromtxt('Similarity_Matrix_Users_normal_2.csv', delimiter=',')
#set3 = np.genfromtxt('Similarity_Matrix_Users_normal_3.csv', delimiter=',')

pos1 = np.genfromtxt('Similarity_Matrix_tp_normal_1.csv', delimiter=',')
pos2 = np.genfromtxt('Similarity_Matrix_tp_normal_2.csv', delimiter=',')
pos3 = np.genfromtxt('Similarity_Matrix_tp_normal_3.csv', delimiter=',')

threshold = 5

set1 = list(set([list(test1)[n] for n in np.where(matrix1 < threshold)[1]]))
tp1 = [i for i in pos1 if i in set1]

set2 = list(set([list(test2)[n] for n in np.where(matrix2 < threshold)[1]]))
tp2 = [i for i in pos2 if i in set2]

set3 = list(set([list(test3)[n] for n in np.where(matrix3 < threshold)[1]]))
tp3 = [i for i in pos3 if i in set3]


TP_Recall1 = round(len(tp1)/len(pos1), 4)
TP_Recall2 = round(len(tp2)/len(pos2), 4)
TP_Recall3 = round(len(tp3)/len(pos3), 4)

FP1 = round((len(set1)-len(tp1))/(len(test1)-len(pos1)), 4)
FP2 = round((len(set2)-len(tp2))/(len(test2)-len(pos2)), 4)
FP3 = round((len(set3)-len(tp3))/(len(test3)-len(pos3)), 4)

TN1 = round(1 - FP1, 4)
TN2 = round(1 - FP2, 4)
TN3 = round(1 - FP3, 4)

FN1 = round(1 - TP_Recall1, 4)
FN2 = round(1 - TP_Recall2, 4)
FN3 = round(1 - TP_Recall3, 4)

Accuracy1 = round((len(tp1)+(len(test1)-len(set1)))/len(test1), 4)
Accuracy2 = round((len(tp2)+(len(test2)-len(set2)))/len(test2), 4)
Accuracy3 = round((len(tp3)+(len(test3)-len(set3)))/len(test3), 4)

Precision1 = round(len(tp1)/len(set1), 4)
Precision2 = round(len(tp2)/len(set2), 4)
Precision3 = round(len(tp3)/len(set3), 4)

F1_Score1 = round((2*len(tp1))/(2*len(tp1)+(len(set1)-len(tp1))+(len(pos1)-len(tp1))), 4)
F1_Score2 = round((2*len(tp2))/(2*len(tp2)+(len(set2)-len(tp2))+(len(pos2)-len(tp2))), 4)
F1_Score3 = round((2*len(tp3))/(2*len(tp3)+(len(set3)-len(tp3))+(len(pos3)-len(tp3))), 4)


print("Results")
print("-------------------------------------------")

print("True Positive Rate/Recall: ")
print("Test 1: ", TP_Recall1)
print("Test 2: ", TP_Recall2)
print("Test 3: ", TP_Recall3)
print('')

print("False Positive Rate: ")
print("Test 1: ", FP1)
print("Test 2: ", FP2)
print("Test 3: ", FP3)
print('')

print("True Negative Rate: ")
print("Test 1: ", TN1)
print("Test 2: ", TN2)
print("Test 3: ", TN3)
print('')

print("False Negative Rate: ")
print("Test 1: ", FN1)
print("Test 2: ", FN2)
print("Test 3: ", FN3)
print('')

print("Accuracy: ")
print("Test 1: ", Accuracy1)
print("Test 2: ", Accuracy2)
print("Test 3: ", Accuracy3)
print('')

print("Precision: ")
print("Test 1: ", Precision1)
print("Test 2: ", Precision2)
print("Test 3: ", Precision3)
print('')

print("F1_Score: ")
print("Test 1: ", F1_Score1)
print("Test 2: ", F1_Score2)
print("Test 3: ", F1_Score3)
print('\n')


print("-------------------------------------------")
print('\n')

print("Test 1: ")
print("TP/Recall: ", TP_Recall1)
print("FP: ", FP1)
print("TN: ", TN1)
print("FN: ", FN1)
print("Accuracy: ", Accuracy1)
print("Precision: ", Precision1)
print("F1_Score: ", F1_Score1)
print('')

print("Test 2: ")
print("TP/Recall: ", TP_Recall2)
print("FP: ", FP2)
print("TN: ", TN2)
print("FN: ", FN2)
print("Accuracy: ", Accuracy2)
print("Precision: ", Precision2)
print("F1_Score: ", F1_Score2)

print('')

print("Test 3: ")
print("TP/Recall: ", TP_Recall3)
print("FP: ", FP3)
print("TN: ", TN3)
print("FN: ", FN3)
print("Accuracy: ", Accuracy3)
print("Precision: ", Precision3)
print("F1_Score: ", F1_Score3)

print('\n')


#print("Results")
#print("-------------------------------------------")
#
#print("True Positive Rate: ")
#print("Test 1: ", len(tp1)/len(pos1))
#print("Test 2: ", len(tp2)/len(pos2))
#print("Test 3: ", len(tp3)/len(pos3))
#print('')
#
#print("False Positive Rate: ")
#print("Test 1: ", (len(set1)-len(tp1))/(len(test1)-len(pos1)))
#print("Test 2: ", (len(set2)-len(tp2))/(len(test2)-len(pos2)))
#print("Test 3: ", (len(set3)-len(tp3))/(len(test3)-len(pos3)))
#print('')
#
#print("True Negative Rate: ")
#print("Test 1: ", (len(test1)-len(pos1)-(len(set1)-len(tp1)))/(len(test1)-len(pos1)))
#print("Test 2: ", (len(test2)-len(pos2)-(len(set2)-len(tp2)))/(len(test2)-len(pos2)))
#print("Test 3: ", (len(test3)-len(pos3)-(len(set3)-len(tp3)))/(len(test3)-len(pos3)))
#print('')
#
#print("False Negative Rate: ")
#print("Test 1: ", (len(pos1)-len(tp1))/len(pos1))
#print("Test 2: ", (len(pos2)-len(tp2))/len(pos2))
#print("Test 3: ", (len(pos3)-len(tp3))/len(pos3))
#print('')
#
#print("Accuracy: ")
#print("Test 1: ", (len(tp1)+(len(test1)-len(set1)))/len(test1))
#print("Test 2: ", (len(tp2)+(len(test2)-len(set2)))/len(test2))
#print("Test 3: ", (len(tp3)+(len(test3)-len(set3)))/len(test3))
#print('\n')
#
#
#print("-------------------------------------------")
#print('\n')
#
#print("Test 1: ")
#print("TP: ", len(tp1)/len(pos1))
#print("FP: ", (len(set1)-len(tp1))/(len(test1)-len(pos1)))
#print("TN: ", (len(test1)-len(pos1)-(len(set1)-len(tp1)))/(len(test1)-len(pos1)))
#print("FN: ", (len(pos1)-len(tp1))/len(pos1))
#print("Accuracy: ", (len(tp1)+(len(test1)-len(set1)))/len(test1))
#print('')
#
#print("Test 2: ")
#print("TP: ", len(tp2)/len(pos2))
#print("FP: ", (len(set2)-len(tp2))/(len(test2)-len(pos2)))
#print("TN: ", (len(test2)-len(pos2)-(len(set2)-len(tp2)))/(len(test2)-len(pos2)))
#print("FN: ", (len(pos2)-len(tp2))/len(pos2))
#print("Accuracy: ", (len(tp2)+(len(test2)-len(set2)))/len(test2))
#print('')
#
#print("Test 3: ")
#print("TP: ", len(tp3)/len(pos3))
#print("FP: ", (len(set3)-len(tp3))/(len(test3)-len(pos3)))
#print("TN: ", (len(test3)-len(pos3)-(len(set3)-len(tp3)))/(len(test3)-len(pos3)))
#print("FN: ", (len(pos3)-len(tp3))/len(pos3))
#print("Accuracy: ", (len(tp3)+(len(test3)-len(set3)))/len(test3))
#print('\n')














