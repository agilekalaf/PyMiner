import hashlib
import sys

sys.setrecursionlimit(3000)

def find_nonce(int1):
    transaction = b"Pay me Greg. "
    nstr = str(int1).zfill(7)
    nonce_value = nstr.encode('ascii')
    m = hashlib.sha256()
    m.update(transaction)
    m.update(nonce_value)
    if m.hexdigest()[0] == "0" and m.hexdigest()[1] == "0" and m.hexdigest()[2] == "0":
        print(nonce_value)
        print(m.hexdigest())
        print(m.hexdigest()[1])
        return nonce_value
    else:
        int1 += 1
        print("try again with " + str(int1))
        find_nonce(int1)

print(find_nonce(1))
