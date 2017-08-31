def main():
    score = float(input("Enter score: "))
    score_outcome = get_score(score)
    print("Your score is {}".format(score_outcome))



def get_score(score):
    if score < 0:
        score = "Invalid score"
        return score
    elif score > 100:
        score = "Amazing"
        return score
    elif score > 90:
        score = "Excellent"
        return score
    elif score > 50:
        score = "Passable"
        return score
    else:
        score = "Bad"
        return score
main()