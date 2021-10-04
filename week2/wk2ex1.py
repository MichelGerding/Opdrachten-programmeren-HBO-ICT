e= [2,7,1]
pi =[3,1,4,1,5,9]

answer0=e[:2] + pi[-2:]       # 2759
answer1=e[1:]                 # 71
answer2=e[2:3]*2 + e[0:1]     # 112
answer3=pi[1:]                # 14159
answer4=e[::-2] + pi[0:][::2] # 12345 


# #strings

h = "hanze"
s = "hogeschool"
g = "groningen" 

answer5=s[:2] + g[4] 
answer6=s[4:8]+g[-2:]*2 
answer7=(h+s).replace('h','') 
answer8 = (g[0] + h[1:3][::-1])*2 + h[:2]*5 
answer9 = s[-1]+h[-1]+g[0:4][::2] + g[2:4][::-1] + s[1:4][::-1]
answer10 = s[-1]+h[-1] + g[0]*2 + g[4:7] + s[4]  # leggings




