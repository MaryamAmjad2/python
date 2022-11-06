from Bio.Seq import Seq
import numpy as np
sequence_1 = Seq("CAGACC")
sequence_2 = Seq("CCGTA")
main_matrix = np.zeros((len(sequence_1)+1, len(sequence_2)+1))
match_checker_matrix = np.zeros((len(sequence_1), len(sequence_2)))
match_reward = 10
mismatch_penalty = 5
gap_penalty = -5
for i in range(len(sequence_1)):
 for j in range(len(sequence_2)):
  if sequence_1[i] == sequence_2[j]:
   match_checker_matrix[i][j]= match_reward
  else:
    match_checker_matrix[i][j]= mismatch_penalty
print(match_checker_matrix)
for i in range(len(sequence_1)+1):
 main_matrix[i][0] = i*gap_penalty
for j in range(len(sequence_2)+1):
 main_matrix[0][j] = j * gap_penalty
for i in range(1, len(sequence_1)+1):
 for j in range(1, len(sequence_2)+1):
  main_matrix[i][j] = max(main_matrix[i-1][j-1]+match_checker_matrix[i-1][j-1],
main_matrix[i-1][j]+gap_penalty,
main_matrix[i][j-1]+ gap_penalty, 0)
print(main_matrix)
aligned_1 = ""
aligned_2 = ""
ti = len(sequence_1)
tj = len(sequence_2)
while ti >0 and tj >0:
 if ti >0 and tj >0 and main_matrix[ti][tj] == main_matrix[ti-1][tj-1]+ match_checker_matrix[ti-1][tj-1]:
  aligned_1 = sequence_1[ti-1] + aligned_1
  aligned_2 = sequence_2[tj-1] + aligned_2
  ti = ti - 1
  tj = tj - 1
 elif ti >0 and main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty:
  aligned_1 = sequence_1[ti-1] + aligned_1
  aligned_2 = "-" + aligned_2
  ti = ti -1
 else:
  aligned_1 = "-" + aligned_1
  aligned_2 = sequence_2[tj-1] + aligned_2
  tj = tj - 1
print(aligned_1)
print(aligned_2)
