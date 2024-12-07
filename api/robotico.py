from openai import OpenAI
client = OpenAI()

def call_chatgpt(content):
    completion = client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": content
            }
        ]
    )
    message = completion.choices[0].message
    return message

# print(call_chatgpt("Summarise this website https://www.leagueoflegends.com/en-gb/news/game-updates/patch-14-23-notes/"))