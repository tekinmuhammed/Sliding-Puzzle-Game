import random
import os
import sys
import time
import keyboard

# Hedef çözüm board'u
TARGET_BOARD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Hareket kuralları (satır ve sütun değişiklikleri)
MOVES = {
    "UP": (-1, 0),    # Yukarı hareket
    "DOWN": (1, 0),   # Aşağı hareket
    "LEFT": (0, -1),  # Sola hareket
    "RIGHT": (0, 1)   # Sağa hareket
}

def clear_console():
    """Konsolu temizler."""
    os.system('cls' if os.name == 'nt' else 'clear')

def is_solvable(board):
    """Kontrol: Tahta çözülebilir mi?"""
    one_d = [num for row in board for num in row if num != 0]
    inversions = sum(
        1 for i in range(len(one_d)) for j in range(i + 1, len(one_d)) if one_d[i] > one_d[j]
    )
    return inversions % 2 == 0

def generate_board():
    """Çözümü mümkün olan rastgele bir 3x3 tahta üretir."""
    while True:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 0]
        random.shuffle(board)
        board = [board[i:i+3] for i in range(0, len(board), 3)]
        if is_solvable(board):
            return board

def find_zero(board):
    """0'ın pozisyonunu (satır, sütun) döndürür."""
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return i, j

def print_board(board):
    """Tahtayı kullanıcıya yazdırır."""
    for row in board:
        print(" | ".join(str(num) if num != 0 else " " for num in row))
        print("-" * 11)

def is_valid_move(zero_row, zero_col, move_row, move_col):
    """Hareket geçerli mi?"""
    new_row, new_col = zero_row + move_row, zero_col + move_col
    return 0 <= new_row < 3 and 0 <= new_col < 3

def move(board, zero_pos, direction):
    """0'ı verilen yöne doğru hareket ettirir."""
    zero_row, zero_col = zero_pos
    move_row, move_col = MOVES[direction]
    if is_valid_move(zero_row, zero_col, move_row, move_col):
        new_row, new_col = zero_row + move_row, zero_col + move_col
        # Swap 0 and the target position
        board[zero_row][zero_col], board[new_row][new_col] = board[new_row][new_col], board[zero_row][zero_col]
        return new_row, new_col
    return zero_row, zero_col

def main():
    # Rastgele tahta üret ve sıfır pozisyonunu bul
    board = generate_board()
    zero_pos = find_zero(board)

    clear_console()
    print("Sliding Puzzle Oyunu!")
    print("Hedef:")
    print_board(TARGET_BOARD)
    input("\nDevam etmek için Enter'a basın...")

    # Oyun döngüsü
    while board != TARGET_BOARD:
        clear_console()
        print("Sliding Puzzle Oyunu!")
        print_board(board)
        print("\nHareket için yön tuşlarını kullan (Çıkış: q):")

        # Kullanıcıdan bir giriş bekle
        while True:
            if keyboard.is_pressed("up"):
                zero_pos = move(board, zero_pos, "UP")  # Yukarı hareket
                time.sleep(0.2)  # Bekleme süresi
                break
            elif keyboard.is_pressed("down"):
                zero_pos = move(board, zero_pos, "DOWN")  # Aşağı hareket
                time.sleep(0.2)  # Bekleme süresi
                break
            elif keyboard.is_pressed("left"):
                zero_pos = move(board, zero_pos, "LEFT")  # Sol hareket
                time.sleep(0.2)  # Bekleme süresi
                break
            elif keyboard.is_pressed("right"):
                zero_pos = move(board, zero_pos, "RIGHT")  # Sağ hareket
                time.sleep(0.2)  # Bekleme süresi
                break
            elif keyboard.is_pressed("q"):
                print("\nOyun sonlandırıldı.")
                sys.exit()

    # Oyuncu çözümü tamamladı
    clear_console()
    print("Tebrikler! Puzzle'ı çözdünüz!")
    print_board(board)

if __name__ == "__main__":
    main()

""" # Sliding Puzzle Game
A fun and interactive **Sliding Puzzle Game** implemented in Python. The objective is to arrange the tiles on a 3x3 board in the correct order by sliding the empty tile (0) using the arrow keys.

### 🎯 Objective
Arrange the board tiles into the following order:

 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 |   
-----------

 
### ✨ Features
* Randomly generated, solvable puzzles.
* Intuitive gameplay using **arrow keys** for movement.
* Clear console interface for a seamless experience.
* Automatic validation to ensure puzzles are solvable.

### 🚀 Getting Started
**Prerequisites**
* Python 3.6 or later installed on your system.
* The **keyboard** module installed. You can install it using pip:

     `pip install keyboard`


### Installation
1. Clone the repository to your local machine:

     `git clone https://github.com/tekinmuhammed/Sliding-Puzzle-Game`
3. Navigate to the project directory:

     `cd sliding-puzzle-game`

### Running the Game
Run the game using the following command:

`python sliding_puzzle.py`

### 🕹️ How to Play
1. Use the arrow keys to slide the empty tile (`0`) up, down, left, or right.
2. The goal is to arrange the tiles in numerical order as shown above.
3. Press **q** at any time to quit the game.

### 📝 License
This project is licensed under the MIT License - see the [LICENSE](https://mit-license.org/) file for details.

### 💡 Acknowledgments 
Inspired by the classic sliding puzzle game.
Special thanks to the Python community for their incredible support and tools.
"""
