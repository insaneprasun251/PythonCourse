# import pandas
#
# dict_of_frequencies = {}
# final_frequency = 0
#
#
# def iterate_through_frequencies(frequency_file, final_frequency=final_frequency,
#                                 dict_of_frequencies=dict_of_frequencies):
#     frequencies = pandas.read_csv(frequency_file)
#     for row in frequencies.iterrows():
#         if '-' in str(row[1]):
#             # print("Negative value: " + str(row[1]))
#             final_frequency -= abs(int(row[1]))
#             if final_frequency in dict_of_frequencies.keys():
#                 dict_of_frequencies[final_frequency] += 1
#                 return str(final_frequency)
#             else:
#                 dict_of_frequencies[final_frequency] = 1
#         else:
#             final_frequency += int(row[1])
#             if final_frequency in dict_of_frequencies.keys():
#                 dict_of_frequencies[final_frequency] += 1
#                 return str(final_frequency)
#             else:
#                 dict_of_frequencies[final_frequency] = 1
#     return final_frequency, dict_of_frequencies
#
#
# while 2 not in dict_of_frequencies.values():
#     print(iterate_through_frequencies("frequencies.txt"))
#
# print("Final: " + str(int(final_frequency)))
# print(dict_of_frequencies)

import itertools

# 1

data = [int(x) for x in open("frequencies.txt").readlines()]
print(sum(data))

# 2

freq = 0
seen = {0}

for num in itertools.cycle(data):
    freq += num
    if freq in seen:
        print(freq)
        break
    seen.add(freq)
