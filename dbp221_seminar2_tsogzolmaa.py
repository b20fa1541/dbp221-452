#!/usr/bin/env python
# coding: utf-8

# In[11]:


def isPalindrome(s):
    return s == s[::-1]
s = "lemel"
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
     
    # single line to find factorial
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


# In[33]:


def CountOccurrences(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count
string = "likeandlikeandlikeandlikeandlike"
print(CountOccurrences(string, "likeand"))


# In[36]:


list1 = [11, 22, 33]
print("Largest element is:", max(list1))


# In[ ]:




