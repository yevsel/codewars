

class PanDigitalProducts:
    def sum_of_all_products(self):
        products = []
        for i in range(10000):
            for j in range(10000):
                their_product = i*j
                # Checking if they are pandigital
                if self.__check_pandigital(i, j, their_product):
                    # Appending product if multiplicand,multiplier and product are pandigital           
                    products.append(their_product)
        # Removing Duplicates and sorting
        products = list(set(products))
        return sum(products)

    def __check_pandigital(self, multiplicand, multiplier, product):
        nums = "123456789"
        ans = ''.join([str(i) for i in [multiplicand, multiplier, product]])
        ans2 = [int(i) for i in list(ans)]
        ans2.sort()
        return ''.join([str(i) for i in ans2]) == nums


p = PanDigitalProducts()
print("Sum is ", p.sum_of_all_products())




