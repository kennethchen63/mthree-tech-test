from flask import Flask, request, jsonify
from permutations.permutation import find_permutations
app = Flask(__name__)

@app.route('/permutations', methods=['POST'])
def permutations():
    # Get body
    try:
        data = request.get_json()
    except:
    # If no body return 400
        return jsonify({"error": "Missing 'string' in JSON body."}), 400
    # If no string in body
    if ("string" not in data):
        return jsonify({"error": "Missing valid 'string' in JSON body."}), 400

    string_to_permuate = data["string"]
    perms = find_permutations(string_to_permuate)
    return jsonify({"permutations": perms})


@app.route('/')
def testing_endpoint():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True)