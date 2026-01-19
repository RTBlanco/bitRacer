# BitRacer

Welcome to the BitRacer! This simple Python script animates a text-based car racing game where two cars compete to reach the finish line. It's a fun demonstration of basic animation techniques using the console.

## Features

- Animated car movement across the terminal screen
- Randomly determines a winner for each race
- Simple and easy to understand code structure

## How It Works

The script defines a car using ASCII art and animates its movement by printing each line with a calculated offset. The winner is chosen randomly, and the display updates until the cars reach the end of the screen.

### Key Functions

- `drive(i, car)`: This function prints the car at a given horizontal position `i`.
- `display()`: This function orchestrates the entire race, including determining the winner and animating the cars.

## Requirements

- Python 3.x
- No additional libraries required

## Usage

1. Clone the repository or download the script.
2. Open your terminal.
3. Navigate to the directory where the script is located.
4. Run the script using:
   ```bash
   python car_race.py
   ```

## Example Output

When you run the script, you'll see two cars racing across the terminal. The output will look something like this:

```
                 ______       
            __/__|__\___    
           |  _  _     _  `-.   
            '-(_)------(_)--'
```

As the race progresses, you'll notice one of the cars pulling ahead, and at the end, the winner will be displayed.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Any enhancements or new features are welcome!

## License

This project is open-source and available under the MIT License.

---

Enjoy racing your cars! 🏎️