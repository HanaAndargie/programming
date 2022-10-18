class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k=k%sum(chalk)
        while k>=0:
            j=0
            while j<len(chalk):
                k-=chalk[j]
                if k<0:
                    return j
                j+=1
        
