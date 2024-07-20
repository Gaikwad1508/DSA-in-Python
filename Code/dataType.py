name="Abhishek Gaikwad"
age=1500
gender="Male"
weight=100
isStudent=True

# Situdation -> unique, add, remove, edit
# Set
fruitsILiked={"orange", "apple", "banana"}

#Repeated, add, remove, edit
#List
earningFrom2022=[22, 23, 22, 25, 23, 56]

#Fixed, repeat
#Tuple
earningBefore2022=(22, 23, 24, 22, 29, 30)

# Key value
# Dictionary
prop={
    "orange":5,
    "onion":"7kg",
    "mango":"1kg", 
    "pink":21
}

prop["onion"]=19
prop["motor"]=25
print(prop)

del prop["onion"]
del prop["mango"]

print(prop["orange"])

# Initializing with empty
#st={5}    # set
st=set()        #empty set
d={}            #empty dictionary
st={1, 2, 3}
d={"name": 17}

name=""     #empty string
age=0       #zero int
lst=[]      #empty list
tup=()    #empty tuple
d={}        #empty dictionary
st=set()    #empty set
print(st, type(st))

st.add(13)
st.add(12)
st.add(12)
print(st)
st.remove(13)
st.remove(12)
print(len(st))

print(13 in st)
print(prop["orange"])
print(prop.get('pink', -1))
print(prop["pink"])

#None
overHyped=None

print(name, type(name), "")
print(age, type(age))
print(gender, type(gender))
print(weight, type(weight))
print(isStudent, type(isStudent))
print(fruitsILiked, type(fruitsILiked))
print(earningFrom2022, type(earningFrom2022))
print(earningBefore2022, type(earningBefore2022))
print(prop, type(prop))
print(overHyped, type(overHyped))

# List Operations
lst=[1, 2, 15, 20]
lst.append(25)
print(lst) # 1, 2, 15, 20, 25
lst.insert(0, 5)
print(lst) # 5, 1, 2, 15, 20, 25

lst.pop()
lst.pop(0)
print(lst) # 1, 2, 15, 20
lst[0]=21
print(lst) #21, 2, 15, 20

# Tuple Operations
num=(3, 4, 5, 6, 12)
print(num[0])
print(num[-1])


# Mutable and Immutable datatypes 
'''In python immutable datatypes are suppose a variable A has value 5 and its address is 100 and if we make A is 7 in next line of our code then 7 will be stored at different location than 100 let it is 200 if we have a variable B which has value of 5 then it will points to the value present at 100 location because the same value is already present like this python handles storage efficienty'''

#integers
A=5
print(id(A))        #address of A
A=7
print(id(A))

A=5
B=5
print(id(B))
B=7
print(id(A))
print(id(B))

#Floats
weight=12.34
print(id(weight))
weight=34.56
print(id(weight))
weight1=12.34
print(id(weight1))

#Boolean
a=True
b=True
print(id(a))
print(id(b))
a=False
b=False
print(id(a))
print(id(b))

#Strings
name="Abhishek Gaikwad"
print(name[0])
name[2]="l"