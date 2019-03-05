from collections import deque


class Animal:
    def __init__(self, name):
        self.name = name
        self.order = None


class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super(Cat, self).__init__(name)


class AnimalQueue:
    def __init__(self):
        self.cats = deque()
        self.dogs = deque()
        self.order = 0

    def enqueue(self, animal: Animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.appendleft(animal)

        elif isinstance(animal, Cat):
            self.cats.appendleft(animal)

    def dequeue(self):
        cat, dog = None, None
        # no cats
        if self.cats:
            cat = self.deque_cat()
        # no dogs
        if self.dogs:
            dog = self.deque_dog()

        # no cat
        if not cat:
            return dog
        # no dog
        if not dog:
            return cat

        if cat.order <= dog.order:
            # put dog back as the oldest in queue which means append to the right
            self.dogs.append(dog)
            return cat
        else:
            self.cats.append(cat)
            return dog

    def deque_cat(self):
        return self.cats.pop()

    def deque_dog(self):
        return self.dogs.pop()


maggie = Cat("maggie")
honey = Dog("honey")
macy = Cat("macy")
gracey = Dog("gracey")

shelter = AnimalQueue()

shelter.enqueue(maggie)
shelter.enqueue(honey)
shelter.enqueue(macy)
shelter.enqueue(gracey)

print(shelter.dequeue().name)
print(shelter.deque_cat().name)
print(shelter.deque_dog().name)
print(shelter.deque_dog().name)
