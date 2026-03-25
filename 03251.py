import tkinter as tk
import random

class Pet:
    def __init__(self, name, pet_type):
        self.name = name
        self.type = pet_type
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.exp = 0
        self.level = 1

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.exp += 10

    def play(self):
        self.happiness = min(100, self.happiness + 20)
        self.energy = max(0, self.energy - 15)
        self.exp += 15

    def rest(self):
        self.energy = min(100, self.energy + 25)
        self.exp += 5

    def level_up(self):
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            return True
        return False

    def random_event(self):
        event = random.choice(["none", "sick", "gift"])
        if event == "sick":
            self.happiness -= 10
            return "😢 아파졌어요!"
        elif event == "gift":
            self.exp += 20
            return "🎁 선물을 발견!"
        return ""

class PetGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🐾 키우기 게임")

        self.pet = None

        self.create_start_screen()

    def create_start_screen(self):
        self.clear()

        tk.Label(self.root, text="캐릭터 선택", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="🐶 강아지", command=lambda: self.start_game("강아지")).pack(pady=5)
        tk.Button(self.root, text="🐱 고양이", command=lambda: self.start_game("고양이")).pack(pady=5)
        tk.Button(self.root, text="🐰 토끼", command=lambda: self.start_game("토끼")).pack(pady=5)

    def start_game(self, pet_type):
        name = "내 " + pet_type
        self.pet = Pet(name, pet_type)
        self.create_game_screen()

    def create_game_screen(self):
        self.clear()

        self.status_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.event_label = tk.Label(self.root, text="", fg="blue")
        self.event_label.pack()

        tk.Button(self.root, text="🍖 밥 주기", command=self.feed).pack(pady=5)
        tk.Button(self.root, text="🎾 놀기", command=self.play).pack(pady=5)
        tk.Button(self.root, text="😴 쉬기", command=self.rest).pack(pady=5)

        self.update_status()

    def update_status(self):
        if not self.pet:
            return

        text = (
            f"{self.pet.name} ({self.pet.type})\n"
            f"🍖 배고픔: {self.pet.hunger}\n"
            f"😊 행복: {self.pet.happiness}\n"
            f"⚡ 에너지: {self.pet.energy}\n"
            f"⭐ 레벨: {self.pet.level} ({self.pet.exp}/100)"
        )
        self.status_label.config(text=text)

        # 자동 감소
        self.pet.hunger += 3
        self.pet.happiness -= 3
        self.pet.energy -= 3

        # 게임오버 체크
        if (self.pet.hunger >= 100 or
            self.pet.happiness <= 0 or
            self.pet.energy <= 0):
            self.game_over()

    def feed(self):
        self.pet.feed()
        self.after_action()

    def play(self):
        self.pet.play()
        self.after_action()

    def rest(self):
        self.pet.rest()
        self.after_action()

    def after_action(self):
        event_msg = self.pet.random_event()
        self.event_label.config(text=event_msg)

        if self.pet.level_up():
            self.event_label.config(text="🎉 레벨 업!")

        self.update_status()

    def game_over(self):
        self.clear()
        tk.Label(self.root, text="💀 게임 오버", font=("Arial", 18)).pack(pady=20)
        tk.Button(self.root, text="다시 시작", command=self.create_start_screen).pack()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PetGameGUI(root)
    root.mainloop()