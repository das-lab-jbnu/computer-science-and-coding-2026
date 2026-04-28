WIDTH = 800
HEIGHT = 450
TITLE = "Tiny Warrior"

GROUND_Y = 340
MOVE_SPEED = 4
ATTACK_RANGE = 80
ATTACK_TIME = 18


class Warrior:
    def __init__(self, name, x, y):
        self.name = name
        self.actor = Actor("warrior_idle", (x, y))
        self.hp = 100
        self.facing = 1
        self.is_attacking = False
        self.attack_timer = 0

    @property
    def x(self):
        return self.actor.x

    @property
    def y(self):
        return self.actor.y

    def move(self, dx):
        self.actor.x += dx
        self.actor.x = max(50, min(WIDTH - 50, self.actor.x))

        if dx < 0:
            self.facing = -1
        elif dx > 0:
            self.facing = 1

    def attack(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_timer = ATTACK_TIME
            self.actor.image = "warrior_attack"

    def update(self):
        if self.is_attacking:
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.is_attacking = False
                self.actor.image = "warrior_idle"

    def attack_box(self):
        if self.facing == 1:
            return Rect((self.x + 25, self.y - 45), (ATTACK_RANGE, 70))
        return Rect((self.x - 25 - ATTACK_RANGE, self.y - 45), (ATTACK_RANGE, 70))

    def draw(self):
        self.actor.draw()
        screen.draw.text(self.name, center=(self.x, self.y - 90), fontsize=24, color="white")

        sword_start = (self.x + self.facing * 24, self.y - 24)
        sword_end = (self.x + self.facing * 70, self.y - 24)
        screen.draw.line(sword_start, sword_end, "white")

        if self.is_attacking:
            screen.draw.rect(self.attack_box(), "yellow")


class Dummy:
    def __init__(self, x, y):
        self.actor = Actor("training_dummy", (x, y))
        self.hp = 50
        self.hit_timer = 0

    @property
    def rect(self):
        return Rect(
            (self.actor.x - self.actor.width / 2, self.actor.y - self.actor.height / 2),
            (self.actor.width, self.actor.height),
        )

    def hit(self, damage):
        if self.hp > 0:
            self.hp = max(0, self.hp - damage)
            self.hit_timer = 10

    def update(self):
        if self.hit_timer > 0:
            self.hit_timer -= 1

    def draw(self):
        self.actor.draw()

        if self.hit_timer > 0:
            screen.draw.rect(self.rect, "red")

        screen.draw.text(f"HP: {self.hp}", center=(self.actor.x, self.actor.y - 90), fontsize=24, color="white")


warrior = Warrior("Warrior", 150, GROUND_Y - 35)
dummy = Dummy(610, GROUND_Y - 35)
message = "Arrow keys: move   Space: attack"


def draw_background():
    screen.fill((35, 40, 55))
    screen.draw.filled_rect(Rect((0, GROUND_Y), (WIDTH, HEIGHT - GROUND_Y)), (70, 120, 70))
    screen.draw.text("Tiny Warrior", center=(WIDTH / 2, 40), fontsize=42, color="white")
    screen.draw.text(message, center=(WIDTH / 2, 78), fontsize=26, color="lightgray")


def draw():
    draw_background()
    warrior.draw()
    dummy.draw()


def update():
    global message

    if keyboard.left:
        warrior.move(-MOVE_SPEED)
    if keyboard.right:
        warrior.move(MOVE_SPEED)

    warrior.update()
    dummy.update()

    if dummy.hp == 0:
        message = "Victory! The dummy is defeated."


def on_key_down(key):
    global message

    if key == keys.SPACE:
        warrior.attack()

        if warrior.attack_box().colliderect(dummy.rect):
            dummy.hit(10)
            message = "Hit! Software changed the game state."
        else:
            message = "Miss! Move closer and try again."
