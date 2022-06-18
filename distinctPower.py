

class DistintPower:
    def __init__(self, a_interval, b_interval):
        self.a = [i for i in range(a_interval[0], a_interval[1]+1)]    
        self.b = [i for i in range(b_interval[0], b_interval[1]+1)]     

    def number_of_terms(self):
        res1 = []
        for a in self.a:
            for b in self.b:
                res1.append(a**b)

        # Removing Duplicates
        list(set(res1)).sort()

        return len(res1)


d = DistintPower([2, 100], [2, 100])
print("There are", d.number_of_terms(), "distinct powers")  


# >> "There are 9801 distinct powers"

