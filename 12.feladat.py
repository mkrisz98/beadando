string=input("Adjon meg egy stringet: ")
kisbetu=0
nagybetu=0
szam=0
egyeb=0
for i in string:
      if i.islower():
            kisbetu=kisbetu+1
      elif i.isupper():
            nagybetu=nagybetu+1
      elif i.isnumeric():
            szam=szam+1
      else:
            egyeb=egyeb+1
print("A kisbetűk száma a stringben:",kisbetu)

print("A nagybetűk száma a stringben:",nagybetu)

print("A számok száma a stringben:",szam)

print("Az egyéb karakterek száma a stringben:",egyeb)