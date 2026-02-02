import random

def show_welcome():
    print("======================")
    print("   QUIZ BATTLE GAME")
    print("======================")


def get_players():
    players = []

    num = int(input("จำนวนผู้เล่น (2-4): "))

    for i in range(num):
        name = input("ชื่อผู้เล่นคนที่ " + str(i + 1) + ": ")
        players.append(name)

    return players


def load_questions():
    questions = [
        ["Python เป็นภาษาอะไร?",
         ["Low-level", "High-level", "Assembly", "Machine"],
         2],

        ["คำสั่งใดใช้แสดงผล?",
         ["echo", "print", "show", "output"],
         2],

        ["โครงสร้างข้อมูลใดเป็นลำดับ?",
         ["Set", "Dict", "List", "None"],
         3],

        ["ไฟล์ Python ลงท้ายด้วยอะไร?",
         [".java", ".py", ".cpp", ".html"],
         2]
    ]

    return questions


def ask_question(player, question):
    print("\nตาของ:", player)
    print(question[0])

    choices = question[1]
    correct = question[2]

    for i in range(4):
        print(str(i + 1) + ".", choices[i])

    answer = int(input("เลือกคำตอบ (1-4): "))

    if answer == correct:
        print("ถูกต้อง!")
        return 1
    else:
        print("ผิด!")
        return 0


def show_scores(players, scores):
    print("\nคะแนนปัจจุบัน")
    for i in range(len(players)):
        print(players[i], ":", scores[i])


def main():
    show_welcome()

    players = get_players()
    scores = []

    for i in range(len(players)):
        scores.append(0)

    questions = load_questions()
    random.shuffle(questions)
    rounds = len(questions)

    for i in range(rounds):
        print("\n----- รอบที่", i + 1, "-----")
        for j in range(len(players)):
            point = ask_question(players[j], questions[i])
            scores[j] = scores[j] + point
            show_scores(players, scores)

    print("\n===== จบเกม =====")
    max_score = max(scores)
    winner_index = scores.index(max_score)
    print("ผู้ชนะคือ", players[winner_index])



main()
