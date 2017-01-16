[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> Exercise 2.4 Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?    

```python
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_wgt = firsts.totalwgt_lb  
other_wgt = others.totalwgt_lb  

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var)
    return d
    
CohenEffectSize(first_wgt, other_wgt)  
```

#### The result is -0.089, meaning the difference in means is -0.089 standard deviation, which is relatively small. First babies are lighter than other babies. Earlier in the book we saw that the Cohen's D for difference in pregnancy length is 0.029, which is smaller than difference in babies' weights.
