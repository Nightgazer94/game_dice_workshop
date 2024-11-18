# Dice Rolling Flask Application

This is a simple Flask-based web application that allows users to roll virtual dice using a specified dice notation. The application accepts a variety of standard dice notations (e.g., `2D6+3`, `D20`, etc.) and returns the result.

## Requirements

- Python 3
- Flask

To install Flask, run the following command:

```bash
pip install Flask
```

## File Structure

- `app.py`: The main application script.
- `templates/index.html`: The HTML template for the application's user interface.

## How to Run

1. Save the code in a file named `app.py`.
2. Create a folder named `templates` in the same directory as `app.py`.
3. Inside the `templates` folder, create an `index.html` file with a form where users can enter the dice notation.
4. Run the application using the following command:

   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

- Enter the dice notation in the format `<number of dice>D<type of dice>+<modifier>`.
- Examples:
  - `D20`: Rolls a 20-sided die.
  - `2D6+3`: Rolls two 6-sided dice and adds 3 to the result.

## Dice Notation Supported

- The application supports standard RPG dice notations, including `D3`, `D4`, `D6`, `D8`, `D10`, `D12`, `D20`, and `D100`.
- You can add or subtract a modifier, e.g., `2D10-5`.

## Application Workflow

1. **Index Page**: The user is presented with an input form (`index.html`) where they can enter the dice notation.
2. **Roll Dice**: When the user submits the form, a POST request is made to the `/roll` endpoint.
3. **Roll Logic**: The `roll_dice` function parses the dice notation and returns the result.
4. **Result**: The result is displayed on the index page.

## Error Handling

- The application handles incorrect inputs by displaying an error message indicating invalid notation or unsupported dice types.


