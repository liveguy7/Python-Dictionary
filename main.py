
class Dictionary(dict):

  def __missing__(self, key):
    return 0

ptr = Dictionary()
ptr['one']
ptr['one'] += 1
ptr['two']
ptr['two'] += 2
ptr['three']
ptr['three'] += 3

print(ptr)




