import secrets
import hashlib
import binascii

difficulty = 24
nonce = 4256665
hash = "5e88aaba783baa3eccbaaeda1dc2a59e576c917aafba3f9176b15744420ea173"
quote = "The general principle for complexity design is this: Think locally, act locally. -- Richard P. Gabriel & Ron Goldman, Mob Software: The Erotic Life of Code"

hash_bytes = bytes.fromhex(hash)
quote_bytes = quote.encode("ascii")
hash_hex = 0
itteration = 1
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 2
hash_bytes = hash
quote = "Premature abstraction is an equally grevious sin as premature optimization. -- Keith Devens"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 9840791
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 3
hash_bytes = hash
quote = "Attitude is no substitute for competence. -- Eric S. Raymond, How to become a hacker"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 15029117
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 4
hash_bytes = hash
quote = "Nobody can make you feel inferior without your consent. -- Eleanor Roosevelt"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 39128280
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)


##itteration 5
hash_bytes = hash
quote = "The only thing a man should ever be 100% convinced of is his own ignorance. -- DJ MacLean"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 3696036
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 6
hash_bytes = hash
quote = "There are many ways to avoid success in life, but the most sure-fire just might be procrastination. -- Hara Estroff Marano."
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 6214114
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 7
hash_bytes = hash
quote = "Only two things are infinite, the universe and human stupidity. And I'm not so sure about the former. -- Albert Einstein"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 31223400
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

##itteration 8
hash_bytes = hash
quote = "A person won't become proficient at something until he or she has done it many times. In other words., if you want someone to be really good at building a software system, he or she will have to have built 10 or more systems of that type. -- Philip Greenspun"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 51528765
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)


##itteration 9
hash_bytes = hash
quote = "Functional programming is like describing your problem to a mathematician. Imperative programming is like giving instructions to an idiot. -- arcus, #scheme on Freenode"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 32996549
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)


##itteration 10
hash_bytes = hash
quote = "The trouble with the world is that the stupid are always cocksure and the intelligent are always filled with doubt. -- Bertrand Russell"
quote_bytes = quote.encode("ascii")
itteration += 1
nonce = 149507
while True:
    nonce_bytes = nonce.to_bytes(((nonce.bit_length() + 7) // 8), "big")
    hash = hashlib.sha256(hash_bytes + nonce_bytes + quote_bytes).digest()
    hash_hex = hash.hex()
    #print(hash_hex)
    if hash_hex.startswith("000000"):
        break
    else:
        nonce +=1
print(f"Itteraton: {itteration}")
print(hash_hex)
print(nonce)

