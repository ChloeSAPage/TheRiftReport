from openai import OpenAI
client = OpenAI()


def call_chatgpt(content, message):
    completion = client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": message },
            {
                "role": "user",
                "content": content
            }
        ]
    )
    message = completion.choices[0].message.content
    return message

# with open("output3.txt", "r", encoding="utf-8") as file:
#     content = file.read()

# print(call_chatgpt(f"Summarise this {content}"))