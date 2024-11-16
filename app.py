from openai import OpenAI

from apikey import api_data

Model = "gpt-4o-mini"
client = OpenAI(api_key=api_data)

def Reply(question):
    completion = client.chat.completions.create(
        model=Model,
        messages=[
            {'role':"system","content":"You are a helful assistant"},
            {'role':'user','content':question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content
    return answer 

question = "Tell me some places to visit in vizag?"

ans = Reply(question)

print(ans)