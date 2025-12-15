""""
- Lightweight version of hash table. Efficient insertions and loopkups

- More space efficient than hash table, but comes at a cost of having "false positives" for entry lookup

- Probabilistic data structure

Uses - fast lookups and insertions. Space constraints. Don't care if data structure sometimes indicates an item is present when in fact it is not.

Example : I run a website and want to keep track of IP addresses that are blocked. I don't particularly care if a blocked IP address is occasionally able to access my website, but I do care if someone on the whitelist is unable to access the site. For more examples, visit Wikipedia.

bit vector is a list of bits
"""

import pyhash

bit_vector = [0] * 20

# Non cryptographic hash functions (Murmur and FNV)
fnv = pyhash.fnv1_32()
murmur = pyhash.murmur3_32()

# Calculate the output of FNV and Murmur hash functions for Pikachu and Charmander
fnv_pika = fnv("Pikachu") % 20
fnv_char = fnv("Charmander") % 20

murmur_pika = murmur("Pikachu") % 20
murmur_char = murmur("Charmander") % 20

bit_vector[fnv_pika] = 1
bit_vector[murmur_pika] = 1

bit_vector[fnv_char] = 1
bit_vector[murmur_char] = 1

# A wild Bulbasaur appears!
fnv_bulb = fnv("Bulbasaur") % 20
murmur_bulb = murmur("Bulbasaur") % 20