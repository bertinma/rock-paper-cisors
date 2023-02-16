# Let's play Rock Paper Scissors against a computer !

## How to play ?
- Enter your name then press Enter 
- Press M to change your name
- Press Q for Rock 
- Press S for Paper
- Press D for Scissors
- The computer will then choose between Rock, Paper or Scissors.
- The winner will be displayed on the screen by adding a point in the 3 circles.
- Between each round, press Space to continue.

Enjoy !

## How to run ?
- Download the repository
- Open a terminal in the repository
- Run the command `python3 main.py` if you have PyQt5 installed 

### Run with Docker on macOS 

```bash
IP=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
xhost +
docker build -t rpc:latest .
docker run -it --rm -e DISPLAY=$IP:0 -v /tmp/.X11-unix:/tmp/.X11-unix -u qtuser rpc python3 main.py
```

