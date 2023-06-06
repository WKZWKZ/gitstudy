

'aaaabbbccfff'
'abcdghrry'

def repeatedstring(s):
    n = len(s)
    l = []
    repeateds = s[0]
    for i in range(1, n):
        
        if s[i] == repeateds[-1]:
            repeateds += s[i]
        else:
            if len(repeateds) >= 2:
                l.append(repeateds)
            repeateds = s[i]
        if i == n - 1:
            if len(repeateds) >= 2:
                l.append(repeateds)
        
    return l
            
print(repeatedstring('abcdghrry'))

