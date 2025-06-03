from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  occupied =[]
  seats = list(range(1,N+1))
  available = []
  #append each seat to S
  [occupied.append(seated) for seated in S]
  # Core Logic 
  
  # populate available if not in occ
  [available.append(seat) for seat in seats if seat not in occupied]  
  max_available_capacity  = len(available) 
  return max_available_capacity
  
if __name__ == "__main__":
   N = 10
   K = 1
   M = 2
   S = [2, 6]
   
   print(f"{getMaxAdditionalDinersCount(N,K,M,S)} seats")
