#%%
x = 123
#Output: 321
#%%
x = -123
#Output: -321
#%%
x = 120
#Output: 21

#%%
x = 0
#Output: 0
#%%
Abs  = abs(x)
digit = len(str(Abs))

if x<0:
  a = -1
else:
  a = 1

l = []
i = 1
while i <= digit:
  l.append(int(Abs/10**(digit-i)))
  Abs = Abs - int(Abs/10**(digit-i))*10**(digit-i)
  i += 1


ans = 0
for i, num in enumerate(l):
  ans = ans + num*10**i

print(ans)
#%%
##Way 1
class Solution(object):
    def reverse(self, x):
        Abs  = abs(x)
        digit = len(str(Abs))

        if x<0:
          a = -1
        else:
          a = 1

        l = []
        i = 1
        
        while i <= digit:      
          l.append(int(Abs/10**(digit-i)))
          Abs = Abs - int(Abs/10**(digit-i))*10**(digit-i)
          i +=1


        ans = 0
        for i, num in enumerate(l):
          ans = ans + num*10**i
        
        "if overflow return 0"
        if ans > 2**31 - 1 or ans < -2**31:
            ans = 0

        return ans*a