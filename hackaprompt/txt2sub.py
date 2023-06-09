import json

dic=dict()

for i in range(1,11):
    try:
        with open(f"prompt/{i}.txt", "r") as f:
            dic[f"level_{i}"]={"prompt":f.read(),"model":"gpt-3.5-turbo"}
            if i==9:
                dic[f"level_{i}"]["model"]="FlanT5-XXL"
    except:
        dic[f"level_{i}"]={"prompt":"","model":""}

with open("submission/new_submission.json", "w") as f:
    f.write(json.dumps(dic, indent=4))