"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the
following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------

    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

N, M = map(int,input().split()) #7 21
# for i in range(N):
#     print("N VALUE:", i)
#     temp = i // 2
#     print("(N//2) VALUE:", temp)
#     j = ((2*i)+1)

for i in range(N//2): # i values for N=7 are 0,1,2 as 7//2 => 3
    j = ((2*i)+1) #j=1 for i=0, j=3 for i=1, j=5 for i=3
    print((".|."*j).center(M,"-"))
print("WELCOME".center(M,"-"))
for i in reversed(range(N//2)):
    j = ((2 * i) + 1)
    print((".|." * j).center(M, "-"))