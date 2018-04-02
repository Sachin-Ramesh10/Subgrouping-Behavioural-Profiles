from bitarray import bitarray
import mmh3


class bloomFilter:

 def __init__(self, arrsize, hCount):
        self.arrsize = arrsize
        self.hCount = hCount
        self.bitArray = bitarray(arrsize)
        self.bitArray.setall(0)
        self.fp = 0
        self.m =[]

 def add(self, string):
    self.m.append(string)
    for seed in range(self.hCount):
      i =  mmh3.hash(string, seed) % self.arrsize
      self.bitArray[i] = 1 


 def filter(self, string):
        miss = False
        for seed in range(self.hCount):
            result = mmh3.hash(string, seed) % self.arrsize 
            if self.bitArray[result] == 0:
                miss = True
            if (miss == True):
                break
            continue
        return miss

def main():
  count = 0
  s = 0
  bF = bloomFilter(3970301,7)
  missCount = 0
  file_name = "listed_username_30.txt"
  with open(file_name, "r") as words:
   for word in words:
    bF.add(word)
    s = s + 1
  print("Completed adding {} elements!".format(s))

  file_name = "listed_username_365.txt"
  with open(file_name, "r") as words:
   for word in words:
    count += 1
    miss = bF.filter(word)
    if ( miss == True):
      missCount+= 1
  print("Number of misscounts {}".format(missCount))
  print("Total number of elements {}".format(count))

  percentage = ((count - missCount)/float(count))*100
  print("False positive rate is {}%".format(percentage))
  
if __name__ == "__main__":
    main()
