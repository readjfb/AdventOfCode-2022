def day2_v1():
    with open("day2_input.txt", "r") as f:
        puzzle_input = f.read().splitlines()

    # Part 1

    mapping_dict = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    scoring_shape = {"Rock": 1, "Paper": 2, "Scissors": 3}
    scoring_outcome = {"Lose": 0, "Win": 6, "Draw": 3}

    total_score = 0

    for turn in puzzle_input:
        elf, human = turn.split(" ")

        total_score += scoring_shape[mapping_dict[human]]

        if mapping_dict[human] == mapping_dict[elf]:
            total_score += scoring_outcome["Draw"]

        elif mapping_dict[human] == "Rock" and mapping_dict[elf] == "Scissors":
            total_score += scoring_outcome["Win"]

        elif mapping_dict[human] == "Paper" and mapping_dict[elf] == "Rock":
            total_score += scoring_outcome["Win"]

        elif mapping_dict[human] == "Scissors" and mapping_dict[elf] == "Paper":
            total_score += scoring_outcome["Win"]

        else:
            total_score += scoring_outcome["Lose"]

    print(f"Part 1: {total_score}")

    target_dict = {"X": "Lose", "Y": "Draw", "Z": "Win"}
    losing_dict = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    winning_dict = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}

    total_score = 0
    for turn in puzzle_input:
        opponent, target = turn.split(" ")

        if target_dict[target] == "Lose":
            total_score += scoring_shape[losing_dict[mapping_dict[opponent]]]
            total_score += scoring_outcome["Lose"]

        elif target_dict[target] == "Win":
            total_score += scoring_shape[winning_dict[mapping_dict[opponent]]]
            total_score += scoring_outcome["Win"]

        else:
            total_score += scoring_shape[mapping_dict[opponent]]
            total_score += scoring_outcome["Draw"]

    print(f"Part 2: {total_score}")


if __name__ == "__main__":
    day2_v1()
