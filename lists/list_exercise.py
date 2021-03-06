import re
from collections import deque

string = 'More than 40% of insect species are declining and a third are endangered, ' \
         'the analysis found. The rate of extinction is eight times faster than that of mammals, ' \
         'birds and reptiles. The total mass of insects is falling by a precipitous 2,5% a year, ' \
         'according to the best data available, suggesting they could vanish within a century. ' \
         'The planet is at the start of a sixth mass extinction in its history, ' \
         'with huge losses already reported in larger animals that are easier to study. ' \
         'But insects are by far the most varied and abundant animals, outweighing humanity by 17 times. ' \
         'They are “essential” for the proper functioning of all ecosystems, the researchers say, ' \
         'as food for other creatures, pollinators and recyclers of nutrients. ' \
         'Insect population collapses have recently been reported in Germany and Puerto Rico, ' \
         'but the review strongly indicates the crisis is global. ' \
         'The researchers set out their conclusions in unusually forceful terms for a peer-reviewed scientific paper: ' \
         '“The [insect] trends confirm that the sixth major extinction event is profoundly impacting [on] ' \
         'life forms on our planet. “Unless we change our ways of producing food, insects as a whole will go down ' \
         'the path of extinction in a few decades,” they write. “The repercussions this will have for the planet’s ' \
         'ecosystems are catastrophic to say the least.”'

# string = string.replace('"', '')
# string = re.sub('"', '', string)
list_strings = string.split('.')
list_strings.pop()
count_lines = len(list_strings)
for el in list_strings:
    print('\t' + el)
print(count_lines)


# Deque creates a simple queue for items, if reaches max the oldest item is deleted
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

q.appendleft(5)
print(q)
