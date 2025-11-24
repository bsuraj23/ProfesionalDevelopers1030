def test_func(arg1, arg2):
    dev = arg1
    per = arg2
    output = dev + " " + per
    print(output)
    return output

T = test_func('Pavithra', 'is going to python developer') 


class Bank:
    def __init__(self):
        self.__balance = 1000   # private

    def get_balance(self):      # getter
        return self.__balance

b = Bank()
print(b.get_balance())   # ✔ prints 1000
