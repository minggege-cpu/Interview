
"""
     猫狗队列 :
     * 用户可以调用add方法将cat类或dog类的 实例放入队列中；
     * 用户可以调用pollAll方法，将队列中所有的实例按照进队列 的先后顺序依次弹出；
     * 用户可以调用pollDog方法，将队列中dog类的实例按照 进队列的先后顺序依次弹出；
     * 用户可以调用pollCat方法，将队列中cat类的实 例按照进队列的先后顺序依次弹出；
     * 用户可以调用isEmpty方法，检查队列中是 否还有dog或cat的实例； 用户可以调用isDogEmpty方法，
     * 检查队列中是否有dog 类的实例； 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例

"""


class dog(object):

    def __init__(self, name):
        self.name = name    # 名字
        self.cls = 'dog'    # 类别标识
        self.count = 0      # 通过count判断猫和狗的先后顺序


class cat(object):

    def __init__(self, name):
        self.name = name
        self.cls = 'cat'
        self.count = 0


class petEnter(object):

    def __init__(self):         # 初始化两个列表存储加进来的猫和狗
        self.dogList = []
        self.catList = []
        self.count = 0          # 将赋值给变量的数值

    def add(self, item):            # 添加宠物
        if item.cls == 'dog':       # 类别为dog
            item.count = self.count
            self.count += 1             # 有元素加入count就自增1
            self.dogList.append(item)   # 加入队尾 先进先出
        elif item.cls == 'cat':
            item.count = self.count
            self.count += 1
            self.catList.append(item)
        else:
            raise Exception("必须添加 dog or cat 类")

    def pollAll(self):          # 按加入顺序弹出队列
        count = 0
        while count < self.count:   # count代表要循环的次数等于加入的次数
            if (not self.isDogEmpty()) and ( not self.isCatEmpty()):    # 猫队列和狗队列都不为空
                if self.dogList[0].count < self.catList[0].count:       # 比较队头的元素的count的值
                    dog = self.dogList.pop(0)
                    print(dog.name, dog.count)
                else:
                    cat = self.catList.pop(0)
                    print(cat.name, cat.count)
            elif (self.isDogEmpty()) and (not self.isCatEmpty()):       # 狗队列为空 猫队列不为空
                cat = self.catList.pop(0)
                print(cat.name, cat.count)
            elif (self.isCatEmpty()) and (not self.isDogEmpty()):       # 猫队列为空 狗队列不为空
                dog = self.dogList.pop(0)
                print(dog.name, dog.count)
            count += 1

    def pollDog(self):                         # 只弹出dog队列的元素
        if not self.isDogEmpty():
            dog = self.dogList.pop(0)
            print(dog.name, dog.count)
        else:
            raise Exception("没有dog类在列表里")

    def pollCat(self):                          # 只弹出cat队列的元素
        if not self.isCatEmpty():
            cat = self.catList.pop(0)
            print(cat.name, cat.count)

    def isDogEmpty(self):
        return not self.dogList

    def isCatEmpty(self):
        return not self.catList

    def isEmpty(self):
        return self.isCatEmpty() and self.isDogEmpty()


if __name__ == "__main__":
    cat1 = cat("cat1")
    cat2 = cat("cat2")
    dog1 = dog("dog1")
    dog2 = dog("dog2")
    pet = petEnter()
    pet.add(dog1)
    pet.add(cat1)
    pet.add(cat2)
    pet.add(dog2)
    pet.pollDog()
    pet.pollCat()
    pet.pollAll()
    print(pet.isEmpty())


