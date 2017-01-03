# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Similar to lists, values in tuples can be any type and they are indexed by integers. However, tuples are immutable and lists are mutable. Tuples can be used as dictionary keys while lists cannot because list are mutable, which means they can be modified. This creates trouble because we want to keep the dictionary keys consistent.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered collections of elements and sets are unordered collections of unique elements.  
>> Set example:    
>> from sets import Set  
>> * engineers = Set(['John', 'Jane', 'Jack', 'Janice'])  
>> * programmers = Set(['Jack', 'Sam', 'Susan', 'Janice'])  
>> * managers = Set(['Jane', 'Jack', 'Susan', 'Zack'])  
>> * employees = engineers | programmers | managers    
>> List example:  
>> number = [17, 123]  
>> number[1] = 5  
>> print numbers  
>> [17, 5]  


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda is a way to create anonymous functions at runtime. It is used similar to function, but one difference is that the body of a lambda can only consist of a single expression.  
>> Example:  
>> student_tuples = [  
        ('john', 'A', 15),  
        ('jane', 'B', 12),  
        ('dave', 'B', 10),  
]  
>> sorted(student_tuples, key=lambda student: student[2])   # sort by age  
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]  

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension provides a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.  
>> Equivalents with map and list comprehension:  
>> squares = map(lambda x: x**2, range(10))  
>> squares = [ x**2 for x in range(10) ]  
>> Equivalents with filter and list comprehension:  
>> names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']  
>> b_names = filter(lambda s: s.startswith('B'), names)  
>> names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']  



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





