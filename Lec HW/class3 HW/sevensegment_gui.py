import tkinter as tk
from tkinter import ttk

# 👇 改為 P1_0 ~ P1_8 共 9 個腳位
PIN_LIST = [f"P1_{i}" for i in range(9)]  # P1_0 ~ P1_8
SEG_LIST = ["A", "B", "C", "D", "E", "F", "G"]

# 七段顯示器段位在 Canvas 的座標（你可微調）
SEG_COORDS = {
    "A": (30, 10, 130, 30),
    "B": (130, 30, 150, 90),
    "C": (130, 100, 150, 160),
    "D": (30, 160, 130, 180),
    "E": (10, 100, 30, 160),
    "F": (10, 30, 30, 90),
    "G": (30, 85, 130, 105),
}

class SevenSegmentGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("七段顯示器腳位模擬 (支援 P1_0 ~ P1_8)")
        self.resizable(False, False)

        # === 段位 ↔ 腳位 對照 ===
        map_frame = ttk.LabelFrame(self, text="段位 ↔ 腳位 對照（可編輯）")
        map_frame.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        self.seg_to_pin = {}
        self.map_vars = {}
        for i, seg in enumerate(SEG_LIST):
            ttk.Label(map_frame, text=seg).grid(row=i, column=0, padx=2, pady=1)
            var = tk.StringVar(value=PIN_LIST[i])  # 初始對應前幾個腳位
            cmb = ttk.Combobox(map_frame, values=PIN_LIST, width=5, textvariable=var, state="readonly")
            cmb.grid(row=i, column=1, padx=2, pady=1)
            cmb.bind("<<ComboboxSelected>>", self.update_map_and_display)
            self.map_vars[seg] = var
            self.seg_to_pin[seg] = var.get()

        # === 腳位狀態開關 ===
        pin_frame = ttk.LabelFrame(self, text="腳位狀態 0=OFF / 1=ON")
        pin_frame.grid(row=0, column=1, padx=10, pady=10, sticky="n")

        self.pin_vars = {}
        for i, pin in enumerate(PIN_LIST):
            ttk.Label(pin_frame, text=pin).grid(row=i, column=0, padx=2, pady=1)
            var = tk.IntVar(value=0)
            chk = ttk.Checkbutton(pin_frame, variable=var, command=self.update_display)
            chk.grid(row=i, column=1, padx=2, pady=1, sticky="w")
            self.pin_vars[pin] = var

        # === 七段顯示器 Canvas ===
        disp_frame = ttk.LabelFrame(self, text="七段顯示器模擬")
        disp_frame.grid(row=0, column=2, padx=10, pady=10)

        self.canvas = tk.Canvas(disp_frame, width=160, height=190, bg="#333333")
        self.canvas.pack()
        self.seg_items = {}
        for seg, (x0, y0, x1, y1) in SEG_COORDS.items():
            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill="#550000", outline="")
            self.seg_items[seg] = rect

        self.update_display()  # 初始渲染

    def update_map_and_display(self, *_):
        for seg, var in self.map_vars.items():
            self.seg_to_pin[seg] = var.get()
        self.update_display()

    def update_display(self):
        ON_COLOR = "#FF3B2F"
        OFF_COLOR = "#550000"
        for seg, pin in self.seg_to_pin.items():
            state = self.pin_vars.get(pin, tk.IntVar(value=0)).get()
            fill = ON_COLOR if state else OFF_COLOR
            self.canvas.itemconfigure(self.seg_items[seg], fill=fill)

# ===== 主程式入口 =====
if __name__ == "__main__":
    SevenSegmentGUI().mainloop()
