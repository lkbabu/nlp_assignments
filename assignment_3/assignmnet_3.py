#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
User: I am unhappy.
ELIZA: DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY
User: I need some help, that much seems certain.
ELIZA: WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP
User: Perhaps I could learn to get along with my mother.
ELIZA: TELL ME MORE ABOUT YOUR FAMILY
User: My mother takes care of me.
ELIZA: WHO ELSE IN YOUR FAMILY TAKES CARE OF YOU
User: My father.
ELIZA: YOUR FATHER
"""


import re 
while True:
    inp=input()
    l1=re.search(r'unhappy',inp)
    l2=re.search(r'some[\s]+help',inp)
    l3=re.search(r'my[\s]+mother',inp)
    l4=re.search(r'takes[\s]+care .*',inp)
    l5=re.search(r'My[\s]+father.*',inp)
    if l1:
        print("DO YOU THINK COMING HERE WILL HELP YOU NOT TO BE UNHAPPY")
    elif l2:
        print("WHAT WOULD IT MEAN TO YOU IF YOU GOT SOME HELP")
    elif l3:
        print("TELL ME MORE ABOUT YOUR FAMILY")
    elif l4:
        n=re.sub(r'me','you',string=l4.group())   
        print('WHO ELSE IN YOUR FAMILY '+n.upper())
    elif l5:
        n2=re.sub(r'My','your',string=l5.group()) 
        n2=n2.upper()
        print(n2)


# In[ ]:




