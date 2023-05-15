#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from random import *

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789"

password = ""
max_pass = int(input("Enter the length of the password:  "))

for i in range(max_pass):
    password += choice(chars)
    
print(password)


# In[ ]:




