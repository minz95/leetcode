class ProductOfNumbers:

    def __init__(self):
        self.product = []
        

    def add(self, num: int) -> None:
        if num != 1:
            self.product = [p * num for p in self.product]
        self.product.append(num)


    def getProduct(self, k: int) -> int:
        return self.product[-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)