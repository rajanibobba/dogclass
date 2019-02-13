from dog import Dog
from statistics import stdev

def read_dogstxt(fn):
    doglist = []
    with open(fn) as f:
        for line in f:
            attrs = line.strip().split(',')
            d = Dog(attrs[0], attrs[1], attrs[2])
            doglist.append(d)
        return doglist    

def avg_age(doglist):
   avgage = sum([int(d.age) for d in doglist])/len(doglist)
   return avgage  

def standard_dev(doglist):
    #sd = (x-avg **2/n) ** 0.5
    sd =  sum([(d.age - avg_age(doglist))**2 for d in doglist])
    #print(sd, sd/len(doglist), (sd/len(doglist)) ** 0.5)
    #print(2.8 ** 2)
    return (sd/len(doglist)) ** 0.5

d1 = Dog("Fido", 3, "Male")
d2 = Dog("Sare", 5, "Female")

file = "dogs.txt"
doglist = read_dogstxt(file)
print("Average age of dogs is ", avg_age(doglist))
print("Standard Deviation of dogs is {:.4f}".format(standard_dev(doglist)))

