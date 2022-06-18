

class LychrelNumbers:

    def lychrel_nums(self):
        counter = 1
        # l_numbers = []
        lychrel = []
        for i in range(1, 10000):
            calc = i+int(str(i)[::-1])
            # If not palindrome, continue
            if i != int(str(i)[::-1]):
                while True:
                    counter += 1
                    calc = calc+int(str(calc)[::-1])
                    if counter >= 100:
                        counter = 1
                        lychrel.append(i)
                        break
                    elif calc == int(str(calc)[::-1]):
                        # l_numbers.append([counter, i])
                        counter = 1
                        break

        return lychrel


l = LychrelNumbers()
print(l.lychrel_nums())
print(len(l.lychrel_nums()))
