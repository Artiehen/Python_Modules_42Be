import sys


def main():
    nsc = "No scores provided. Usage: python3"
    print("=== Player Score Analytics ===")
    pcount = len(sys.argv) - 1
    try:
        score_list = [int(arg) for arg in sys.argv[1:]]
        if len(sys.argv) == 1:
            raise IndexError
        print(f"Total players: {pcount}")
        print(f"Scores processed: {score_list}")
        print(f"Total Score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / pcount}")
        print(f"High Score: {max(score_list)}")
        print(f"Low Score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}")

    except IndexError:
        print((f"{nsc} {sys.argv[0]} <Score1> <Score2>..."))
    except ValueError:
        print("Invalid Score provided! Please check scores and retry.")


if __name__ == "__main__":
    main()
