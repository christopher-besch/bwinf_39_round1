from random import choice


def main():
    amount_students = 1000
    amount_wishes = 100
    print(amount_students)
    for student_number in range(1, amount_students + 1):
        wishes = []
        for _ in range(amount_wishes):
            while str(wish := choice(range(1, amount_students + 1))) in wishes:
                pass
            wishes.append(str(wish))
        print(" ".join(wishes))


if __name__ == "__main__":
    main()
