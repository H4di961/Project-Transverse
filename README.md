# Bomberman Clone - Multiplayer Battle Game

A Python remake of the classic Bomberman game featuring multiplayer battles, and special attacks. Built with Pygame.

## Features

- 2-Player Local Multiplayer (Arrow Keys vs WASD controls)
- Destructible Environment with random block generation
- Special Attack System with charging mechanics
- Animated Explosions and player defeat sequences
- Dynamic Map Scaling based on screen resolution


### Prerequisites
- Python 3.7+
- Pip package manager
- Pygame library

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bomberman-clone.git
cd bomberman-clone
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Start the game from the terminal:
```bash
python menu.py
```

2. Use the main menu to:
   - Start a new game
   - View controls and special attack instructions
   - Show controls
   - Exit the game

### Controls
| Player 1        | Player 2         | Action          |
|-----------------|------------------|-----------------|
| W, A, S, D      | Arrow Keys       | Movement        |
| E               | Right Shift      | Plant Bomb      |
| Movement Keys   | Movement Keys    | Aim Special     |

### Special Attacks
- Earn special attacks by destroying 5 blocks
- During special attack:
  - Attacking player becomes stationary
  - Use movement keys to aim
  - Release bomb key to execute
  - Opponent gets temporary speed boost after being hit

### AI Pathfinding
- DFS (Depth-First Search) for basic pathfinding
- Dijkstra's Algorithm for optimized routes
- Configurable via the game menu

### Match System
- Best-of-three match counter
- Victory animation sequences
- Auto-reset after match conclusion
- Score persistence between rounds

## Project Structure
```
bomberman-clone/
├── main.py              # Core game logic and mechanics
├── menu.py              # Menu system (main entry point)
├── algorithm.py         # AI pathfinding algorithms
├── counter.py           # Match scoring system
├── maps/                # Game assets directory
│   └── background_bomberman.PNG
├── requirements.txt     # Dependency list
└── README.md
```

## Configuration Options
1. In-game menu settings:
   - Toggle path visualization
   - Adjust game speed

2. Code modifications:
   - Modify WINDOW_SCALE in menu.py
   - Adjust TILE_SIZE calculations
   - Edit initial matrice layout in main.py

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch:
```bash
git checkout -b feature/NewFeature
```
3. Commit your changes:
```bash
git commit -m 'Add NewFeature'
```
4. Push to the branch:
```bash
git push origin feature/NewFeature
```
5. Open a Pull Request

## Acknowledgments

- Pygame community for excellent documentation
- Classic Bomberman games for game mechanics inspiration
- Computer science pathfinding algorithms community
- Open source contributors to pygame-menu library
```
