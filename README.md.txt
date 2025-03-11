# Bubble Pop!

A simple bubble popping game created with Pygame.

## Installation

1.  **Install Python:** Ensure you have Python 3.x installed on your system.
2.  **Install Pygame:** Open your terminal or command prompt and run:
    ```bash
    pip install pygame
    ```

## How to Run

1.  **Save the Code:** Save the provided Python code as a file named `bubble_game.py`.
2.  **Run the Game:** Open your terminal or command prompt, navigate to the directory where you saved `bubble_game.py`, and run:
    ```bash
    python bubble_game.py
    ```

## Gameplay

* Click on the bubbles to pop them and earn points.
* Bubbles rise from the bottom of the screen.
* The game continues until you close the window.
* Your score is displayed in the top-left corner.

## Controls

* **Left Mouse Button:** Pop bubbles.
* **Close Window:** Quit the game.

## Customization

* **Bubble Frequency:** Change the probability of new bubbles appearing by adjusting the value in the line `if random.random() < 0.02:` (e.g., `0.01` for fewer bubbles, `0.03` for more).
* **Bubble Speed:** Modify the range of bubble speeds in the line `speed_y = random.uniform(-5, -2)` to make bubbles move faster or slower.
* **Bubble Size:** Change the size of the bubbles by altering the `bubble_radius` variable.
* **Colors:** Modify the RGB color values for `WHITE`, `BLUE`, and `RED` to change the game's appearance.
* **Window Size:** Adjust the `WIDTH` and `HEIGHT` variables to change the game window dimensions.

## Dependencies

* Python 3.x
* Pygame

## Author

This game was created by a large language model.

## License

This project is open-source and available for use and modification.