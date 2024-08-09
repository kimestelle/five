import random
from typing import List
from pathlib import Path

# Frequencies as an array where the index corresponds to the letter 'a' to 'z'
frequencies = [
    0.08167,  # a
    0.01492,  # b
    0.02782,  # c
    0.04253,  # d
    0.12702,  # e
    0.02228,  # f
    0.02015,  # g
    0.06094,  # h
    0.06966,  # i
    0.00153,  # j
    0.00772,  # k
    0.04025,  # l
    0.02406,  # m
    0.06749,  # n
    0.07507,  # o
    0.01929,  # p
    0.00095,  # q
    0.05987,  # r
    0.06327,  # s
    0.09056,  # t
    0.02758,  # u
    0.00978,  # v
    0.02360,  # w
    0.00150,  # x
    0.01974,  # y
    0.00074   # z
]

indices = [
    {'letter': 'a', 'start': 0, 'end': 295},
    {'letter': 'b', 'start': 296, 'end': 727},
    {'letter': 'c', 'start': 728, 'end': 1167},
    {'letter': 'd', 'start': 1168, 'end': 1478},
    {'letter': 'e', 'start': 1479, 'end': 1607},
    {'letter': 'f', 'start': 1608, 'end': 1925},
    {'letter': 'g', 'start': 1926, 'end': 2204},
    {'letter': 'h', 'start': 2205, 'end': 2443},
    {'letter': 'i', 'start': 2444, 'end': 2517},
    {'letter': 'j', 'start': 2518, 'end': 2590},
    {'letter': 'k', 'start': 2591, 'end': 2681},
    {'letter': 'l', 'start': 2682, 'end': 2952},
    {'letter': 'm', 'start': 2953, 'end': 3250},
    {'letter': 'n', 'start': 3251, 'end': 3368},
    {'letter': 'o', 'start': 3369, 'end': 3476},
    {'letter': 'p', 'start': 3477, 'end': 3862},
    {'letter': 'q', 'start': 3863, 'end': 3901},
    {'letter': 'r', 'start': 3902, 'end': 4169},
    {'letter': 's', 'start': 4170, 'end': 4893},
    {'letter': 't', 'start': 4894, 'end': 5269},
    {'letter': 'u', 'start': 5270, 'end': 5344},
    {'letter': 'v', 'start': 5345, 'end': 5453},
    {'letter': 'w', 'start': 5454, 'end': 5681},
    {'letter': 'x', 'start': 5682, 'end': 5685},
    {'letter': 'y', 'start': 5686, 'end': 5732},
    {'letter': 'z', 'start': 5733, 'end': 5756}
]

def get_next_word(letters: List[str]) -> str:
    file_path = Path("server/five.txt").resolve()
    filtered_frequencies = {letter: frequencies[ord(letter) - ord('a')] for letter in letters}
    total_frequency = sum(filtered_frequencies.values())
    normalized_frequencies = {letter: freq / total_frequency for letter, freq in filtered_frequencies.items()}
    weighted_letters = list(normalized_frequencies.keys())
    weights = list(normalized_frequencies.values())
    chosen_letter = random.choices(weighted_letters, weights=weights, k=1)[0]
    for entry in indices:
        if entry['letter'] == chosen_letter:
            start = entry['start']
            end = entry['end']
            random_index = random.randint(start, end)
            with open(file_path, 'r') as file:
                words = file.readlines()
                return words[random_index].strip()
    return "No valid word found"
