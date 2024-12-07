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

with open("output.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(call_chatgpt(f"Summarise this {content}"))