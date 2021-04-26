a=10
b=20
print(a+b)
if(a>b):
    print("a is greater")
else:
    print("b is greater")

# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2])
print(msg)
print("{0}{1}{0}".format("abra", "cad"))

a = "{x}, {y}".format(x=5, y=12)
print(a)

print(", ".join(["spam", "eggs", "ham"]))
#prints "spam, eggs, ham"

print("Hello ME".replace("ME", "world"))
#prints "Hello world"

print("This is a sentence.".startswith("This"))
# prints "True"

print("This is a sentence.".endswith("sentence."))
# prints "True"

print("This is a sentence.".upper())
# prints "THIS IS A SENTENCE."

print("AN ALL CAPS SENTENCE".lower())
#prints "an all caps sentence"

print("spam, eggs, ham".split(", "))
#prints "['spam', 'eggs', 'ham']"

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(sum([1, 2, 3, 4, 5]))

nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
    print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
    print("At least one is even")

for v in enumerate(nums):
    print(v)
text="My name is abdullah"
char="a"
def count_char(text, char):
  count = 0
  for c in text:
    if c == char:
      count += 1
  return count


def count_char(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

file = open("newfile.txt", "w")
file.write("""Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcenfr fv orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabthu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orgnf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba bg thrff.
Gurer fubhyq or bar-- naq cersrenoylbayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arrire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!""")
file.close()
filename = "newfile.txt"
with open(filename) as f:
    text = f.read()

for char in "abcdefghijklmnopqrstuvwxyz":
    perc = 100 * count_char(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


#####if elif else###

#1. Print next date
def generate_next_date(day,month,year):
    #Start writing your code here
    if((year%400==0 or year%4==0) and month==2):
        next_day=day+1
        next_month=month
        next_year=year
    elif(month==2 and day==28):
        next_day=1
        next_month=month+1
        next_year=year
    elif(month==12 and day==31):
        next_day=1
        next_month=1
        next_year=year+1
    elif(day==31 ):
        next_day=1
        next_month=month+1
        next_year=year
    elif((day==30) and (month==4 or month==6 or month==9 or month==11)):
        next_day=1
        next_month=month+1
        next_year=year
    else:
        next_day=day+1
        next_month=month
        next_year=year




    print(next_day,"-",next_month,"-",next_year)


generate_next_date(28,2,2015)



# pizza slice

n=int(input("engter number of slices"))
if (n%2==0):
    a=120.00*n
    print(a)
else:
    a=123.00*n
    print(a)

x=input()
print(type(x))
## print second highest
l=[1,2,3,4,5,6,7,8,8,9,10,10]
a=list(set(l))
b=a.remove(max(a))
print(max(a))

## change position of every nth to n+1

l=[1,2,3,4]
for i in range(0,len(l),2):
    l[i],l[i+1]=l[i+1],l[i]
print(l)

#max and min of a set
a={1,2,3,4,2,3,5,6,7}
print(max(a))
print(min(a))

#repeated element in a tuple
a=(1,2,3,4,2,1)
c=set()
for i in range(len(a)):
    b=a.count(a[i])
    if b>1:
        c.add(a[i])
d=list(c)
print([d[i] for i in range(len(d))])

###
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)


###
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))

#set
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)


##itertool

from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))

#
import re

pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

print(re.findall(pattern, "eggspamsausagespam"))

##
import re

pattern = r"pam"

match = re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

    ##

import re

str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", str)
print(newstr)

##
import re

pattern = r"gr.y"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

##
import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

##
import re

pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")


##import re

pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

##Juice maker


class Juice:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return (self.name + ' (' + str(self.capacity) + 'L)')

    def __add__(self, newJuice):
        self.name += "&" + str(newJuice.name)
        self.capacity += newJuice.capacity
        return self.__str__


a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

print(a.__add__(b)())