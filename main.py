class AssociationRules:
    def __init__(self, items):
        self.items = items

    def support(self, item, item2=None):
        if item2 is not None:
            return self.__support2__(item, item2)
        count = 0
        for cart in self.items:
            if item in cart:
                count += 1
        return count / len(self.items)

    def __support2__(self, item1, item2):
        both = 0
        for cart in self.items:
            if item1 in cart and item2 in cart:
                both += 1
        return both / len(self.items)

    def confidence(self, item1, item2):
        return self.__support2__(item1,item2) / self.support(item1)

    def lift(self, item1, item2):
        return self.__support2__(item1,item2) / (self.support(item1) * self.support(item2))


carts = [[1, 2, 3, 4, 5], [1, 2, 4, 5], [1, 2, 5], [2, 3, 4, 5], [2, 3, 5], [3, 4, 5], [2, 4]]
check = AssociationRules(carts)
# print(check.support(5))
# print(check.confidence(2,3))
# print(check.lift(2,3))
# print(check.lift(1,4))
# print(check.lift(2,5))

carts2 = [["apple", "banana", "cheese"], ["bagel", "apple", "banana", "bottle", "pepper"],
          ["bagel", "bottle", "fish", "pizza", "banana"], ["pizza", "cheese", "avocdo"],
          ["fish", "beer", "bagel", "pepper"],
          ["pizza", "avocdo", "pepper"], ["banana", "bottle", "pizza"], ["cheese", "beer", "pepper", "bagel", "banana"],
          ["banana", "bottle", "pizza", "fish"]]

check2 = AssociationRules(carts2)

print(check2.support("pizza"))
print(check2.support("pizza", "bagel"))
print(check2.lift("bagel","apple"))