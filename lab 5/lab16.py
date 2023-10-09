def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5
    return average

def determine_grade(score):
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

def main():
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))
    score4 = int(input("Enter score 4: "))
    score5 = int(input("Enter score 5: "))

    average_score = calc_average(score1, score2, score3, score4, score5)
    print("Average Score:", average_score)

    print("Grades:")
    print("Score 1:", determine_grade(score1))
    print("Score 2:", determine_grade(score2))
    print("Score 3:", determine_grade(score3))
    print("Score 4:", determine_grade(score4))
    print("Score 5:", determine_grade(score5))

if __name__ == "__main__":
    main()