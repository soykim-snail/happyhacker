# module 불러오기 --- import
import random

numbers = [1, 2, 3, 4, 5]
result = random.choice(numbers)
print(result)

pick = random.choice(range(10))
print(pick)

n = random.sample(range(20), 3)
print(n)

# print(dir(random))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 
# 'Random', 'SG_MAGICCONST', 'SystemRandom', 
# 'TWOPI', '_BuiltinMethodType', '_MethodType', 
# '_Sequence', '_Set', '__all__', '__builtins__', 
# '__cached__', '__doc__', '__file__', '__loader__', 
# '__name__', '__package__', '__spec__', '_acos', 
# '_bisect', '_ceil', '_cos', '_e', '_exp', 
# '_inst', '_itertools', '_log', '_os', '_pi', 
# '_random', '_sha512', '_sin', '_sqrt', '_test', 
# '_test_generator', '_urandom', '_warn', 
# 'betavariate', 'choice', 'choices', 'expovariate', 
# 'gammavariate', 'gauss', 'getrandbits', 'getstate', 
# 'lognormvariate', 'normalvariate', 'paretovariate', 
# 'randint', 'random', 'randrange', 'sample', 'seed', 
# 'setstate', 'shuffle', 'triangular', 'uniform', 
# 'vonmisesvariate', 'weibullvariate']

fruits = ['포도', '사과', '귤', '바나나', '파인애플', '자두', '수박']
fruit = random.choice(fruits)
print(fruit)
fruit_box = random.sample(fruits, 3)
print(fruit_box)