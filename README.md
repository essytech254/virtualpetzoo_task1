# Virtual Pet Zoo

## Description
Virtual Pet Zoo is an interactive Python-based simulation where users can manage and interact with virtual animals in a zoo. Users can feed the animals, play with them, monitor their health and happiness levels, and even adopt them. This project demonstrates object-oriented programming concepts such as inheritance and encapsulation, providing a fun and engaging way to interact with virtual pets.

## Features
- Add animals to the zoo.
- Feed animals with different types of food affecting their health.
- Play games with animals to improve their happiness levels.
- Monitor an animal's health status and happiness levels.
- Remove animals from the zoo when adopted.

## Technologies Used
- Python
- Object-Oriented Programming (OOP)

## Installation & Usage
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd virtual-pet-zoo
   ```
2. Run the program:
   ```bash
   python zoo.py
   ```

## Code Structure
- `Animal` class: Base class for all animals.
- `Panda`, `Elephant`, `Monkey`, `Bear`: Derived classes that inherit from `Animal`.
- `Zoo` class: Manages the list of animals in the zoo.
- Methods allow users to feed, play, and interact with animals.

## Example Usage
```python
zoo = Zoo()
panda = Panda("Po", 5)
zoo.add_animal(panda)
panda.feed("vegetables")
panda.play("fetch")
print(f"Health: {panda.health_status}, Happiness: {panda.happiness_level}")
```

## Future Improvements
- Implement a graphical user interface (GUI).
- Add more interactions and behaviors for animals.
- Save and load the zoo state for persistent gameplay.

## contribution
Contributions are welcome! Please fork the repository and submit a pull request with improvements or new features..

