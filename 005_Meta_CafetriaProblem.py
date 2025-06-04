from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Core Logic 
  S.sort()
  num_new_diners = (S[0] - 1) // (K + 1)
  for i in range(1, len(S)):
    num_new_diners += (S[i] - S[i-1] - K-1) // (K + 1)
  num_new_diners += (N - S[-1]) // (K + 1)
  return num_new_diners
  # populate available if not in occ
  [available.append(seat) for seat in seats if seat not in occupied]  
  max_available_capacity  = len(available) 
  return (max_available_capacity,available)
  
if __name__ == "__main__":
   N = 10
   K = 1
   M = 2
   S = [2, 6]
   print(f"{getMaxAdditionalDinersCount(N,K,M,S)} seats")

  #  print(f"{getMaxAdditionalDinersCount(N,K,M,S)[0]} seats\n{getMaxAdditionalDinersCount(N,K,M,S)[1]}")
