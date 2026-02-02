def list_comprehension():
    player1 = ["alice", 2300]
    player2 = ["bob", 1800]
    player3 = ["charlie", 2150]
    player4 = ["diana", 2050]
    players = [player1, player2, player3, player4]
    # scores = [2300, 1800, 2150, 2050]
    first = True
    # print("", end="")
    for p in players:
        if not first:
            print(", ", end="")
        print(f"'{p}'", end="")
        first = False
    print("")


def main():
    print("=== Game Analytics Dashboard ===")
    list_comprehension()
    print("=== Game Analytics Dashboard ===")



if __name__ == "__main__":
    main()


ef list_comprehension():
    players = ["alice", 2300, "bob", 1800, "chalie", 2150, "diana", 2050]
    scores = [2300, 1800, 2150, 2050]
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 2000
    slice = [s for s in scores if s > n]
    print(slice)
    first = True
    print("[", end="")
    for p in players:
        if not first:
            print(", ", end="")
        print(f"'{p}'", end="")
        first = False
    print("]")


def main():
    print("=== Game Analytics Dashboard ===\n")    
    print("=== List comprehension examples ===")
    list_comprehension()



if __name__ == "__main__":
    main()


