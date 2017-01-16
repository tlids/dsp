[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> Exercise 5.1 In the BRFSS (see Section 5.4), the distribution of heights is roughly normal with parameters μ = 178 cm and σ = 7.7 cm for men, and μ = 163 cm and σ = 7.3 cm for women.
In order to join Blue Man Group, you have to be male between 5’10” and 6’1” (see http://bluemancasting.com). What percentage of the U.S. male population is in this range? Hint: use scipy.stats.norm.cdf.

#### Solution

```python

import scipy.stats

# Provide the parameters for the distribution of heights
mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

dist.mean(), dist.std()

dist.cdf(mu-sigma)

# First, we know that 5'10" is 177.8 cm and 6'1" is 185.4 cm. We can therefore create the cdf for these values.

# CDF for 177.8cm

dist.cdf(177.8)
```
#### CDF for 177.8 cm is 0.49.

```python

# CDF for 185.9 cm.

dist.cdf(185.4)
```

#### CDF for 185.4 cm is 0.83.

```python

# The difference between these two values is the percentage of US male population in this range.

diff = dist.cdf(185.4) - dist.cdf(177.8)
print (diff)

``` 
#### The difference between the CDF of 185.4 cm and 177.8cm is 0.34, meaning that 34% of US male population fall within the range for Blue Man's height requirement.
