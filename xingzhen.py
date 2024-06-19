from functools import reduce
answer_set = ["A", "B", "C", "D"]

class question:
    def __init__(self, requirement):
        self.requirement = requirement
        self.answer = None
    
    def test(self):
        return self.requirement(self.answer)

questions = []

def compare(*toCompare):
    for x in range(0, len(toCompare)-1):
        if questions[toCompare[x]-1].answer != questions[toCompare[x+1]-1].answer:
            return False
    return True

def compareByAnswer(ans, a,b,c,d):
    if ans == "A":
        return compare(*a)
    elif ans == "B":
        return compare(*b)
    elif ans == "C":
        return compare(*c)
    elif ans == "D":
        return compare(*d)
    else:
        print("Invalid answer")

def q2(ans):
    if ans == "A":
        ans = "C"
    elif ans == "B":
        ans = "D"
    elif ans == "C":
        ans = "A"
    elif ans == "D":
        ans = "B"
    return ans == questions[4].answer

def q7(ans):
    # count questions answers
    count = [0, 0, 0, 0]
    for q in questions:
        count[answer_set.index(q.answer)] += 1
    lowest = count.index(min(count))
    # print(count,lowest)
    answer_table = {
        "A": "C",
        "B": "B",
        "C": "A",
        "D": "D"
    }
    return answer_set[lowest] == answer_table[ans]

def q8(ans):
    answer_table = {
        "A": 7,
        "B": 5,
        "C": 2,
        "D": 10
    }
    ans = questions[answer_table[ans]-1].answer
    next = (answer_set.index(ans)+1)%4
    prev = (answer_set.index(ans)-1)%4
    return questions[1-1].answer != answer_set[next] and questions[1-1].answer != answer_set[prev]

def q9(ans):
    flag = not compare(1, 6)
    answer_table = {
        "A": 6,
        "B": 10,
        "C": 2,
        "D": 9
    }
    ans = answer_table[ans]
    return flag == compare(ans, 5)

def q10(ans):
    count = [0, 0, 0, 0]
    for q in questions:
        count[answer_set.index(q.answer)] += 1
    lowest = min(count)
    highest = max(count)
    answer_table = {
        "A": 3,
        "B": 2,
        "C": 4,
        "D": 1
    }
    ans = answer_table[ans]
    return ans == highest - lowest

questions = [
    question(lambda x: True),
    question(lambda x: q2(x)),
    question(lambda x: compareByAnswer(x, (6,2,4), (3,2,4), (3,6,4), (3,6,2))), 
    question(lambda x: compareByAnswer(x, (1,5), (2,7), (1,9), (6,10))),
    question(lambda x: compareByAnswer(x, (5,8), (4,5), (9,5), (7,5))),
    question(lambda x: compareByAnswer(x, (2,4,8), (1,6,8), (3,10,8), (5,0,8))),
    question(lambda x: q7(x)),
    question(lambda x: q8(x)),
    question(lambda x: q9(x)),
    question(lambda x: q10(x))    
]

answer = [0]*len(questions)
def setAnswer():
    for i in range(0, len(answer)):
        questions[i].answer = answer_set[answer[i]]

def incrementAnswer():
    flag = True
    index = 0
    while flag and index < len(answer):
        answer[index] += 1
        if answer[index] == 4:
            answer[index] = 0
            index += 1
        else:
            flag = False

for i in range(0, 4**len(questions)):
    setAnswer()
    flag = reduce(lambda x, y: x and y, [q.test() for q in questions])
    if flag:
        print(list(map(lambda x: answer_set[x], answer)))
        # break
    # else:
    incrementAnswer()

# answer = [2]*len(questions)
# setAnswer()
# questions[0].answer = "A"
# questions[1].answer = "A"
# questions[2].answer = "A"
# questions[3].answer = "B"
# questions[4].answer = "D"
# questions[5].answer = "B"


# questions[9].answer = "A"


# print(questions[9].test())
# for q in questions:
    # print(q.test())


