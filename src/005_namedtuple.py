from collections import namedtuple


def main():
    Person = namedtuple("Person", "name lastname age job")

    p_1 = Person("Ivan", "Ivanov", 34, "Python Developer")

    print(p_1)  # Person(name='Ivan', lastname='Ivanov', age=34, job='Python Developer')
    print(p_1.job)  # Python Developer
    print(p_1[3])   # Python Developer
    print(p_1[-1])  # Python Developer

    # p_1.age = 45  # AttributeError: can't set attribute

    for i in p_1:
        print(i, end=' ')  # Ivan Ivanov 34 Python Developer
    print()

    print(*p_1)            # Ivan Ivanov 34 Python Developer

    print(issubclass(Person, tuple))  # True
    print(p_1.index("Ivan"))          # 0
    print(p_1.index(34))              # 2
    print(p_1.count("Ivan"))          # 1
    # {'name': 'Ivan', 'lastname': 'Ivanov', 'age': 34, 'job': 'Python Developer'}
    print(p_1._asdict())
    # new created object -> Person(name='Ivan', lastname='Ivanov', age=30, job='Python Developer')
    print(p_1._replace(age=30))
    # new created copy -> Person(name='Stepan', lastname='Tur', age=50, job='Driver')
    p_2 = p_1._make(["Stepan", "Tur", 50, "Driver"])
    print(p_2)
    # ('Ivan', 'Ivanov', 34, 'Python Developer', 'Stepan', 'Tur', 50, 'Driver')
    print(p_1 + p_2)
    print(p_1 + (2, 4))  # ('Ivan', 'Ivanov', 34, 'Python Developer', 2, 4)

    # Invalid field names will be renamed
    C = namedtuple("ClassC", "arg class for", rename=True)
    print(C)          # <class '__main__.ClassC'>
    print(C._fields)  # ('arg', '_1', '_2')

    BMW = namedtuple("Car", ["model", "dist", "weight", "price"])
    print(BMW)  # <class '__main__.Car'>

    bmw_1 = BMW("X3", 100, 1.2, 3_200)
    bmw_2 = BMW("X5", 6201, 1.5, 5_100)

    print(bmw_1)  # Car(model='X3', dist=100, weight=1.2, price=3200)
    print(bmw_2)  # Car(model='X5', dist=6201, weight=1.5, price=5100)


if __name__ == '__main__':
    main()
