from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return """Welcome to TheRiftReport"""


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