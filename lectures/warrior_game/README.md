# Tiny Warrior

Pygame Zero로 실행하는 아주 작은 워리어 실습입니다.

## 설치

```powershell
pip install pgzero
```

## 실행

```powershell
pgzrun warrior_game.py
```

`python warrior_game.py`가 아니라 `pgzrun warrior_game.py`로 실행해야 합니다. Pygame Zero가 `Actor`, `screen`, `keyboard`, `keys`, `Rect` 같은 객체를 자동으로 준비해 줍니다.

## 폴더 구조

```text
warrior_game/
├── images/
│   ├── training_dummy.png
│   ├── warrior_attack.png
│   └── warrior_idle.png
├── README.md
└── warrior_game.py
```

## 조작

- 왼쪽/오른쪽 방향키: 이동
- Space: 공격

## 실습 목표

- `Warrior` 클래스로 게임 캐릭터의 상태와 행동을 묶어 봅니다.
- `Dummy` 클래스로 공격 대상의 상태를 표현합니다.
- 입력, 업데이트, 그리기, 충돌 판정이 작은 게임 루프 안에서 어떻게 연결되는지 봅니다.
