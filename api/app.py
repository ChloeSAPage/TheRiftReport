from flask import Flask, request
from robotico import call_chatgpt
from prompts import top_lane_prompt, jungle_prompt, mid_lane_prompt, adc_prompt, support_prompt

app = Flask(__name__)

role_prompts = {
    "top": top_lane_prompt,
    "jungle": jungle_prompt,
    "mid": mid_lane_prompt,
    "adc": adc_prompt,
    "support": support_prompt
}

with open("output3.txt", "r", encoding="utf-8") as file:
    content = file.read()


@app.route('/')
def index():
    return """Welcome to TheRiftReport"""

@app.route('/get_patch_notes/<role>')
def get_patch_notes(role):
    prompt = role_prompts.get(role)
    response = call_chatgpt(prompt, content)
    return response

# @app.route('/get-recipes')
# def call_get_recipes():
#     result = get_recipes()
#     return result


# @app.route('/get-recipe/<name>')
# def call_get_recipe(name):
#     result = get_recipe(name)
#     return result


# @app.route('/submit-recipe', methods=["PUT"])
# def call_insert_recipe():
#     recipe = request.get_json()
#     code = insert_recipe(recipe)
#     return code


if __name__ == '__main__':
    app.run(debug=True, port=5001)