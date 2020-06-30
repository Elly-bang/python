
jb=[1,'two',3,'four',5,'six']
print(jb)
print(jb[3])
print(jb[-2])
print(jb[1:3])
print(jb[3:])
print(jb[4:])
jb=[1,'two',3,'four',5,'six']
jb[1]=2
print(jb) #[1, 2, 3, 'four', 5, 'six']

jb1=[1,2,3]
jb2=jb1*3
print(jb2)

print(len(jb))
'''
1 in jb
6 in jb
1 not in jb
2 not in jb
'''

print(jb)

jb=[1,2,3,4,5]
jb.append(6)
jb

#.copy
jb1=[1,2,3,4,5]
jb2=jb.copy() #[1, 2, 3, 4, 5, 6]
jb2

jb=[1,2,3,2,3,2]
jb.count(2) #3

jb1=[1,2,3]
jb2=[4,5,6]
jb1.extend(jb2)
jb1

jb=['a','b','c','d','e']
jb.index('c')

jb=['a','b','c','a','b']
jb.index('b')

jb=[1,2,3,4,5]
jb.insert(2,100)
jb

jb=[1,2,3,4,5]
jb.pop()

jb=[6,7,8,2,11]
jb.pop()

jb

jb=['a','b','c','d','e']
jb.pop(3)
jb

jb=[1,2,3,4,5]
jb.remove(3)
jb

jb=[1,2,3,1,1]
jb.remove(1)
jb

jb=[3,5,2,6,7]
jb.sort()
jb #[2, 3, 5, 6, 7]

jb.sort(reverse=True)
jb

#tuple : 여러개의 자료를 하나의 변수로 관리할때

jb=(1,2,3,4,5)
type(jb) #<class 'tuple'>

jb=()
jb #()

jb=tuple()

print()
jb=(1,2,3,4,5)
print(jb) #(1, 2, 3, 4, 5)
print(jb[2])
print(jb[2:5])
print(len(jb))
1 in jb
9 in jb
1 not in jb
9 not in jb
jb1=(1,2,3)
jb2=(4,5,6)


#dict
a={1:'a'}
a[2]='b'
a['name']='pey'
a[3]=[1,2,3]
a
del a[1]
a

a={1:'a',2;'b'}
a[1]