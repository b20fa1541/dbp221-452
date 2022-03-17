#!/usr/bin/env python
# coding: utf-8

# In[37]:


def isPalindrome(s):
    return s == s[::-1]
s = "lemmel"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[10]:


def count_upper_case_letters(str_obj):
    count = 0
    for elem in str_obj:
        if elem.isupper():
            count += 1
    return count
count = count_upper_case_letters('This Is MY FirsT claSs OF the DAY')
print(count)


# In[13]:


def count_lower_case_letters(str_obj):
    count = 0
    for elem in str_obj:
        if elem.isupper():
            count += 1
    return count
count = count_lower_case_letters('This Is MY FirsT claSs OF the Day')
print(count)


# In[18]:


number = 11 * 22
print('The product is: ',number)


# In[17]:


def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1);
 
num = 10;
print("Factorial of",num,"is",
factorial(num))


# In[25]:


def Reverse(list):
    return [ele for ele in reversed(list)]
list = [11, 22, 33, 44, 55, 66]
print(Reverse(list))


# In[30]:


numbers = [11, 22, 33, 44, 55, 66]
Sum = sum(numbers)
print(Sum)


# In[50]:


list1 = ["hi", "my","hi","I like my hi"]
list2 = []
for elem in list1:
    for candidate in list1:
        if elem == candidate:
            continue
        elif elem in candidate:
            break
    else:
        list2.append(elem)

print(list2)


# In[45]:


list1 = [11, 22, 33]
print("Largest element is:", max(list1))


# In[ ]:




