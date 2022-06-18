
class PythagoreanTriplet:
    def triples(self):
        ans = []
        for i in range(500):
            for j in range(500):
                for k in range(500):
                    if i < j < k and i**2+j**2 == k**2:
                        ans.append([i, j, k])
        for i in ans:
            if sum(i) == 1000:
                return i


p = PythagoreanTriplet()
print(p.triples())
