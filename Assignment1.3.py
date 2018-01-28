
# coding: utf-8

# ### Problem Statement
# 
# Write a Python program to accept the user's first and last name and then getting them
# printed in the the reverse order with a space between first name and last name.

# In[2]:


firstname = input("Please Enter Your Firstname : ") # to get user's firstname
lastname  = input("Please Enter Your Lastname : ")   # to get user's lastname
print("{Firstname} {Lastname}".format(Firstname=firstname[::-1],Lastname=lastname[::-1])) # print output

