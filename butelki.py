print('Numer zatrutej butelki to:')
import random
zatruta = random.randint(1,1000)

print(zatruta)

ile = 0


for i in range(0,10):
    print("\n \n Osoba numer", i+1, "pije z butelek:")
    j=2**i
    while j <=1000:
        for k in range(j,min(j+2**i,1001)):
            print(k, end=" ")
            if k==zatruta:
                ile+=1
        j+=2**(i+1)

print("\n\n Z zatrutej butelki piło", ile, "osób")