def gemstones(arr):
   rocks = [set(arr[i]) for i in range(len(arr))]
   gems = set.intersection(*rocks)
   return len(gems)
