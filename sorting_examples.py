import timeit
import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):            
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    smaller, equal, larger = [], [], []
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

# Arrays/Lists
#arr = [11,3,14,7,1,12,13,6,16,3]
#arr = [33359,20892,56727,55277,58751,65181,20917,19270,22709,14295]
hundred_small = [16,12,6,1,7,1,13,3,15,13,11,10,13,12,11,2,6,7,4,12,3,12,2,2,5,16,14,2,13,2,6,7,13,13,9,6,4,2,16,11,8,2,9,1,1,10,16,13,10,7,16,13,6,16,11,5,14,7,12,3,4,14,2,15,16,4,1,6,2,9,11,14,13,9,14,10,14,8,3,15,15,14,12,6,4,12,2,4,13,9,3,6,2,15,4,12,12,8,9,16]
hundred_large = [54303,56471,37709,37945,49409,29475,36855,60488,39389,25616,16824,10872,59352,52162,15097,50739,55412,32759,14853,36782,56079,14665,16089,16000,32133,33389,37071,48799,17938,57323,31556,60792,5369,59895,27946,14502,4782,60147,23272,17424,3501,40955,35930,21044,49304,15387,47685,15799,34759,65423,47887,64200,37451,34637,49448,40380,7690,52472,37148,45173,1087,24849,39034,49467,63384,45734,471,60383,43238,48838,23490,31662,39345,59935,32763,2118,28560,38548,13878,57307,28356,6549,48846,62477,39044,42222,10504,44684,2929,26763,5103,56569,34247,63442,29512,23392,62315,43688,20081,51401]
five_hundred_large = [55320,11213,39405,6218,53376,20206,64094,44468,41122,9590,59215,25251,44669,64374,511,16596,29563,34563,36964,15958,20824,39620,45078,44760,20976,58988,55732,57528,21311,48366,49594,54479,1519,55720,59450,41174,27885,50900,27018,24478,56683,33688,58937,58483,336,45808,48059,55211,2919,24027,1336,35192,5111,61202,40548,48626,57188,56561,25715,50727,54344,7230,10746,36105,47284,53573,17908,59912,43119,41863,7351,54468,23886,45898,34957,54627,32874,14641,56283,11434,35536,59507,50327,18693,24483,10246,48672,28980,2994,44876,39064,46702,59136,62209,32831,62953,47949,28049,28195,11652,61931,16255,18412,26638,3934,51750,13049,13146,57987,18503,62500,61887,36705,36887,28853,17781,30552,63611,7227,39053,41456,46179,33295,33458,19886,7240,16849,2010,20802,41929,6398,46514,53686,42952,567,13832,34490,49478,49931,43288,5286,12766,6289,43176,49645,186,47153,63034,56710,60868,43998,57623,58106,24346,33544,31850,43264,31091,44933,1137,55640,52833,63082,45921,4738,49804,23971,9446,29161,44384,62185,16557,29928,58409,59908,39151,4980,10201,63532,879,27904,47586,4904,11115,50610,63873,29759,50148,33736,29941,35782,27114,52324,37180,29496,34976,42844,58777,37689,36352,15427,49678,54761,59493,48147,31303,39967,47088,36319,2936,40799,40792,16479,61903,52822,36190,37674,4408,16555,586,35032,19836,27501,9003,38638,44478,43586,61849,7222,836,39087,39732,10163,15966,57499,37095,11306,34061,39182,45072,46076,19199,64545,48636,18058,50797,1602,59904,23114,48371,41795,49892,40351,55801,17738,26719,12024,51792,48808,33946,28539,24137,32242,56732,46351,52628,6238,53218,44335,4150,8857,43484,24773,47887,36900,62440,37631,51160,39645,44052,44450,60700,64814,22266,22883,8858,31722,4337,60693,5219,6074,24282,49883,21948,40937,23131,6625,56995,47751,56295,40412,31009,21142,49559,32653,59017,28356,9121,43455,4904,2492,53909,57134,62985,33910,2784,11340,3268,26080,34678,52726,15743,36119,52962,63684,17040,2632,3969,59191,13180,23677,52573,8493,32125,31138,39740,57369,56589,11555,52449,52976,51182,7005,12282,122,11631,49923,41250,23642,34457,3570,46073,18259,63089,18230,15721,20037,45588,2728,52101,9640,61427,29157,27363,27541,39259,36627,16890,16683,51337,32384,63959,500,3094,27553,65003,12790,22689,8274,58236,20414,11745,44038,59323,45843,38416,28123,21420,21156,13051,62082,19769,49455,36487,33214,19930,61573,52381,9473,28254,1309,3398,17893,8609,36178,37183,4390,41321,40416,31672,19071,3460,5446,33820,59226,42755,53920,15108,41207,37225,46957,18710,63751,62537,36470,25472,49985,53551,34553,13812,41591,24486,7884,48408,30146,13702,11082,53681,54378,45036,45837,17007,57735,49312,18635,64027,53770,17079,3598,37300,13967,39006,194,22791,21851,33679,49913,15050,40232,3011,27554,37910,43691,33889,50247,7362,54801,15308,54217,42586,34817,36223,925,61,35479,38251,31353,23965,14171,14807,20532,31216,1062,7260,28399,56643,11458,11002,58586,56661,45031,43577,36714,4330,8395,49818,60098,52324,10867,50512]

hundred_small = [random.randint(1,65535) for _ in range(10000)]
print(len(hundred_small))
# Quick Sort
print("#----------------\nQuick Sort\n#----------------")
start = timeit.default_timer()
sorted_arr = quick_sort(hundred_small)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-16 Quick Sort Total Time:",delta,"seconds.")

#start = time.time()
#sorted_arr = quick_sort(hundred_small)
#end = time.time()
#delta = end - start
#print("100-Element 1-16 Quick Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = quick_sort(hundred_large)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-65535 Quick Sort Total Time:",delta,"seconds.")

#start = time.time()
#sorted_arr = quick_sort(hundred_large)
#end = time.time()
#delta = end - start
#print("100-Element 1-65535 Quick Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = quick_sort(five_hundred_large)
end = timeit.default_timer()
delta = end - start
print("500-Element 1-65535 Quick Sort Total Time:",delta,"seconds.")

#start = time.time()
#sorted_arr = quick_sort(five_hundred_large)
#end = time.time()
#delta = end - start
#print("500-Element 1-65535 Quick Sort Total Time:",delta,"seconds.")

# Merge Sort
print("#----------------\nMerge Sort\n#----------------")
start = timeit.default_timer()
sorted_arr = merge_sort(hundred_small)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-16 Merge Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = merge_sort(hundred_large)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-65535 Merge Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = merge_sort(five_hundred_large)
end = timeit.default_timer()
delta = end - start
print("500-Element 1-65535 Merge Sort Total Time:",delta,"seconds.")

# Insertion Sort
print("#----------------\nInsertion Sort\n#----------------")
start = timeit.default_timer()
sorted_arr = insertion_sort(hundred_small)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-16 Insertion Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = insertion_sort(hundred_large)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-65535 Insertion Sort Total Time:",delta,"seconds.")

start = timeit.default_timer()
sorted_arr = insertion_sort(five_hundred_large)
end = timeit.default_timer()
delta = end - start
print("500-Element 1-65535 Insertion Sort Total Time:",delta,"seconds.")

# Bubble Sort
print("#----------------\nBubble Sort\n#----------------")
start = timeit.default_timer()
sorted_arr = bubble_sort(hundred_small)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-16 Bubble Sort Total Time:",delta,"seconds")

start = timeit.default_timer()
sorted_arr = bubble_sort(hundred_large)
end = timeit.default_timer()
delta = end - start
print("100-Element 1-65535 Bubble Sort Total Time:",delta,"seconds")

start = timeit.default_timer()
sorted_arr = bubble_sort(five_hundred_large)
end = timeit.default_timer()
delta = end - start
print("500-Element 1-65535 Bubble Sort Total Time:",delta,"seconds")

# Python Sort
print("#----------------\nPython Sort\n#----------------")
arr = hundred_small
start = timeit.default_timer()
sorted_arr = arr.sort()
end = timeit.default_timer()
delta = end - start
print("100-Element 1-16 Bubble Sort Total Time:",delta,"seconds")

arr = hundred_large
start = timeit.default_timer()
sorted_arr = arr.sort()
end = timeit.default_timer()
delta = end - start
print("100-Element 1-65535 Bubble Sort Total Time:",delta,"seconds")

arr = five_hundred_large
start = timeit.default_timer()
sorted_arr = arr.sort()
end = timeit.default_timer()
delta = end - start
print("500-Element 1-65535 Bubble Sort Total Time:",delta,"seconds")