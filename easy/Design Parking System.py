# https://leetcode.com/problems/design-parking-system/
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # self.big = big
        # self.medium = medium
        # self.small = small
        self.slot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # if carType == 1:
        #     if self.big <= 0:
        #         return False
        #     else:
        #         self.big -= 1
        #         return True
        # elif carType == 2:
        #     if self.medium <= 0:
        #         return False
        #     else:
        #         self.medium -= 1
        #         return True
        # elif carType == 3:
        #     if self.small <= 0:
        #         return False
        #     else:
        #         self.small -= 1
        #         return True
        # else:
        #     return False

        if self.slot[carType - 1] > 0:
            self.slot[carType - 1] -= 1
            return True

        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)