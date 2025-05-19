from flask import Flask, render_template, request

return render_template("index.html", result=result)

app = Flask(__name__)

# Vigenère cipher function
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        mode = request.form["mode"]
        message = request.form["message"]
        key = request.form["key"].lower()

        if mode == "encrypt":
            result = vigenere(message, key, 1)
        elif mode == "decrypt":
            result = vigenere(message, key, -1)
        else:
            result = "Invalid mode selected."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
