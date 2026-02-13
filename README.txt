================================================================================
                         QUANTUMGRID GAME GUIDE
              Complete Rules, Installation & Deployment Manual
================================================================================
                          Version 3.5.0
                        February 7, 2026
================================================================================
                          TABLE OF CONTENTS
================================================================================
I.    Game Overview: What is QuantumGrid?
II.   Game Rules: How to Play
III.  Pattern Types: Mathematical Scoring System
IV.   Advanced Mechanics: Combos, Energy & Progression
V.    Controls Reference: Mouse & Keyboard
VI.   Installation Guide: Getting Started
VII.  Running the Game: Step-by-Step Instructions
VIII. Deployment Guide: Sharing Your Game
IX.   Troubleshooting: Common Issues & Solutions
X.    Advanced Topics: Customization & Modifications
================================================================================
                  I. GAME OVERVIEW: WHAT IS QUANTUMGRID?
================================================================================
QuantumGrid is a strategic puzzle game that challenges players to place 
numbered tiles on a 7x7 grid to create mathematical patterns. The game 
combines simple mechanics with deep strategic gameplay, rewarding players 
for recognizing mathematical relationships like Fibonacci sequences, prime 
numbers, and powers of two.

CORE CONCEPT:
You have a grid. You have numbered tiles. You place tiles to make patterns.
Patterns give you points. More complex patterns give more points. Creating
multiple patterns in one move multiplies your score. Plan ahead, think
strategically, and watch your score soar!

GAME OBJECTIVE:
Score as many points as possible before running out of moves or filling
the entire board. Beat your high score. Master the patterns. Become a
QuantumGrid champion!

KEY FEATURES:
- 7x7 grid providing 49 cells for strategic tile placement
- Tiles numbered 1-9 appearing randomly
- 4 distinct pattern types with different point values
- Combo multiplier system rewarding multi-pattern moves
- Quantum Energy mechanic for strategic move extension
- Level progression system with bonus moves
- Beautiful neon-cyberpunk visual design
- Smooth 120 FPS performance
- Comprehensive tutorial system
- High score tracking with persistent save

WHAT MAKES IT SPECIAL:
QuantumGrid is not just another match-3 game. It rewards mathematical
thinking without feeling like a math test. You discover Fibonacci sequences
naturally through gameplay. You learn to recognize prime numbers by creating
them. The game is both entertaining and educational, accessible yet deep,
simple to learn but challenging to master.

================================================================================
                    II. GAME RULES: HOW TO PLAY
================================================================================
STARTING THE GAME:
When you launch QuantumGrid, you see the main menu with three options:
- PLAY: Start a new game
- TUTORIAL: Learn the rules (recommended for first-time players)
- QUIT: Exit the game

Click PLAY to begin. You start with:
- An empty 7x7 grid (49 cells)
- 25 moves
- 3 charges of Quantum Energy
- 0 points
- Level 1

THE BASIC GAMEPLAY LOOP:
1. Look at the "Next Tiles" panel on the right side
2. The top tile (highlighted in GOLD) is your current tile
3. Click any empty cell on the grid to place that tile
4. The game automatically checks for patterns
5. If patterns are found, you score points and tiles highlight in gold
6. Your move counter decreases by 1
7. A new tile appears in the queue
8. Repeat until you run out of moves or fill the board

TILE PLACEMENT RULES:
- You can only place tiles in EMPTY cells (cells with no number)
- You must place the current tile (the gold one in Next Tiles panel)
- You cannot move or remove tiles once placed
- You cannot skip your turn or discard tiles
- Each placement consumes exactly 1 move

PATTERN DETECTION:
After you place a tile, the game scans:
- All 7 rows (horizontal lines)
- All 7 columns (vertical lines)  
- Both main diagonals (corner to corner)

For each line, it checks all possible sequences of 3 consecutive tiles
to see if they form any of the 4 pattern types.

WINNING CONDITION:
There is no traditional "win" in QuantumGrid. The goal is to score as
many points as possible before the game ends. Your score is compared
against your personal high score.

GAME OVER CONDITIONS:
The game ends when either:
1. Your move counter reaches 0 (displays "No moves remaining!")
2. All 49 cells are filled (displays "BOARD FULL!")

When the game ends, you see:
- Your final score
- The level you reached
- "NEW HIGH SCORE!" if you beat your previous best
- Options to play again or return to main menu

================================================================================
              III. PATTERN TYPES: MATHEMATICAL SCORING SYSTEM
================================================================================
QuantumGrid recognizes four distinct pattern types. Each pattern must
consist of exactly 3 consecutive tiles in a row, column, or diagonal.

PATTERN 1: SUM OF FIFTEEN (+50 points)
Three consecutive tiles that add up to exactly 15.

Examples:
- 9 + 5 + 1 = 15 ✓
- 8 + 4 + 3 = 15 ✓
- 7 + 6 + 2 = 15 ✓
- 7 + 5 + 3 = 15 ✓
- 6 + 6 + 3 = 15 ✓
- 5 + 5 + 5 = 15 ✓

Why 15? This number was chosen because it has many combinations using
single-digit numbers, making it achievable but requiring thought.

Strategy Tip: Sum of Fifteen is the most common pattern. Look for it
frequently to maintain steady point flow.

PATTERN 2: PRIME PRODUCT (+75 points)
Three consecutive tiles whose product is a prime number.

Prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43...
(numbers divisible only by 1 and themselves)

Examples:
- 1 × 1 × 2 = 2 (prime) ✓
- 1 × 1 × 3 = 3 (prime) ✓
- 1 × 1 × 5 = 5 (prime) ✓
- 1 × 1 × 7 = 7 (prime) ✓
- 1 × 2 × 2 = 4 (not prime) ✗
- 2 × 2 × 2 = 8 (not prime) ✗

Strategy Tip: Tiles with 1 are very valuable for this pattern since
1 × a × b = a × b, giving you control over the product.

PATTERN 3: FIBONACCI SEQUENCE (+100 points)
Three consecutive tiles forming part of the Fibonacci sequence.

The Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
(each number equals the sum of the two before it)

Valid 3-tile patterns:
- 1, 1, 2 ✓ (1 + 1 = 2)
- 1, 2, 3 ✓ (1 + 2 = 3)
- 2, 3, 5 ✓ (2 + 3 = 5)
- 3, 5, 8 ✓ (3 + 5 = 8)

Invalid examples:
- 1, 2, 4 ✗ (1 + 2 ≠ 4)
- 2, 4, 6 ✗ (2 + 4 ≠ 6)

Strategy Tip: The sequence 1-1-2 is easiest to create. Look for
opportunities to place these tiles in sequence.

PATTERN 4: POWERS OF TWO (+125 points)
Three consecutive tiles that are ALL powers of 2.

Powers of 2 are: 1, 2, 4, 8, 16, 32, 64, 128...
(2^0=1, 2^1=2, 2^2=4, 2^3=8...)

In QuantumGrid, only 1, 2, 4, and 8 are available (single digits).

Valid patterns (ALL three must be powers of 2):
- 1, 2, 4 ✓
- 2, 4, 8 ✓
- 1, 4, 8 ✓
- 1, 1, 2 ✓
- 2, 2, 4 ✓
- 4, 4, 8 ✓

Invalid examples:
- 1, 2, 3 ✗ (3 is not a power of 2)
- 2, 4, 6 ✗ (6 is not a power of 2)

Strategy Tip: This is the highest-scoring pattern but also the rarest.
Only 4 of the 9 possible tile values qualify. Prioritize this pattern
when you have the right tiles available.

PATTERN OVERLAP:
A single sequence of 3 tiles can match MULTIPLE patterns simultaneously!

Example: 1, 1, 2
- Sum of Fifteen? No (1 + 1 + 2 = 4)
- Prime Product? Yes! (1 × 1 × 2 = 2, which is prime) +75
- Fibonacci? Yes! (1 + 1 = 2) +100
- Powers of Two? Yes! (all three are powers of 2) +125
- Total: 75 + 100 + 125 = 300 points from one sequence!

This overlap is intentional and creates interesting strategic decisions.

================================================================================
          IV. ADVANCED MECHANICS: COMBOS, ENERGY & PROGRESSION
================================================================================
COMBO MULTIPLIER SYSTEM:
When a single tile placement creates multiple patterns across different
lines (rows, columns, diagonals), you trigger a COMBO!

How it works:
- Place a tile
- Game finds all patterns created by that placement
- Count the number of distinct patterns found
- Multiply total points by the pattern count

Example Scenario:
You place a tile that completes:
- A Sum of Fifteen in a row (+50 points)
- A Fibonacci sequence in a column (+100 points)
- Total base points: 150
- Combo multiplier: 2x (two patterns)
- Final score: 150 × 2 = 300 points!

The combo display appears in large GOLD text above the grid:
"2x COMBO!" or "3x COMBO!" or "4x COMBO!"

Maximum possible combo: 4x
(one pattern in the row, one in the column, one in each diagonal)

Strategy Tip: Setting up combos is the key to high scores. Look for
positions where a single tile will complete multiple patterns. This
requires planning several moves ahead and understanding the board state.

QUANTUM ENERGY SYSTEM:
Quantum Energy is a limited resource that extends your game.

Starting Energy: 3 charges (displayed as purple orbs)
Effect: +5 moves per charge
Activation: Press Q key
Maximum: 3 charges (cannot exceed)

When to use Quantum Energy:
- Early game: Extend the game to set up better patterns
- Mid game: Recover from a bad tile sequence
- Late game: Give yourself more moves to maximize final score

How to gain Quantum Energy:
- Start each game with 3 charges
- Earn 1 charge each time you level up (max 3 total)

Strategy Tip: Don't hoard Quantum Energy! Using it early can help you
set up combos that generate more points, leading to faster leveling,
which gives you more energy. It's a positive feedback loop.

LEVEL PROGRESSION SYSTEM:
You advance to the next level every 1000 points.

Level-up rewards:
- +10 bonus moves
- +1 Quantum Energy charge (up to maximum of 3)
- Sense of accomplishment!

Level progression:
- Level 1: 0-999 points
- Level 2: 1000-1999 points
- Level 3: 2000-2999 points
- And so on...

The level system creates a positive feedback loop:
1. Score points by creating patterns
2. Reach 1000 points → Level up
3. Gain 10 bonus moves + 1 energy
4. Use extra moves to create more patterns
5. Score more points → Level up again
6. Repeat!

This system rewards skilled play by extending the game for players who
create effective patterns and combos.

Strategy Tip: Try to level up before using Quantum Energy. The level-up
bonus gives you 10 moves, while Quantum Energy gives you 5. If you're
close to leveling up, create a few more patterns first, then use energy
if needed.

SCORE DISPLAY:
Your current score appears in large white numbers in the score panel.
When you score points, you see "+XXX" in green below the grid for 2 seconds.
High scores are saved automatically and displayed in gold on the menu.

MOVE COUNTER:
Displays "MOVES: XX" in the score panel.
- Green text when you have more than 10 moves (comfortable)
- Pink text when you have 10 or fewer moves (warning!)

This color coding helps you judge urgency and decide when to use
Quantum Energy.

================================================================================
                V. CONTROLS REFERENCE: MOUSE & KEYBOARD
================================================================================
MOUSE CONTROLS:
Left Click: Primary interaction method
- Click empty cells to place tiles
- Click buttons to activate them
- Click anywhere on pause/game-over overlays (no effect)

Mouse Movement:
- Hover over empty cells to see blue highlight
- Hover over buttons to see them light up
- Visual feedback confirms interactive elements

KEYBOARD SHORTCUTS:
These shortcuts work during gameplay (PLAYING state):

N - New Game
  Immediately starts a fresh game with:
  - Empty grid
  - 25 moves
  - 3 Quantum Energy charges
  - Score reset to 0
  - Level reset to 1

P - Pause/Resume
  Toggles between PLAYING and PAUSED states
  - Paused: Shows overlay with Resume/Restart/Main Menu options
  - Playing: Returns to game
  - Your game state is preserved while paused

H - Help
  Opens the tutorial system
  - Shows page 1 of 3 by default
  - Use Previous/Next buttons to navigate
  - Use "START PLAYING" to return to game

Q - Quantum Power
  Activates Quantum Energy (if available)
  - Consumes 1 energy charge
  - Grants +5 moves immediately
  - Only works if you have energy charges remaining
  - Visual feedback: purple orb becomes empty

F - Toggle FPS Display
  Shows/hides frames-per-second counter
  - Displays in top-left corner
  - Shows average FPS over last 60 frames
  - Useful for performance monitoring
  - Does not affect gameplay

ESC - Context-Sensitive Back/Pause
  Behavior depends on current game state:
  - MENU: Quit the game
  - PLAYING: Pause the game
  - PAUSED: Resume playing
  - TUTORIAL: Return to menu
  - GAME OVER: No effect (use buttons)

TUTORIAL NAVIGATION:
When viewing the tutorial:

Previous Button: Go to previous page (disabled on page 1)
Next Button: Go to next page (disabled on page 3)
Start Playing Button: Close tutorial and begin game (page 3 only)

PAUSE MENU:
When paused:

Resume Button: Return to game
Restart Button: Start new game (current game is lost)
Main Menu Button: Return to main menu (current game is lost)

GAME OVER SCREEN:
When game ends:

Play Again Button: Start new game immediately
Main Menu Button: Return to main menu

ACCESSIBILITY NOTES:
- All game functions are accessible via mouse
- Keyboard shortcuts provide faster access for experienced players
- No time pressure - take as long as you need to plan moves
- Clear visual feedback for all interactions
- High contrast neon colors for visibility

================================================================================
              VI. INSTALLATION GUIDE: GETTING STARTED
================================================================================
SYSTEM REQUIREMENTS:

Minimum Requirements:
- Operating System: Windows 7/8/10/11, macOS 10.12+, or Linux
- Python: Version 3.7 or higher
- RAM: 512 MB
- Storage: 50 MB free space
- Display: 1400x900 resolution or higher
- Input: Mouse and keyboard

Recommended Requirements:
- Python: Version 3.9 or higher
- RAM: 1 GB or more
- Display: 1920x1080 resolution
- Modern CPU (for 120 FPS performance)

STEP 1: INSTALL PYTHON

Windows:
1. Visit https://www.python.org/downloads/
2. Download Python 3.9 or higher (latest stable version recommended)
3. Run the installer
4. IMPORTANT: Check "Add Python to PATH" during installation
5. Click "Install Now"
6. Wait for installation to complete
7. Verify installation:
   - Open Command Prompt (Win + R, type "cmd", press Enter)
   - Type: python --version
   - Should display: Python 3.x.x

macOS:
1. Python 3 may already be installed. Check by opening Terminal:
   - Press Cmd + Space, type "Terminal", press Enter
   - Type: python3 --version
   - If version 3.7+ displays, skip to Step 2

2. If Python 3 is not installed:
   - Visit https://www.python.org/downloads/
   - Download Python 3.9 or higher for macOS
   - Run the installer package
   - Follow installation prompts
   - Verify: python3 --version

Linux (Ubuntu/Debian):
1. Open Terminal (Ctrl + Alt + T)
2. Update package list:
   sudo apt update
3. Install Python 3 and pip:
   sudo apt install python3 python3-pip
4. Verify installation:
   python3 --version
   pip3 --version

Linux (Fedora/RHEL):
1. Open Terminal
2. Install Python 3:
   sudo dnf install python3 python3-pip
3. Verify installation:
   python3 --version

STEP 2: INSTALL PYGAME

Pygame is the only external dependency for QuantumGrid.

Windows:
1. Open Command Prompt
2. Install Pygame:
   pip install pygame
3. Wait for installation to complete
4. Verify installation:
   python -c "import pygame; print(pygame.version.ver)"
   Should display Pygame version (e.g., 2.5.2)

macOS:
1. Open Terminal
2. Install Pygame:
   pip3 install pygame
3. Verify installation:
   python3 -c "import pygame; print(pygame.version.ver)"

Linux:
1. Open Terminal
2. Install Pygame:
   pip3 install pygame
   
   If you encounter permission errors, use:
   pip3 install --user pygame
   
3. Verify installation:
   python3 -c "import pygame; print(pygame.version.ver)"

TROUBLESHOOTING PYGAME INSTALLATION:

If "pip: command not found":
- Windows: Reinstall Python and ensure "Add Python to PATH" is checked
- macOS/Linux: Install pip separately:
  - Ubuntu/Debian: sudo apt install python3-pip
  - macOS: python3 -m ensurepip --upgrade

If "Permission denied":
- Add --user flag: pip install --user pygame
- Or use sudo (Linux/macOS): sudo pip3 install pygame

If installation fails with compiler errors:
- Windows: Install pre-built wheel (pip should do this automatically)
- Linux: Install development packages:
  sudo apt install python3-dev libsdl2-dev libsdl2-image-dev \
  libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev

STEP 3: DOWNLOAD QUANTUMGRID

Option A: Direct Download
1. Locate the quantumgrid.py file
2. Save it to a folder of your choice
   Recommended: Create a folder like C:\Games\QuantumGrid or ~/Games/QuantumGrid
3. Note the folder location for running the game

Option B: Git Clone (GitHub)
1. Install Git if not already installed
2. Open Terminal/Command Prompt
3. Navigate to desired folder:
   cd C:\Games  (Windows)
   cd ~/Games   (macOS/Linux)
4. Clone repository:
   git clone https://github.com/ms1963/quantumgrid.git
5. Navigate into folder:
   cd quantumgrid

STEP 4: VERIFY INSTALLATION

1. Open Terminal/Command Prompt
2. Navigate to the QuantumGrid folder:
   cd C:\Games\QuantumGrid  (Windows)
   cd ~/Games/QuantumGrid   (macOS/Linux)

3. List files to confirm quantumgrid.py exists:
   dir  (Windows)
   ls   (macOS/Linux)

4. You should see: quantumgrid.py

Installation is complete! Proceed to Section VII to run the game.

================================================================================
            VII. RUNNING THE GAME: STEP-BY-STEP INSTRUCTIONS
================================================================================
BASIC EXECUTION:

Windows:
1. Open Command Prompt
2. Navigate to game folder:
   cd C:\Games\QuantumGrid
3. Run the game:
   python quantumgrid.py
4. The game window should appear within 2-3 seconds

macOS:
1. Open Terminal
2. Navigate to game folder:
   cd ~/Games/QuantumGrid
3. Run the game:
   python3 quantumgrid.py
4. The game window should appear

Linux:
1. Open Terminal
2. Navigate to game folder:
   cd ~/Games/QuantumGrid
3. Run the game:
   python3 quantumgrid.py
4. The game window should appear

ALTERNATIVE: DOUBLE-CLICK EXECUTION

Windows:
1. Navigate to the QuantumGrid folder in File Explorer
2. Right-click quantumgrid.py
3. Select "Open with" → "Python"
4. Game should launch

Note: If Python is not in the "Open with" menu:
- Choose "Choose another app"
- Browse to Python installation (usually C:\Users\YourName\AppData\Local\Programs\Python\Python3X\python.exe)
- Check "Always use this app"
- Click OK

macOS:
1. Open Finder and navigate to QuantumGrid folder
2. Right-click (or Control-click) quantumgrid.py
3. Select "Open With" → "Python Launcher"
4. Game should launch

Linux:
1. Open file manager and navigate to QuantumGrid folder
2. Right-click quantumgrid.py
3. Select "Properties" or "Permissions"
4. Check "Allow executing file as program"
5. Close properties
6. Double-click the file to run

CREATING A DESKTOP SHORTCUT:

Windows:
1. Right-click on Desktop → New → Shortcut
2. For location, enter:
   python "C:\Games\QuantumGrid\quantumgrid.py"
   (adjust path to your actual location)
3. Click Next
4. Name it "QuantumGrid"
5. Click Finish
6. (Optional) Right-click shortcut → Properties → Change Icon

macOS:
1. Open Automator (Applications → Automator)
2. Choose "Application"
3. Search for "Run Shell Script" and drag it to the workflow
4. In the script box, enter:
   cd ~/Games/QuantumGrid
   python3 quantumgrid.py
5. Save as "QuantumGrid" to Applications folder
6. Drag from Applications to Dock for easy access

Linux (Ubuntu):
1. Create a .desktop file:
   nano ~/Desktop/quantumgrid.desktop
2. Add this content:
   [Desktop Entry]
   Type=Application
   Name=QuantumGrid
   Exec=python3 /home/yourusername/Games/QuantumGrid/quantumgrid.py
   Path=/home/yourusername/Games/QuantumGrid
   Terminal=false
   
3. Save and exit (Ctrl+X, Y, Enter)
4. Make executable:
   chmod +x ~/Desktop/quantumgrid.desktop
5. Double-click to run

STARTUP SEQUENCE:

When you run QuantumGrid, you'll see console output:

Initializing QuantumGrid ULTRA-FAST...
  Pre-rendering text...
  Creating background...
  Setting up game...
Ready!

========================================
  QuantumGrid ULTIMATE v3.5.0
  LIGHTNING FAST - 120 FPS!
  Perfect UI Alignment - Optimized!
========================================

Controls:
  Mouse: Click to interact
  N: New Game | P: Pause | H: Help | Q: Quantum Power
  F: Toggle FPS | ESC: Pause/Back/Quit

All buttons respond INSTANTLY!

Then the game window appears showing the main menu.

FIRST-TIME PLAYERS:

1. Click TUTORIAL button
2. Read through all 3 pages
3. Click "START PLAYING" on page 3
4. The game begins!

RETURNING PLAYERS:

1. Click PLAY button
2. Start placing tiles immediately

EXITING THE GAME:

Method 1: Close window (click X in top-right corner)
Method 2: From main menu, click QUIT button
Method 3: From main menu, press ESC key

When you exit, you'll see:

Thanks for playing QuantumGrid ULTIMATE!
   Final High Score: XXXXX

Your high score is automatically saved to quantumgrid_save.json

PERFORMANCE MONITORING:

To check game performance:
1. Start the game
2. Press F to toggle FPS display
3. Top-left corner shows current FPS
4. Should consistently show 115-120 FPS

If FPS is below 60:
- Close other applications
- Update graphics drivers
- Check system requirements
- See Troubleshooting section

================================================================================
            VIII. DEPLOYMENT GUIDE: SHARING YOUR GAME
================================================================================
OPTION 1: SHARE SOURCE CODE (Simplest)

Best for: Sharing with other Python developers

Steps:
1. Ensure your game file is named clearly: quantumgrid.py
2. Create a README.txt file with installation instructions:

   ===================================
   QUANTUMGRID v3.5.0
   ===================================
   
   REQUIREMENTS:
   - Python 3.7 or higher
   - Pygame library
   
   INSTALLATION:
   1. Install Python from python.org
   2. Install Pygame: pip install pygame
   3. Run game: python quantumgrid.py
   
   CONTROLS:
   - Mouse: Click to place tiles
   - N: New Game
   - P: Pause
   - Q: Quantum Power
   - H: Help
   
   Enjoy!

3. Compress both files into a ZIP:
   - quantumgrid.py
   - README.txt

4. Share the ZIP file via:
   - Email
   - Cloud storage (Google Drive, Dropbox)
   - GitHub repository
   - USB drive

Pros:
- Simple and straightforward
- Small file size (< 100 KB)
- Easy to modify and learn from
- Cross-platform (works on Windows, macOS, Linux)

Cons:
- Requires Python and Pygame installation
- Not suitable for non-technical users

OPTION 2: CREATE EXECUTABLE WITH PYINSTALLER

Best for: Sharing with non-technical users

PyInstaller converts Python scripts into standalone executables.

INSTALLATION:

pip install pyinstaller

CREATING WINDOWS EXECUTABLE:

1. Open Command Prompt in game folder
2. Run PyInstaller:
   pyinstaller --onefile --windowed --name QuantumGrid quantumgrid.py

3. Wait for build to complete (1-2 minutes)
4. Executable appears in dist folder: dist\QuantumGrid.exe
5. Test the executable:
   cd dist
   QuantumGrid.exe

6. Distribute the .exe file (approximately 10-15 MB)

CREATING MACOS APPLICATION:

1. Open Terminal in game folder
2. Run PyInstaller:
   pyinstaller --onefile --windowed --name QuantumGrid quantumgrid.py

3. Application bundle appears in dist folder: dist/QuantumGrid.app
4. Test the application:
   open dist/QuantumGrid.app

5. Distribute the .app file (approximately 15-20 MB)
   - Compress to ZIP for easier sharing
   - Users may need to right-click → Open (first time only)

CREATING LINUX EXECUTABLE:

1. Open Terminal in game folder
2. Run PyInstaller:
   pyinstaller --onefile --name QuantumGrid quantumgrid.py

3. Executable appears in dist folder: dist/QuantumGrid
4. Make it executable:
   chmod +x dist/QuantumGrid

5. Test:
   ./dist/QuantumGrid

6. Distribute the binary (approximately 10-15 MB)

PYINSTALLER OPTIONS EXPLAINED:

--onefile: Packages everything into single executable
--windowed: No console window (GUI only)
--name: Sets executable name
--icon: Add custom icon (optional)
  Example: --icon=quantumgrid.ico

ADVANCED PYINSTALLER:

To add a custom icon:
1. Create/download an icon file:
   - Windows: .ico format
   - macOS: .icns format
   - Linux: .png format

2. Run PyInstaller with icon:
   pyinstaller --onefile --windowed --icon=icon.ico --name QuantumGrid quantumgrid.py

To reduce file size:
1. Use UPX compression:
   - Download UPX from https://upx.github.io/
   - Place upx.exe in PATH
   - PyInstaller will use it automatically

2. Exclude unnecessary modules:
   pyinstaller --onefile --windowed --exclude-module matplotlib --exclude-module numpy --name QuantumGrid quantumgrid.py

OPTION 3: WEB DEPLOYMENT WITH PYGAME-WEB

Best for: Browser-based play (experimental)

Pygame-web (Pygbag) converts Pygame games to WebAssembly for browser play.

INSTALLATION:

pip install pygbag

PREPARATION:

1. Create a main.py file (required by pygbag):
   - Copy quantumgrid.py to main.py
   - Or create main.py that imports and runs your game

2. Create asyncio-compatible version:
   - Add "import asyncio" at top
   - Wrap main game loop with async/await
   - This requires code modifications

BUILDING:

pygbag main.py

This creates a web folder with HTML/JS files.

HOSTING:

Upload the web folder to:
- GitHub Pages
- Netlify
- Vercel
- Any static web host

Note: Pygame-web is experimental and may have compatibility issues.
Test thoroughly before deploying.

OPTION 4: GITHUB REPOSITORY

Best for: Open-source sharing and collaboration

SETUP:

1. Create GitHub account at github.com
2. Install Git on your computer
3. Create new repository on GitHub:
   - Name: quantumgrid
   - Description: "Strategic mathematical puzzle game"
   - Public or Private
   - Add README

4. Clone repository locally:
   git clone https://github.com/ms1963/quantumgrid.git

5. Copy game file into repository folder
6. Create README.md with game description and instructions
7. Create requirements.txt:
   pygame>=2.0.0

8. Commit and push:
   git add .
   git commit -m "Initial commit: QuantumGrid v3.5.0"
   git push origin main

BENEFITS:

- Version control
- Issue tracking
- Collaboration
- Free hosting
- Easy distribution (git clone)

OPTION 5: PYTHON PACKAGE (PyPI)

Best for: Professional distribution

Create a proper Python package and upload to PyPI.

STRUCTURE:

quantumgrid/
├── setup.py
├── README.md
├── LICENSE
├── requirements.txt
└── quantumgrid/
    ├── __init__.py
    └── game.py

SETUP.PY:

from setuptools import setup, find_packages

setup(
    name="quantumgrid",
    version="3.5.0",
    packages=find_packages(),
    install_requires=["pygame>=2.0.0"],
    entry_points={
        "console_scripts": [
            "quantumgrid=quantumgrid.game:main",
        ],
    },
    author="Michael Stal",
    description="Strategic mathematical puzzle game",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ms1963/quantumgrid",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)

UPLOAD TO PYPI:

1. Install tools:
   pip install twine build

2. Build package:
   python -m build

3. Upload to PyPI:
   twine upload dist/*

4. Users can install with:
   pip install quantumgrid

LICENSING:

Choose an appropriate license:
- MIT License: Permissive, allows commercial use
- GPL: Copyleft, requires derivatives to be open-source
- Apache 2.0: Permissive with patent grant

Add LICENSE file to your distribution.

DISTRIBUTION CHECKLIST:

Before sharing your game:
☐ Test on target platform(s)
☐ Verify all features work
☐ Check high score saving/loading
☐ Include README with instructions
☐ Add license information
☐ Test with fresh Python installation
☐ Verify file paths are relative (not absolute)
☐ Check for hardcoded personal information
☐ Optimize file size if using PyInstaller
☐ Create screenshots for promotion

================================================================================
           IX. TROUBLESHOOTING: COMMON ISSUES & SOLUTIONS
================================================================================
INSTALLATION ISSUES:

PROBLEM: "python: command not found"
SOLUTION:
- Windows: Reinstall Python, check "Add Python to PATH"
- macOS/Linux: Use python3 instead of python
- Verify installation: which python3 (macOS/Linux)

PROBLEM: "pip: command not found"
SOLUTION:
- Install pip: python -m ensurepip --upgrade
- Or use: python -m pip install pygame
- Linux: sudo apt install python3-pip

PROBLEM: "No module named 'pygame'"
SOLUTION:
- Install Pygame: pip install pygame
- Verify: python -c "import pygame"
- Check Python version: python --version (must be 3.7+)

PROBLEM: Pygame installation fails with "error: command 'gcc' failed"
SOLUTION (Linux):
sudo apt install python3-dev libsdl2-dev libsdl2-image-dev \
libsdl2-mixer-dev libsdl2-ttf-dev libfreetype6-dev

RUNTIME ISSUES:

PROBLEM: Game window doesn't appear
SOLUTION:
- Check console for error messages
- Verify screen resolution is at least 1400x900
- Try windowed mode (modify WINDOW_WIDTH/HEIGHT in code)
- Update graphics drivers

PROBLEM: "pygame.error: No available video device"
SOLUTION (Linux):
- Install SDL2: sudo apt install libsdl2-2.0-0
- Set display: export DISPLAY=:0
- Check X server is running

PROBLEM: Game runs but is completely black
SOLUTION:
- Update graphics drivers
- Try different display mode
- Check GPU compatibility
- Reduce window size in code

PROBLEM: "FileNotFoundError" or "Permission denied" when saving high score
SOLUTION:
- Check write permissions in game folder
- Run from user directory (not system folders)
- Windows: Don't run from C:\Program Files
- Linux: Don't run with sudo

PERFORMANCE ISSUES:

PROBLEM: Low FPS (below 60)
SOLUTION:
- Close other applications
- Update graphics drivers
- Reduce window size (edit WINDOW_WIDTH/HEIGHT)
- Disable FPS display (press F)
- Check CPU usage in Task Manager

PROBLEM: Input lag or delayed response
SOLUTION:
- Verify FPS is above 60 (press F to check)
- Close background applications
- Update Pygame: pip install --upgrade pygame
- Check mouse driver settings

PROBLEM: Game stutters or freezes
SOLUTION:
- Check available RAM (should have 500+ MB free)
- Close browser and other memory-intensive apps
- Restart computer
- Check for malware/antivirus interference

GAMEPLAY ISSUES:

PROBLEM: High score not saving
SOLUTION:
- Check quantumgrid_save.json exists in game folder
- Verify write permissions
- Don't run from read-only location (CD, USB)
- Check disk space (need at least 1 MB free)

PROBLEM: High score file corrupted
SOLUTION:
- Delete quantumgrid_save.json
- Game will create new file on next run
- High score resets to 0

PROBLEM: Tiles not placing where I click
SOLUTION:
- Ensure you're clicking empty cells (no number)
- Check that you have moves remaining
- Verify game is not paused
- Try clicking cell center, not edges

PROBLEM: Patterns not being detected
SOLUTION:
- Verify pattern rules (see Section III)
- Patterns must be exactly 3 consecutive tiles
- Check row, column, or diagonal alignment
- Gaps between tiles break patterns

PROBLEM: Quantum Energy (Q key) not working
SOLUTION:
- Check you have energy charges (purple orbs filled)
- Verify game state is PLAYING (not paused/menu)
- Press Q (not Shift+Q)
- Check keyboard layout (Q key position)

DISPLAY ISSUES:

PROBLEM: Text is blurry or pixelated
SOLUTION:
- Check display scaling settings
- Windows: Right-click desktop → Display settings → Scale 100%
- Disable DPI scaling for Python
- Update graphics drivers

PROBLEM: Window too large for screen
SOLUTION:
- Edit code: Reduce WINDOW_WIDTH and WINDOW_HEIGHT
- Recommended minimum: 1200x800
- Maintain aspect ratio approximately 14:9

PROBLEM: Colors look wrong or washed out
SOLUTION:
- Check monitor color settings
- Update graphics drivers
- Verify color profile (sRGB recommended)
- Check monitor cable connection

PROBLEM: Window appears off-screen
SOLUTION:
- Windows: Alt+Space → Move → Arrow keys
- macOS: Mission Control → Drag window
- Linux: Alt+F7, then arrow keys

PYINSTALLER ISSUES:

PROBLEM: Executable won't run
SOLUTION:
- Check antivirus (may block unknown executables)
- Run from Command Prompt to see error messages
- Rebuild with --debug flag
- Try --onedir instead of --onefile

PROBLEM: "Failed to execute script"
SOLUTION:
- Missing dependencies: rebuild with --hidden-import
- Check Python version compatibility
- Verify all imports in code
- Test in virtual environment first

PROBLEM: Executable is too large (>50 MB)
SOLUTION:
- Use UPX compression
- Exclude unnecessary modules: --exclude-module
- Use --onedir for smaller individual files
- Remove unused imports from code

PROBLEM: Antivirus flags executable as malware
SOLUTION:
- This is a false positive (common with PyInstaller)
- Add exception in antivirus
- Submit to antivirus vendor for whitelisting
- Code-sign executable (requires certificate)

MACOS-SPECIFIC ISSUES:

PROBLEM: "App is damaged and can't be opened"
SOLUTION:
- Right-click app → Open (instead of double-click)
- Or: System Preferences → Security → Allow
- Or: Terminal: xattr -cr QuantumGrid.app

PROBLEM: Permission denied errors
SOLUTION:
- Grant Terminal full disk access
- System Preferences → Security → Privacy → Full Disk Access
- Add Terminal to allowed apps

LINUX-SPECIFIC ISSUES:

PROBLEM: No sound (if you add audio later)
SOLUTION:
- Install audio libraries: sudo apt install libsdl2-mixer-2.0-0
- Check PulseAudio is running
- Verify volume settings

PROBLEM: Window manager issues
SOLUTION:
- Try different window manager
- Set SDL_VIDEO_X11_NET_WM_BYPASS_COMPOSITOR=0
- Update SDL2 libraries

GETTING HELP:

If you encounter issues not listed here:

1. Check console output for error messages
2. Search error message online
3. Check Pygame documentation: pygame.org/docs
4. Ask on forums:
   - Stack Overflow (tag: pygame)
   - Reddit: r/pygame
   - Pygame Discord community

5. Report bugs:
   - Include Python version
   - Include Pygame version
   - Include operating system
   - Include error messages
   - Describe steps to reproduce

================================================================================
           X. ADVANCED TOPICS: CUSTOMIZATION & MODIFICATIONS
================================================================================
CUSTOMIZING COLORS:

The Colors class (near top of code) defines all colors.

To change color scheme:

1. Locate the Colors class
2. Modify RGB values (0-255 for each component)

Example - Change to blue theme:
class Colors:
    DEEP_SPACE = (5, 5, 40)          # Darker blue
    DARK_PURPLE = (10, 10, 60)       # Blue-purple
    NEON_BLUE = (0, 150, 255)        # Bright blue
    NEON_PINK = (100, 150, 255)      # Light blue
    NEON_GREEN = (0, 200, 255)       # Cyan
    # ... etc

3. Save and run to see changes

CUSTOMIZING GRID SIZE:

To change from 7x7 to different size:

1. Locate: GRID_SIZE = 7
2. Change to desired size (e.g., GRID_SIZE = 9 for 9x9)
3. Adjust CELL_SIZE if needed for screen fit
4. Note: Larger grids = longer games, more strategy

Recommended sizes:
- 5x5: Quick games (15 minutes)
- 7x7: Standard (current, 20-30 minutes)
- 9x9: Long games (45+ minutes)

CUSTOMIZING STARTING MOVES:

To change initial move count:

1. Locate: self.moves_remaining = 25
2. Change to desired value (e.g., 50 for longer games)

Recommended values:
- 15: Quick challenge
- 25: Standard (current)
- 50: Extended play
- 100: Marathon mode

CUSTOMIZING PATTERN POINTS:

To adjust scoring balance:

1. Locate the check_line method
2. Find point assignments:
   - Sum of Fifteen: points += 50
   - Prime Product: points += 75
   - Fibonacci: points += 100
   - Powers of Two: points += 125

3. Modify values as desired

Example - Make Powers of Two worth more:
if all(self.is_power_of_2(x) for x in seq):
    points += 200  # Changed from 125

CUSTOMIZING LEVEL PROGRESSION:

To change level-up threshold:

1. Locate: new_level = (self.score // 1000) + 1
2. Change 1000 to desired value

Examples:
- 500: Level up every 500 points (faster)
- 2000: Level up every 2000 points (slower)

To change level-up rewards:

1. Locate: self.moves_remaining += 10
2. Change 10 to desired move bonus

CUSTOMIZING QUANTUM ENERGY:

To change energy effect:

1. Locate: self.moves_remaining += 5
2. Change 5 to desired move bonus

To change starting energy:

1. Locate: self.quantum_energy = 3
2. Change 3 to desired starting charges

To change maximum energy:

1. Locate: self.quantum_energy = min(3, ...)
2. Change 3 to desired maximum

CUSTOMIZING TILE RANGE:

To use different number range:

1. Locate: random.randint(1, 9)
2. Change range (e.g., random.randint(1, 12) for 1-12)
3. Update pattern detection if needed
4. Note: Affects pattern difficulty significantly

ADDING NEW PATTERN TYPES:

To add a custom pattern:

1. In check_line method, add new pattern check:

# Perfect Square pattern
if all(int(x**0.5)**2 == x for x in seq):
    points += 90
    matches.update(seq_indices)

2. Update tutorial with new pattern description
3. Update rules panel with new pattern info

Example patterns you could add:
- Arithmetic sequence (e.g., 2-4-6)
- Geometric sequence (e.g., 2-4-8)
- Perfect squares (e.g., 1-4-9)
- Palindromes (e.g., 3-5-3)
- Consecutive numbers (e.g., 4-5-6)

CUSTOMIZING WINDOW SIZE:

To change window dimensions:

1. Locate:
   WINDOW_WIDTH = 1400
   WINDOW_HEIGHT = 900

2. Change to desired size:
   WINDOW_WIDTH = 1600
   WINDOW_HEIGHT = 1000

3. Adjust panel positions accordingly
4. Maintain reasonable aspect ratio

CUSTOMIZING FRAME RATE:

To change target FPS:

1. Locate: FPS = 120
2. Change to desired value

Recommended values:
- 60: Standard (lower CPU usage)
- 120: Current (very responsive)
- 144: For high-refresh monitors
- 30: For low-power devices

ADDING SOUND EFFECTS:

To add audio (requires additional code):

1. Load sounds in __init__:
   self.place_sound = pygame.mixer.Sound("place.wav")
   self.pattern_sound = pygame.mixer.Sound("pattern.wav")

2. Play sounds at appropriate times:
   # When placing tile:
   self.place_sound.play()
   
   # When pattern detected:
   self.pattern_sound.play()

3. Provide sound files in same folder as game

ADDING BACKGROUND MUSIC:

1. In __init__ method:
   pygame.mixer.music.load("background.mp3")
   pygame.mixer.music.set_volume(0.3)
   pygame.mixer.music.play(-1)  # Loop forever

2. Provide music file in game folder

CREATING DIFFICULTY MODES:

Add difficulty selection in menu:

class Difficulty:
    EASY = 1
    NORMAL = 2
    HARD = 3

# In game initialization:
if difficulty == Difficulty.EASY:
    self.moves_remaining = 50
    self.quantum_energy = 5
elif difficulty == Difficulty.NORMAL:
    self.moves_remaining = 25
    self.quantum_energy = 3
elif difficulty == Difficulty.HARD:
    self.moves_remaining = 15
    self.quantum_energy = 1

SAVING GAME STATE:

To add save/load functionality:

1. Create save_game method:
def save_game(self):
    state = {
        'score': self.score,
        'level': self.level,
        'moves': self.moves_remaining,
        'energy': self.quantum_energy,
        'grid': [[cell.value for cell in row] for row in self.cells],
        'next_tiles': self.next_tiles
    }
    with open('savegame.json', 'w') as f:
        json.dump(state, f)

2. Create load_game method to restore state

3. Add Save/Load buttons to pause menu

ADDING STATISTICS TRACKING:

Track additional metrics:

self.total_patterns = 0
self.total_combos = 0
self.highest_combo = 0
self.patterns_by_type = {
    'sum15': 0,
    'prime': 0,
    'fibonacci': 0,
    'powers2': 0
}

Display on game-over screen for player insights.

CREATING ACHIEVEMENTS:

Define achievements:

achievements = {
    'first_combo': False,
    'score_1000': False,
    'level_10': False,
    'perfect_game': False,  # No wasted moves
}

Check and unlock during gameplay.
Display unlocked achievements on game-over screen.

MODDING BEST PRACTICES:

1. Make a backup before modifying
2. Test changes incrementally
3. Comment your modifications
4. Keep original values in comments
5. Document custom features
6. Share your mods with the community!

LEARNING RESOURCES:

To learn more about Pygame and game development:

- Pygame Documentation: pygame.org/docs
- Pygame Tutorials: pygame.org/wiki/tutorials
- Real Python Pygame Guide: realpython.com/pygame-a-primer
- Python Game Development: inventwithpython.com
- Game Programming Patterns: gameprogrammingpatterns.com

CONTRIBUTING:

If you create improvements or fixes:

1. Fork the repository (GitHub)
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request
6. Describe your changes clearly

Your contributions help make QuantumGrid better for everyone!

================================================================================
                              CONCLUSION
================================================================================
Congratulations! You now have complete knowledge of QuantumGrid:

✓ Game rules and pattern types
✓ Installation and setup
✓ Running and deploying
✓ Troubleshooting common issues
✓ Customization and modding

QUICK START REMINDER:

1. Install Python 3.7+
2. Install Pygame: pip install pygame
3. Run game: python quantumgrid.py
4. Click TUTORIAL to learn
5. Click PLAY to start
6. Have fun!

HINT:

Consider using a virtual Python environment for the game

SUPPORT:

For questions, bug reports, or suggestions:
- Check this guide first
- Search online for similar issues
- Ask in Pygame community forums
- Report bugs with detailed information

Thank you for playing QuantumGrid!
May your patterns be plentiful and your combos be mighty!

