# TensorFlow 学习



## 安装

我使用window 10 python 3.7进行对TensorFlow的学习。

期间出现了几个大坑

1. TensorFlow对window的兼容性可能不是很好（官网上推荐用Linux或者Mac，虽然我有Linux deepin，但是总感觉用得别扭），如果直接用 pip install tensorflow 总是会有各种问题，最后我用Anaconda来安装TensorFlow，用anaconda的好处是它可以根据python的版本选择合适的TensorFlow版本 [这是anaconda的详细教程](https://www.jianshu.com/p/62f155eb6ac5)
2. 网速慢,使用国内conda镜像源

如果以后要重装TensorFlow的话,[就按照这个教程](https://blog.csdn.net/KID_yuan/article/details/88775254)



## 初期学习方法和目标

1. [官网教程](http://tensorfly.cn/tfdoc/tutorials/mnist_beginners.html),简单教程是中文版的,这些都是机器学习基础中的基础,要认真学
2. 在官网中文教程中有一些扩展链接,这些多为英文,可以当成英语阅读理解.
3. 然后是老师要求的[micro-courses](https://www.kaggle.com/learn/overview),这个看前六个
4. 根据上面六个micro-courses 写六篇学习笔记
5. 每三天汇报一次进度
6. 登录kaggle, 验证码无法显示





a//b remove fractional parts

a** b exponentiation

if you want to get some help about a function which you forget, select the function and press **ctrl + Q**

for example, if you select function print, it will displace **print(value, ..., sep=' ', end=' ', file=sys.stdout, flush=False)** on the screen

file parameter can allow you to print things into a file

if you want to find which function you can use in a class, select the class and press **shift + ctrl + I**

```python
def mult_by_five(x):
    return 5 * x

def call(fn, arg):
    """Call fn on arg"""
    return fn(arg)

def squared_call(fn, arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))

print(
    call(mult_by_five, 1),
    squared_call(mult_by_five, 1), 
    sep='\n', # '\n' is the newline character - it starts a new line
)
# result 
# 5 
# 25
```

```python
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x % 5

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number is the biggest modulo 5?',
    max(100, 51, 14, key=mod_5),
    sep='\n',
)
# result:
# Which number is biggest?
# 100
# Which number is the biggest modulo 5?
# 14
```

Elements at the end of the list can be accessed with negative numbers, starting from -1

```python
# All the planets except the first and last
planets[1:-1]
```

tuples are almost exactly the same as lists. They differ in just two ways.

1. the syntax for creating them uses parentheses rather than square brackets
2. they can not be modified once they are defined

**List comprehensions** are a very unique features

```python
squares = [n**2 for n in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

short_planets = [planet for planet in planets if len(planet) < 6]
# ['Venus', 'Earth', 'Mars']

loud_short_planets = [
    planet.upper() + '!' 
    for planet in planets 
    if len(planet) < 6
]
# ['VENUS!', 'EARTH!', 'MARS!']

# count for negative number
len([num for num in nums if num < 0])
sum([num < 0 for num in nums])
```

```python
'/'.join([month, day, year])
# '01/31/1956'

"{}, you'll always be the {}th planet to me.".format(planet, position)
# "Pluto, you'll always be the 9th planet to me."

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
"{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
# "Pluto weighs about 1.3e+22 kilograms (0.218% of Earth's mass). It is home to 52,910,390 Plutonians."

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)
```

```
# Get the rows with population over 1m in South America
df[(df['population'] > 10**6) & (df['continent'] == 'South America')]
```

