#User function Template for python3

class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        dic = {}
        res = []
        ct = 0
        for i in words:
            val = sorted(list(i))
            val = "".join(val)
            
            if val in dic.keys():
                res[dic[val]].append(i)
            else:
                res.append([i])
                dic[val] = ct
                ct += 1
        
        return res
        
            
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends
