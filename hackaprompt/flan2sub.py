import json

dic=dict()

for i in range(1,11):
    try:
        with open(f"prompt/for-flan/{i}.txt", "r") as f:
            dic[f"level_{i}"]={"prompt":f.read(),"model":"FlanT5-XXL"}
    except:
        dic[f"level_{i}"]={"prompt":"","model":""}

with open("submission/flan_submission.json", "w") as f:
    f.write(json.dumps(dic, indent=4))