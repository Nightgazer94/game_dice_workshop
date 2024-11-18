from flask import Flask, request, render_template
import random

app = Flask(__name__)


def roll_dice(dice_notation):
    try:
        parts = dice_notation.lower().split('d')
        num_dice = int(parts[0]) if parts[0] else 1
        rest = parts[1]
        if '+' in rest:
            dice_sides, modifier = rest.split('+')
            modifier = int(modifier)
        elif '-' in rest:
            dice_sides, modifier = rest.split('-')
            modifier = -int(modifier)
        else:
            dice_sides = rest
            modifier = 0
        dice_sides = int(dice_sides)

        if dice_sides not in [3, 4, 6, 8, 10, 12, 20, 100]:
            return "Invalid dice type. Supported types are: D3, D4, D6, D8, D10, D12, D20, D100."

        total = sum(random.randint(1, dice_sides) for _ in range(num_dice)) + modifier
        return f'Result: {total}'
    except ValueError:
        return "Invalid input. Please enter a valid dice notation (for example: 2D10+5)."


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/roll', methods=['POST'])
def roll():
    dice_notation = request.form['dice_notation']
    result = roll_dice(dice_notation)
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)
