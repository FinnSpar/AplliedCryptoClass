import secrets
import hashlib
import binascii

#givens, plus the random a by me
g = 5
p = 233000556327543348946447470779219175150430130236907257523476085501968599658761371268535640963004707302492862642690597042148035540759198167263992070601617519279204228564031769469422146187139698860509698350226540759311033166697559129871348428777658832731699421786638279199926610332604408923157248859637890960407
a = 3129596338919545659221396494219063683305387818809965183098351028897741952356147830947093642636012303588534543054566010274312933009817345693785555196355307498812801388998112612863728629696515017395364369585716110201792609819853520440618220339741942967072723
netid = "bjy819"

#calculate public key
publicKeyA = pow(g, a, p)
# print(publicKeyA)

# next step, new given informaiton
password = "preenvironmental"
salt = "c72f4b07"

#calculate/convert the bytes for hash
passbytes = password.encode("ascii")
saltbytes = bytes.fromhex(salt)
result = saltbytes + passbytes

#hash password, do the opperation 1000 times
x = result
for _ in range(1000):
    x = hashlib.sha256(x).digest()
intX = int.from_bytes(x, byteorder="big")

###print(intX)

#next step, new given, calculate public key, k, and shared key
B = 188782252172127376583423573213731008388739790223460677769336983769750412987797047454878976828682024634444198481207679388355254112535793015466671164728552005775331250903186804591884359954733696367576293611117245645832376781829905766659778625903866290188112717446810267607288926898589895147411612530677254805718
lengthp = (p.bit_length() + 7) // 8  
lengthg = (g.bit_length() + 7) // 8  
pbytes = p.to_bytes(lengthp, "big")
gbytes = g.to_bytes(lengthg, "big")
#calculate k
k = hashlib.sha256(pbytes + gbytes).digest()
intK = int.from_bytes(k, byteorder="big")

###print(intK)

#now calculate  g^b (public key)
publicKeyB =(B - intK * pow(g, intX, p)) % p

###print(publicKeyB)

#calculate u
lengthA = (publicKeyA.bit_length() + 7) // 8  
lengthB = (publicKeyB.bit_length() + 7) // 8  
Abytes = publicKeyA.to_bytes(lengthA, "big")
Bbytes = publicKeyB.to_bytes(lengthB, "big")
u = hashlib.sha256(Abytes + Bbytes).digest()
intU = int.from_bytes(u, byteorder="big")

##print(intU)

#calculate shared key
sharedKey= pow(publicKeyB, a + (intU * intX), p)
##print(sharedKey)


#calculate m1 and m2

#calculate hashed p and g
phash = hashlib.sha256(pbytes).digest()
ghash = hashlib.sha256(gbytes).digest()
phshint = int.from_bytes(phash, byteorder="big")
ghashint = int.from_bytes(ghash, byteorder="big")
oredPG = phshint ^ ghashint
lengthPG = (oredPG.bit_length() + 7) // 8  
PG = oredPG.to_bytes(lengthPG, "big")

#prepare other elements for M1
IDbytes = netid.encode("ascii")
IDHash = hashlib.sha256(IDbytes).digest()
#IDint = int.from_bytes(IDHash, byteorder="big")

sharedkeylength = (sharedKey.bit_length() + 7) // 8 
sharedKeyBytes = sharedKey.to_bytes(sharedkeylength, "big")

publicKeyALength = (publicKeyA.bit_length() + 7) // 8 
publicKeyBLength = (publicKeyB.bit_length() + 7) // 8 
publicKeyAbytes = publicKeyA.to_bytes(publicKeyALength, "big")
publicKeyBbytes = publicKeyB.to_bytes(publicKeyBLength, "big")

M1 = hashlib.sha256(PG + IDHash + saltbytes + publicKeyAbytes + publicKeyBbytes + sharedKeyBytes).digest()
M1hex = M1.hex()

## print(M1hex)

M2 = hashlib.sha256(publicKeyAbytes + M1 + sharedKeyBytes).digest()
M2hex = M2.hex()
print(M2hex)
