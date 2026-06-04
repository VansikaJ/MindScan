# 🎲 LudoMind — Disorder Detection through Play

LudoMind is a gamified psychological screening tool built with Python and Pygame. Players compete in a classic Ludo board game against an AI opponent while answering clinically-inspired questions. At the end of the game, responses are analyzed to flag potential indicators of **Learning Disorders** or **Mental Health Disorders**.

---

## 📸 Overview

The game integrates a fully functional Ludo engine with an embedded questionnaire system. Questions are presented between turns, making the screening feel natural and low-pressure. Results are shown at the end in a dialog summarizing disorder indicators based on response patterns.

---

## 🧠 Features

- **Ludo Board Game** — Full 4-player Ludo implementation with token movement, captures, safe zones, and finish detection
- **AI Opponent** — Computer-controlled player with randomized but valid move logic
- **Psychological Questionnaire** — Questions presented mid-game with Likert-scale responses (Never → Always)
- **Disorder Detection** — Two screening modes:
  - Learning Disorder Detection (disorders 1–16, questions 1–27)
  - Mental Health Disorder Detection (disorders 17–25, questions 28–47)
- **Results Dialog** — Post-game summary categorizing disorders by likelihood:
  - *Higher possibility* — all questions answered "Often" or "Always"
  - *Lower possibility* — at least one question answered "Sometimes", "Often", or "Always"
- **Animated Dice Rolls** — Visual dice animation with sound effects
- **Smooth Token Movement** — Step-by-step animated token movement along paths
- **GUI Color Picker** — In-game color selection screen for the human player

---

## 🗂️ Project Structure

```
├── main.py               # Entry point; game loop, color/disorder selection, results
├── game_logic.py         # Dice rolling, token movement, AI logic, capture mechanics
├── draw_utils.py         # All Pygame rendering (board, tokens, dice, turn indicator)
├── question_handler.py   # Question/answer loading, text wrapping, question dialog UI
├── constants.py          # Screen size, colors, grid config, paths, home/safe positions
├── user_responses.txt    # Auto-generated file storing player responses during gameplay
├── data/
│   ├── questions_output.txt   # CSV: question_id, question_text, disorder_id
│   ├── answers_output.txt     # CSV: answer_id, question_id, answer_text, score
│   └── disorders_output.txt   # CSV: disorder_id, disorder_name
└── assets/
    ├── dice-142528.mp3
    └── puzzle-game-bright-casual-video-game-music-249202.mp3
```

---

## ⚙️ Requirements

- Python 3.8+
- pygame
- tkinter (standard library)

Install dependencies:

```bash
pip install pygame
```

---

## 🚀 Getting Started

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ludomind.git
cd ludomind
```

2. **Ensure data and asset files are in place** (see Project Structure above).

3. **Run the game:**

```bash
python main.py
```

---

## 🎮 How to Play

1. **Choose your color** — Click on Red, Blue, Green, or Yellow.
2. **Choose a screening type** — Learning Disorder Detection or Mental Health Disorder Detection.
3. **Play Ludo** — Press `SPACE` to roll the dice on your turn. Press a number key to select which token to move.
4. **Answer questions** — After each non-6 roll, a question appears. Click your response to continue.
5. **View results** — After the game window closes, a dialog box shows disorder indicators based on your answers.

---

## 📊 Scoring & Detection Logic

Each response is scored 0–4:

| Response  | Score |
|-----------|-------|
| Never     | 0     |
| Rarely    | 1     |
| Sometimes | 2     |
| Often     | 3     |
| Always    | 4     |

**Higher possibility** of a disorder is flagged when *all* associated questions are answered "Often" or "Always".  
**Lower possibility** is flagged when *at least one* associated question is answered "Sometimes", "Often", or "Always".

---

## ⚠️ Disclaimer

LudoMind is a **screening tool only** and is not a diagnostic instrument. Results should not be used as a substitute for professional psychological evaluation. If indicators are flagged, please consult a qualified mental health or learning specialist.

