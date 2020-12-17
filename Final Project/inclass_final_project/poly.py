from OO_complex import *


class Polynomial:

    def __init__(self, coefficients):
        self.coeffs = coefficients

    def add(self, other):
        temp_self = self.coeffs
        temp_other = other.coeffs
        temp_sum = []
        if len(temp_self) < len(temp_other):
            while len(temp_self) != len(temp_other):
                temp_self.insert(0, 0)
        else:
            while len(temp_self) != len(temp_other):
                temp_other.insert(0, 0)
        for i in range(len(temp_self)):
            temp_sum.append(temp_self[i] + temp_other[i])
        for i in range(len(temp_sum)):
            if temp_sum[0] == 0:
                temp_sum.pop(0)
        return Polynomial(temp_sum)

    def val(self, v):
        temp = self.coeffs[::-1]
        for i in range(len(temp)):
            temp[i] *= (v ** i)
        return sum(temp)

    def mul(self, other):
        result = [0 for _ in range((len(self.coeffs) + len(other.coeffs)) - 1)]
        for index, number in enumerate(self.coeffs):
            for index2, number2 in enumerate(other.coeffs):
                result[index + index2] += number * number2
        return Polynomial(result)

    def coeff(self, i):
        return self.coeffs[::-1][i]

    def roots(self):
        for i in range(len(self.coeffs)):
            if self.coeffs[0] == 0:
                self.coeffs.pop(0)
        if len(self.coeffs) == 2:
            return self.coeffs.coeff(2)/self.coeffs.coeff(1)
        elif len(self.coeffs) == 3:
            if ((-self.coeffs.coeff(2)))
        return self.coeffs

    def __call__(self, v):
        return self.val(v)

    def __add__(self, other):
        return self.add(other)

    def __mul__(self, other):
        return self.mul(other)

    def __str__(self):
        # temp = ""
        # reverse_poly = self.coeffs
        # reverse_poly.reverse()
        # for i in range(len(self.coeffs) - 1, -1, -1):
        #     if reverse_poly[i] > 0:
        #         temp += f"+ {reverse_poly[i]}x^{i}"
        #     elif reverse_poly[i] == 0:
        #         pass
        #     else:
        #         temp += f"- {abs(reverse_poly[i])}x^{i}"
        return " ".join([str(i) for i in self.coeffs])

