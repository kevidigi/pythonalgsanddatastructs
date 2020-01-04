# Bloom filter: a time and memory efficient data structure
# A 'lightweight' version of a hash table, with some drawbacks
# False positives can occur in entry lookup

import pyhash

bit_vector = [0] * 50

# Non-cryptographic hash functions (Murmur and FNV)

murmur = pyhash.murmur3_32()
fnv = pyhash.fnv1_32()

fnv_mane = fnv("Sadio Mané") % 50
fnv_willian = fnv("Willian") % 50
murmur_mane = murmur("Sadio Mané") % 50
murmur_willian = murmur("Willian") % 50

bit_vector[fnv_mane] = 1
bit_vector[fnv_willian] = 1
bit_vector[murmur_mane] = 1
bit_vector[murmur_willian] = 1

# The bits in my vector being "switched on" at the indices provided by
# hashing these two player names can be taken as an indication that
# these players are present in my team.

def isPlayerPresent(player):
    fnv_player = fnv(player) % 50
    murmur_player = murmur(player) % 50

    if bit_vector[fnv_player] == 1 and bit_vector[murmur_player] == 1:
        print("Player is present in this team... probably.")
    else:
        print("Player is not in this team!")

def __main__():
    player = input("Enter player to look up: ")
    isPlayerPresent(player)

if __name__ == __main__():
    __main__()


