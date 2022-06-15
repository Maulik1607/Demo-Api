import pandas as pd

file_loc = r"C:\Users\01182\Desktop\app\data\KnowledgeBaseReplica.xlsx"

df = pd.read_excel(file_loc)

questions =[]
answers = []

for i in range(len(df)):
    questions.append(df.iloc[i][0])
    answers.append(df.iloc[i][1])

print(questions)
print(answers)



que_ans = {"bot":[]}
for i in range(len(questions)):
    que_ans["bot"].append({"Question":questions[i],"answer":answers[i]})
print(que_ans)

