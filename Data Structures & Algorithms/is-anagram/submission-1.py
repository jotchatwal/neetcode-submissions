# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#           return Counter(s)==Counter(t)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
         return False

        count = {}
        # Count characters in s
        for char in s:
          if char in count:
             count[char] += 1
          else:
             count[char] = 1 
       # print(count) 
         
        for char in t:
          if char in count:
               count[char] -= 1
          else:
            return False

        for value in count.values():
         if value != 0:
            return False
      
        return True

              

           

         
    
    

    
    
    


