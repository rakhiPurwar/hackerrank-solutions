def serviceLane(n, cases):
          print(n,cases)
          return [min(width[i:j+1]) for i,j in cases]
