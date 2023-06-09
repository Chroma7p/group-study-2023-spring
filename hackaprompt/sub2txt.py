import json
with open("submission/submission.json", "r") as f:
    data = f.read()
    data = json.loads(data)

for i in range(1,11):
    level=data["level_"+str(i)]
    if level["model"]!="":
        with open(f"prompt/{i}.txt", "w") as f:
            f.write(level["prompt"])
