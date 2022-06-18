questions = ["Whats your name: ", "Whats your age: ", "Where were you born: "]
answers = ["Selasi", "23", "Nungua"]
user = []
mark = 0
for i in range(len(questions)):
    res = input(questions[i])
    user.append(res)
for i in range(len(answers)):
    if user[i].lower() == answers[i].lower():
        mark += 1

print(f"You had {mark}/{len(answers)}")
