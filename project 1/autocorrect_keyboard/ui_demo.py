import tkinter as tk
from tkinter import font
import math

class RoundedFrame(tk.Canvas):
    def __init__(self, parent, width, height, radius=20, bg="#FFFFFF", **kwargs):
        super().__init__(parent, width=width, height=height, bg=parent["bg"], highlightthickness=0, **kwargs)
        self.radius = radius
        self.fill_color = bg
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        self.delete("all")
        # Draw rounded rectangle
        x1, y1 = 0, 0
        x2, y2 = self.width, self.height
        r = self.radius
        
        # Create polygon for rounded rect
        points = [
            x1+r, y1,
            x2-r, y1,
            x2, y1, x2, y1+r,
            x2, y2-r,
            x2, y2, x2-r, y2,
            x1+r, y2,
            x1, y2, x1, y2-r,
            x1, y1+r,
            x1, y1
        ]
        self.create_polygon(points, smooth=True, fill=self.fill_color)

class Config:
    # Colors
    BG_COLOR = "#F3F4F6"
    PRIMARY_BLUE = "#2563EB"
    HEADER_GRADIENT_START = "#1E3A8A"
    HEADER_GRADIENT_END = "#2563EB"
    SUCCESS_GREEN = "#22C55E"
    ACCENT_RED = "#EF4444"
    CARD_WHITE = "#FFFFFF"
    TEXT_DARK = "#1F2937"
    TEXT_LIGHT = "#9CA3AF"
    
    # Fonts
    FONT_FAMILY = "Segoe UI"

class SmartTypeUI:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.setup_ui()
    
    def setup_window(self):
        self.root.title("SmartType - Intelligent Autocorrect")
        self.root.geometry("1100x750")
        self.root.configure(bg=Config.BG_COLOR)

    def setup_ui(self):
        self._fonts()
        self._header()
        self._main_content()
        self._footer()

    def _fonts(self):
        self.title_font = font.Font(family=Config.FONT_FAMILY, size=24, weight="bold")
        self.subtitle_font = font.Font(family=Config.FONT_FAMILY, size=11)
        self.status_font = font.Font(family=Config.FONT_FAMILY, size=10, weight="bold")
        self.input_font = font.Font(family="Consolas", size=16)
        self.card_header_font = font.Font(family=Config.FONT_FAMILY, size=13, weight="bold")
        self.result_font = font.Font(family=Config.FONT_FAMILY, size=18, weight="bold")
        self.footer_font = font.Font(family=Config.FONT_FAMILY, size=9)

    def _header(self):
        # Header Frame with Simulated Gradient (Solid for Tkinter simplicity, or minimal gradient steps)
        # Using solid Primary Blue as requested in one of the stops, but we can do a simple frame.
        header = tk.Frame(self.root, bg=Config.PRIMARY_BLUE, height=100)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        # Title & Subtitle Container
        title_frame = tk.Frame(header, bg=Config.PRIMARY_BLUE)
        title_frame.pack(side="left", padx=40, pady=20)

        tk.Label(title_frame, text="SmartType", font=self.title_font, 
                 bg=Config.PRIMARY_BLUE, fg="white").pack(anchor="w")
        
        tk.Label(title_frame, text="Intelligent Autocorrect & Prediction Engine", 
                 font=self.subtitle_font, bg=Config.PRIMARY_BLUE, fg="#BFDBFE").pack(anchor="w")

        # Status Indicator
        status_frame = tk.Frame(header, bg=Config.PRIMARY_BLUE)
        status_frame.pack(side="right", padx=40)
        
        # Green Dot (Using unicode)
        status_lbl = tk.Label(status_frame, text="● System Ready", 
                              font=self.status_font, bg=Config.PRIMARY_BLUE, fg=Config.SUCCESS_GREEN)
        status_lbl.pack()

    def _main_content(self):
        container = tk.Frame(self.root, bg=Config.BG_COLOR)
        container.pack(fill="both", expand=True, padx=40, pady=30)
        
        # 1. Typing Area Card
        self._create_typing_card(container)

        # Spacing
        tk.Frame(container, bg=Config.BG_COLOR, height=20).pack()

        # 2. Bottom Split Section
        bottom_frame = tk.Frame(container, bg=Config.BG_COLOR)
        bottom_frame.pack(fill="x")
        bottom_frame.columnconfigure(0, weight=1)
        bottom_frame.columnconfigure(1, weight=1)

        self._create_prediction_card(bottom_frame)
        self._create_autocorrect_card(bottom_frame)

    def _create_typing_card(self, parent):
        # Background frame for shadow/border effect could go here, 
        # but for simplicity in Tkinter, we use a Frame with thick padding or a bordered frame.
        
        card = tk.Frame(parent, bg=Config.CARD_WHITE, padx=25, pady=25)
        card.pack(fill="x")
        
        # Rounded corners mock-up: Tkinter doesn't do real rounded corners on Frames easily without images.
        # We will use a flat, clean card style which is also very modern "Material" style.
        # To strictly follow "Rounded corners (16px radius)", we would need a Canvas-based approach 
        # for the *container*, which is complex for resizing. 
        # I will stick to a very clean flat card with a subtle border for robustness.
        
        card.configure(highlightbackground="#E5E7EB", highlightthickness=1)

        tk.Label(card, text="TYPE HERE", font=("Segoe UI", 9, "bold"), 
                 bg=Config.CARD_WHITE, fg=Config.TEXT_LIGHT).pack(anchor="w", pady=(0, 10))

        self.input_box = tk.Text(card, height=6, font=self.input_font,
                                 bg=Config.BG_COLOR, fg=Config.TEXT_DARK,
                                 relief="flat", padx=15, pady=15,
                                 highlightbackground=Config.PRIMARY_BLUE, highlightthickness=0)
        self.input_box.pack(fill="x")
        
        # Add a subtle border to the input box via a wrapper frame if needed, 
        # or just rely on the background contrast.
        self.input_box.configure(bg="#F9FAFB") # Very light grey for input area

    def _create_prediction_card(self, parent):
        # Left side - Blue Accent
        frame = tk.Frame(parent, bg=Config.CARD_WHITE, padx=20, pady=20)
        frame.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        frame.configure(highlightbackground=Config.PRIMARY_BLUE, highlightthickness=1) # Blue border hint
        
        # Top Accent Line (mocked with a frame at top)
        tk.Frame(frame, bg=Config.PRIMARY_BLUE, height=3).place(relx=0, rely=0, relwidth=1)

        tk.Label(frame, text="NEXT WORD PREDICTION", font=self.card_header_font, 
                 bg=Config.CARD_WHITE, fg=Config.PRIMARY_BLUE).pack(anchor="w")
        
        self.prediction_label = tk.Label(frame, text="waiting...", font=self.result_font,
                                         bg=Config.CARD_WHITE, fg=Config.TEXT_DARK, pady=15)
        self.prediction_label.pack(anchor="w")

    def _create_autocorrect_card(self, parent):
        # Right side - Red Accent
        frame = tk.Frame(parent, bg=Config.CARD_WHITE, padx=20, pady=20)
        frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))
        frame.configure(highlightbackground=Config.ACCENT_RED, highlightthickness=1) # Red border hint

        # Top Accent Line
        tk.Frame(frame, bg=Config.ACCENT_RED, height=3).place(relx=0, rely=0, relwidth=1)

        tk.Label(frame, text="AUTOCORRECT SUGGESTION", font=self.card_header_font, 
                 bg=Config.CARD_WHITE, fg=Config.ACCENT_RED).pack(anchor="w")
        
        self.correction_label = tk.Label(frame, text="waiting...", font=self.result_font,
                                         bg=Config.CARD_WHITE, fg=Config.TEXT_DARK, pady=15)
        self.correction_label.pack(anchor="w")

    def _footer(self):
        tk.Label(self.root, text="Designed for SmartType", font=self.footer_font,
                 bg=Config.BG_COLOR, fg=Config.TEXT_LIGHT).pack(side="bottom", pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartTypeUI(root)
    root.mainloop()
