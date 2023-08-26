import tkinter as tk
import random
import time

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        self.words = ["apPle$", "aaKHK{:'m", "ananas","aaaaaaaaaa","12@#$%^%$32","32ghaba7","ba6by$","bcdvy%$ftgv#cf$","banana", "cheH78&)rry", "daAeW222@te","nbygayhbv&^%(){]?.,}", " 5%8&SGBGV5","elderberry", "fig", "graPo0o&^%4pe", "honeydew"]
        self.current_word = ""
        self.user_input = ""
        self.start_time = 0
        
        self.word_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.word_label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=("Helvetica", 18))
        self.entry.pack(pady=10)
        
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=20)
        
        self.next_word()
        
        self.entry.bind("<Return>", self.check_input)
    
    def next_word(self):
        self.user_input = ""
        self.entry.delete(0, tk.END)
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.start_time = time.time()
    
    def check_input(self, event):
        entered_text = self.entry.get().strip()
        if entered_text == self.current_word:
            elapsed_time = time.time() - self.start_time
            words_per_minute = int(len(entered_text) / (elapsed_time / 60))
            self.result_label.config(text=f"Your typing speed: {words_per_minute} WPM")
            self.next_word()
        else:
            self.result_label.config(text="Incorrect. Try again.")
            self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
