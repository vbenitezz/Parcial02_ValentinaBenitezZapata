from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/respuesta_json/<int:num>', methods=['GET'])
def respuesta_json(num):
    factorial = math.factorial(num)
    par_impar = "Par" if num % 2 == 0 else "Impar"

    return jsonify({
        "num": num,
        "factorial": factorial,
        "par_impar": par_impar
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
