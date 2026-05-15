
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
       
        count=Counter(s)

        scount=sorted(count.items(),key=lambda x:x[1], reverse=True)
        final_lst=[]
        print(scount)
        for k,v in scount:
            for i in range(v):
                final_lst.append(k)

        return "".join(final_lst)