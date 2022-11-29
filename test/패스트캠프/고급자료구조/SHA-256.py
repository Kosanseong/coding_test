import sys
import hashlib
sys.stdin = open("input.txt", "rt")

s = input()
encodeS = s.encode()

print(hashlib.sha256(encodeS).hexdigest())
