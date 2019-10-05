import time
class PromotionalGoods:
    def __init__(self, discount, product_name, the_original_price, promotion_price):
        self.discount = discount
        self.product_name = product_name
        self.the_original_price = the_original_price
        self.promotion_price = promotion_price

    def __del__(self):
        pass


def printList(arr):
    for i in range(len(arr)):
        print(arr[i],end=" ")
    print()


def sorting_by_merge_sort_at_the_discount(array):
    if len(array) > 1:
        mid = len(array) // 2
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        sorting_by_merge_sort_at_the_discount(leftHalf)
        sorting_by_merge_sort_at_the_discount(rightHalf)

        elementsOfLeftHalf = elementsOfRightHalf = 0
        step = 0

        while elementsOfLeftHalf < len(leftHalf) and elementsOfRightHalf < len(rightHalf):
            if leftHalf[elementsOfLeftHalf] < rightHalf[elementsOfRightHalf]:
                array[step] = leftHalf[elementsOfLeftHalf]
                elementsOfLeftHalf += 1
            else:
                array[step] = rightHalf[elementsOfRightHalf]
                elementsOfRightHalf += 1
            step += 1

        while elementsOfLeftHalf < len(leftHalf):
            array[step] = leftHalf[elementsOfLeftHalf]
            elementsOfLeftHalf += 1
            step += 1

        while elementsOfRightHalf < len(rightHalf):
            array[step] = rightHalf[elementsOfRightHalf]
            elementsOfRightHalf += 1
            step += 1
    return array


def sorting_by_bubble_at_the_original_price_of_descending(bad_list):
    length = len(bad_list) - 1
    sorted = False
    counter = 0
    swap = 0
    start_time = time.time()
    while not sorted:
        sorted = True
        for element in range(length):
            if bad_list[element] < bad_list[element+1]:
                counter += 1
                sorted = False
                hold = bad_list[element]
                bad_list[element] = bad_list[element+1]
                bad_list[element+1] = hold
                swap += 1

    print("time", start_time)
    print("counter", counter)
    print("swap", swap)
    return (bad_list)



kefir = PromotionalGoods(20,"Kefir",99, 80)
milk = PromotionalGoods(30,"Kefir5",2, 70)
apple = PromotionalGoods(40,"Kefir4",5, 60)
bread = PromotionalGoods(24,"Kefir3",9, 76)
lemon = PromotionalGoods(25,"Kefir2",10, 75)
blackberry = PromotionalGoods(35,"Kefir1",11, 65)
goods = [kefir, milk, apple, bread, lemon, blackberry]

goods_discount = [kefir.discount,milk.discount,apple.discount,
                  bread.discount,lemon.discount,blackberry.discount]
goods_the_original_price = [kefir.the_original_price, milk.the_original_price, apple.the_original_price,
                  bread.the_original_price, lemon.the_original_price, blackberry.the_original_price]

print('The original price was sorted by the bubble method:')

print(sorting_by_bubble_at_the_original_price_of_descending(goods_the_original_price))
print()

print('Merge sort for a discount')

print(sorting_by_merge_sort_at_the_discount(goods_discount))

