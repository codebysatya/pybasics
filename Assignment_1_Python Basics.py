#!/usr/bin/env python
# coding: utf-8

# # Assignment_1_Python Basics

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
Ans: Values- 'hello', -87.8, 6 ,Expressions- *, -, /, +
# 2. What is the difference between string and variable?
Ans: Strings are collection of characters and informations which are immutable, whereas variable stores information, in other language variable is a name that reffers to an object which store the information.
# 3. Describe three different data types.
Ans: Numeric data type like integer where we store integers value eg. a=42, float b=45.5 and complex eg. c=4+5j. Text data type like string eg. d= ‘xyz’. Boolean data type where it will give True if the condition is true or False if condition is false. Other data types are list eg. L = ['x’, ’y’, ’z’] , Tuple eg. T = ('x’, ’y’, ’z’) , Dictionary or dict eg. D = {‘name’ : ‘xyx’, ‘mob_no’ : 7894561233} 
# 4. What is an expression made up of? What do all expressions do?
Ans: Expression are made of operators and operands which are use to produce some other values. Expressions are representations of value which always evaluates down to a single value. eg 5 + 5 where both 5 are int value and + is mathematical operator and this expression evaluates down to integer 10.
# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Ans: Expression are combination of operators and operands which will give result according to expression, whereas Statements are instruction or command to follow like here it says spam = 10 i.e spam holds the value of 10 that has been instructed.
# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1

# In[1]:


bacon = 22


# In[2]:


bacon+1

Ans: 23
# 7. What should the values of the following two terms be?
# 'spam'+'spamspam'
# 'spam'*3

# In[5]:


'spam'+'spamspam'


# In[6]:


'spam'*3

Ans:'spam'+'spamspam'='spamspamspam'
    'spam'*3 = 'spamspamspam'
# 8. Why is eggs a valid variable name while 100 is invalid?

# Ans: Eggs variable is valid cause its data type is string and can be treated as variables, but whereas 100 is integer data type and integer data type can't be treated as variable.

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
Ans: int() float() str() are respected functions to get the integer, floating-point number, or string version of a value.
# 10. Why does this expression cause an error? How can you fix it?
# 'i hate eaten' +99+'burritos.'

# In[16]:


'i hate eaten ' + str(99) +' burritos.'

Ans: Error is because string and integer can't be concatenate hence we have to type cast it i.e type casted integer to string. correct code= 'i hate eaten ' + str(99) +' burritos.'
