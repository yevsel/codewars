class PanDigitalMultiples:
    def concatenatedProduct(self):
        ans = []
        results = []
        for i in range(5):
            ans.append(str(9*(i+1)))
        return self.check_if_pandigital(ans)

    def check_if_pandigital(self, arr):
        nums = "123456789"
        ans2 = [int(i) for i in list(''.join(arr))]
        ans2.sort()
        return (''.join([str(i) for i in ans2]) == nums, int(''.join(arr)))


p = PanDigitalMultiples()
print(p.concatenatedProduct())
