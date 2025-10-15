import enum


class Week(enum.IntEnum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7


def get_subjects(day: Week):
    match day:
        case Week.Monday:
            return "Computer Science", "Mathematics"
        case Week.Wednesday:
            return "Physics"
        case Week.Friday:
            return "Machine Learning", "Mathematics", "Computer Science"
        case _:
            return tuple()


class Filter(enum.StrEnum):
    ASC = 'ascend'
    DESC = 'descent'
    BYID = 'id'


def main():

    # IntEnum example

    d_1 = Week.Monday
    d_2 = Week.Friday
    print(d_1 == 1)              # True
    print(d_2 == 5)              # True
    print(d_1, d_2)              # 1 5
    print(type(d_1), type(d_2))  # <enum 'Week'> <enum 'Week'>
    print(d_1.name)              # Monday
    print(d_1.value)             # 1
    print(d_1 + d_2)             # 6

    subjects = get_subjects(Week.Monday)
    print(subjects)              # ('Computer Science', 'Mathematics')
    subjects = get_subjects(1)
    print(subjects)              # ('Computer Science', 'Mathematics')
    subjects = get_subjects(Week.Sunday)
    print(subjects)              # ()

    # StrEnum example

    for p in Filter:
        print(f"{p.name} = {p.value}")

    p_1 = Filter.DESC
    p_2 = Filter['ASC']
    print(p_2 == Filter.ASC)     # True
    print(p_2 < p_1)             # True
    print(p_1 + p_2)             # descentascend


if __name__ == '__main__':
    main()
