# Molt

**Molt** is a 2D arcade game inspired by **Snake**, where the player controls a growing caterpillar.

The goal is simple: collect leaves, grow longer and survive as long as possible without hitting the walls or your own body.

The project is developed in **Python** with **Pygame**.

---

## Concept

The player controls a caterpillar moving around the screen.

Each time the caterpillar eats a leaf, a new segment is added to its body.

The longer the caterpillar becomes, the harder it is to move without colliding with itself.

The game is inspired by the classic **Snake** gameplay while adding its own visual identity and theme around the growth of a caterpillar.

---

## Technologies

* **Python**
* **Pygame**
* **Git / GitHub**
* **Piskel** *(planned for pixel-art assets)*

---

## Features

### Completed

* [x] Pygame window
* [x] Game loop
* [x] Caterpillar display
* [x] Caterpillar movement
* [x] Screen boundaries
* [x] Grid system
* [x] Leaf spawning
* [x] Leaf collection
* [x] Caterpillar growth
* [x] Body segment system
* [x] Collision with the walls
* [x] Collision with its own body

### Planned

* [ ] Score system
* [ ] Increasing difficulty
* [ ] Game Over
* [ ] Restart system
* [ ] Main menu
* [ ] Final visual identity
* [ ] Sound effects
* [ ] Music

---

## Gameplay

The main gameplay loop is:

**Move → Find a leaf → Eat it → Grow → Avoid your body → Repeat**

The difficulty will increase as the caterpillar gets longer.

---

## Project structure

```text
Molt/
├── main.py
├── README.md
└── assets/
```

---

## Project goal

The goal of **Molt** is to create a small but complete arcade game while improving my skills in:

* Python programming
* Pygame
* Game loops
* Object movement
* Collision detection
* Lists and data structures
* Game states
* Git and GitHub
* Pixel art

The project will be developed progressively, feature by feature.

---

## Project status

**Status:** In development

The core gameplay of **Molt** is already functional.

The next steps are to implement the **score system** and work on the **visual design** of the game.
