# Alien Invasion

One of my first Python projects: a space shooter built with Pygame.

## Project structure

```text
Alien-Invasion/
├── assets/               # Game images and icon
├── releases/
│   └── windows/          # Original Windows executable
├── src/                  # Original Python source code
│   └── main.py           # Game entry point
├── requirements.txt      # Dependencies
└── run.sh                # Linux launcher
```


## Running on Linux

You need Python 3, virtual environment support, and a graphical desktop session.
On Debian or Ubuntu, install the system requirements with:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

From the repository root, create a virtual environment and install Pygame:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
./run.sh
```

After installation, run `./run.sh` whenever you want to play.
The launcher uses `.venv/bin/python` and switches to `src/` so the game can
find its images. If `.venv` does not exist, it uses `python3` from the current environment.

You can also start the game manually with the virtual environment activated:

```bash
cd src
python main.py
```

Running `python src/main.py` from the repository root does not work with the
relative paths in the original code. Use the launcher or switch to `src/` first.

## Controls

| Action | Control |
| --- | --- |
| Start a game | Click **Play** |
| Move the ship | Left and right arrow keys |
| Shoot | Space bar |
| Quit | Press **Q** or close the window |

## Windows

The original executable is preserved at `releases/windows/Alien Invasion.exe`.
This is a Windows binary. On Linux, run the Python source using the steps above.
