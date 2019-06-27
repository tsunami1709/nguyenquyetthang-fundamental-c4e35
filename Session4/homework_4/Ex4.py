q1= {
    "question": """Answer the following algebra question:
If x = 8, then what is the valuevalue of 4(x+3) ?""",
    "1":35,
    "2":36,
    "3":40,
    "4":44,
    "answer": "4"
}
q2= {
    "question": """Estimate this answeranswer (exact caculationcaculation not needed):
Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the meanmean?""",
    "1": "About 55",
    "2": "About 65",
    "3": "About 75",
    "4": "About 85",
    "answer":"2"
}

final = 0
q = [q1,q2]
for i in range (len(q)):
    for k,v in q[i].items():
        if k == "question":
            print(v)
            continue
        if k == "answer":
            continue
        print(k, end =". ")
        print(v)
    a = input("Your choice: ")
    if a == q[i]["answer"]:
        print("Bingo")
        final += 1
    else:
        print(":(")

print("Your correct answer", final, "out of", len(q), "questions")