    from flask import Flask, request, render_template

    app = Flask(__name__)

    def shift_character(char, shift, encrypt=True):
        if not char.isalpha():
            return char

        ascii_base = 97 if char.islower() else 65
        if not encrypt:
            shift = -shift

        shifted = (ord(char) - ascii_base + shift) % 26
        return chr(shifted + ascii_base)

    def process_text(text, shift, encrypt=True):
        result = ''
        for char in text:
            result += shift_character(char, shift, encrypt)
        return result

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            plaintext = request.form.get('plaintext')
            shift = int(request.form.get('shift', 3))
            action = request.form.get('action')

            if action == 'encrypt':
                result = process_text(plaintext, shift, encrypt=True)
            elif action == 'decrypt':
                result = process_text(plaintext, shift, encrypt=False)
            else:
                result = ''

            return render_template('index.html', result=result, plaintext=plaintext, shift=shift)

        return render_template('index.html', result='', plaintext='', shift=3)

    if __name__ == '__main__':
        app.run(debug=True)