import sys, random
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer, QSize
from PyQt5.QtGui import QMovie, QCursor

app = QApplication(sys.argv)

label = QLabel()
movie = QMovie("pikachu.gif")
label.setMovie(movie)
movie.setScaledSize(QSize(70, 48))
movie.start()

label.setAttribute(Qt.WA_TranslucentBackground)
label.setWindowFlags(
    Qt.FramelessWindowHint |
    Qt.WindowStaysOnTopHint |
    Qt.Tool
)

screen = app.primaryScreen().geometry()
x, y = 100, 100
label.move(x, y)
label.show()
FOLLOW_SPEED = 0.15
OFFSET_X = 20
OFFSET_Y = 20
Follow = False
def move_pikachu():
    global x, y, Follow
    mouse = QCursor.pos()

    if random.random() < 0.05:
        Follow = True

    if Follow and random.random() < 0.03:
        Follow = False
        
    if Follow == True:
        target_x = mouse.x() + OFFSET_X
        target_y = mouse.y() + OFFSET_Y
        x += int((target_x - x) * FOLLOW_SPEED)
        y += int((target_y - y) * FOLLOW_SPEED)

        x = max(0, min(screen.width() - label.width(), x))
        y = max(0, min(screen.height() - label.height(), y))
    else:
        dx = random.randint(-30, 30)
        dy = random.randint(-30, 30)
        x = max(0, min(screen.width()- label.width(), x + dx))
        y = max(0, min(screen.height() - label.height(), y + dy))


    label.move(x, y)

def quit_app(event):
    if event.button() == Qt.RightButton:
        app.quit()

label.mousePressEvent = quit_app

timer = QTimer()
timer.timeout.connect(move_pikachu)
timer.start(500)

sys.exit(app.exec_())
