[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> # Exercise 2.4 Using the variable totalwgt_lb, investigate whether first babies are lighter or heavier than others. Compute Cohen’s d to quantify the difference between the groups. How does it compare to the difference in pregnancy length?
>> first_wgt = firsts.totalwgt_lb
>> other_wgt = others.totalwgt_lb
>> CohenEffectSize(first_wgt, other_wgt)
