#This program computes average test scores

test_scores = []

while True:
    score = input("Enter the test score: (or press ENTER to finish) ")
    if score == "":
        break
    test_scores.append(float(score))

#calculate average score

total_score = sum(test_scores)


average_score = total_score / len(test_scores)

print(f"The average test score is {average_score}")