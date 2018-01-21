#source: https://www.youtube.com/watch?v=fkjjqyfN51c
import collections
from pprint import pprint
'''scientists = [
    {'name': 'Ada Lovelace', 'field': 'math', 'born': 1894, 'nobel': False},
    {'name': 'Emmy Noether', 'field': 'math', 'born': 1882, 'nobel': False},
    {'name': 'Marie Curie', 'field': 'physic', 'born': 1867, 'nobel': True},
    {'name': 'Tu Yoyoyu', 'field': 'chemistry', 'born': 1934, 'nobel': True},
    {'name': 'Ada Yonath', 'field': 'chemistry', 'born': 1939, 'nobel': True},
    {'name': 'Sally Ride', 'field': 'physic', 'born': 1951, 'nobel': False}
]'''
Scientist = collections.namedtuple('Scientist', ['name', 'field', 'born', 'nobel'])

scientists = (
    Scientist(name='Ada Lovelace', field='math', born=1894, nobel=False),
    Scientist(name='Emmy Noether', field='math', born=1882, nobel=False),
    Scientist(name='Marie Curie', field='physic', born=1867, nobel=True),
    Scientist(name='Tu Yoyoyu', field='chemistry', born=1934, nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born=1939, nobel=True),
    Scientist(name='Sally Ride', field='physic', born=1951, nobel=False),
)
pprint(scientists)


## FILTER() Function ##
#a = filter(lambda  x: x['nobel'] is True, scientists)

a = filter(lambda  x: x.nobel is True, scientists)

#pprint (a)

#loop approach - not recommended
'''
for x in scientists:
    if x['nobel'] is True:
        print (x)
'''
# function approach
def nobel_filter(x):
    return x.nobel is True

#pprint(tuple(filter(nobel_filter, scientists)))

# MORE APPLICABLE APPROACH

#pprint([x for x in scientists if x['nobel'] is True])

#pprint(tuple([x for x in scientists if x['field'] == 'chemistry']))


## MAP function

names_ang_ages = tuple(map(
            lambda x: {'name': x.name, 'age': 2017 - x.born}, scientists
))

pprint(names_ang_ages)

#Another way of present above
#pprint(tuple( {'name': x.name, 'age': 2017 - x.born} for x in scientists))


## Reduce function

total_age = sum(x['age'] for x in names_ang_ages)
print(total_age)

# same as above but more geek way!
total_age_reduce = reduce(lambda x, y: x + y['age'], names_ang_ages,0)
print(total_age_reduce)


## Multiprocessing
import multiprocessing

print type(scientists)



#result = tuple(map(transform, scientists))
#pprint (result)



