import tkinter as tk
from tkinter import font
import nltk
from nltk.corpus import gutenberg
from spellchecker import SpellChecker
from collections import Counter, defaultdict
import threading

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

class AutocorrectKeyboard: # Class name preserved
    def __init__(self, root):
        self.root = root
        
        # --- UI CONFIGURATION (New) ---
        self.root.title("SmartType")
        self.root.geometry("1100x750") # Slightly larger for better spacing
        self.root.configure(bg=Config.BG_COLOR)

        # Initialize SpellChecker (Logic preserved)
        self.spell = SpellChecker()

        # Data for prediction (Logic preserved)
        self.bigram_model = defaultdict(Counter)

        # UI Setup (Method rewritten for new UI)
        self.setup_ui()

        # Load resources (Logic preserved, just updated UI labels)
        self.status_label.config(text="● Loading...", fg="#F59E0B") # Amber
        self.root.update()
        self.load_resources()
        self.status_label.config(text="● System Ready", fg=Config.SUCCESS_GREEN)

    def setup_ui(self):
        # ---------------------------------------------------------
        # FONTS (Updated)
        # ---------------------------------------------------------
        self.title_font = font.Font(family=Config.FONT_FAMILY, size=24, weight="bold")
        self.subtitle_font = font.Font(family=Config.FONT_FAMILY, size=11)
        self.status_font = font.Font(family=Config.FONT_FAMILY, size=10, weight="bold")
        self.input_font = font.Font(family="Consolas", size=16)
        self.card_header_font = font.Font(family=Config.FONT_FAMILY, size=13, weight="bold")
        self.result_font = font.Font(family=Config.FONT_FAMILY, size=18, weight="bold")
        self.footer_font = font.Font(family=Config.FONT_FAMILY, size=9)

        # ---------------------------------------------------------
        # HEADER SECTION (Blue Brand Bar - Updated)
        # ---------------------------------------------------------
        header = tk.Frame(self.root, bg=Config.PRIMARY_BLUE, height=100)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        # Title & Subtitle
        title_frame = tk.Frame(header, bg=Config.PRIMARY_BLUE)
        title_frame.pack(side="left", padx=40, pady=20)

        tk.Label(title_frame, text="SmartType", font=self.title_font, 
                 bg=Config.PRIMARY_BLUE, fg="white").pack(anchor="w")
        
        tk.Label(title_frame, text="Intelligent Autocorrect & Prediction Engine", 
                 font=self.subtitle_font, bg=Config.PRIMARY_BLUE, fg="#BFDBFE").pack(anchor="w")

        # Status Badge
        status_frame = tk.Frame(header, bg=Config.PRIMARY_BLUE)
        status_frame.pack(side="right", padx=40)
        
        self.status_label = tk.Label(status_frame, text="● Initializing...", 
                                     font=self.status_font, bg=Config.PRIMARY_BLUE, fg=Config.TEXT_LIGHT)
        self.status_label.pack()

        # ---------------------------------------------------------
        # BODY CONTAINER (Updated layout)
        # ---------------------------------------------------------
        container = tk.Frame(self.root, bg=Config.BG_COLOR)
        container.pack(fill="both", expand=True, padx=40, pady=30)
        
        # ---------------------------------------------------------
        # INPUT CARD (Updated)
        # ---------------------------------------------------------
        card = tk.Frame(container, bg=Config.CARD_WHITE, padx=25, pady=25)
        card.pack(fill="x")
        card.configure(highlightbackground="#E5E7EB", highlightthickness=1)

        tk.Label(card, text="TYPING AREA", font=("Segoe UI", 9, "bold"), 
                 bg=Config.CARD_WHITE, fg=Config.TEXT_LIGHT).pack(anchor="w", pady=(0, 10))

        self.input_box = tk.Text(card, height=6, font=self.input_font,
                                 bg="#F9FAFB", fg=Config.TEXT_DARK,
                                 relief="flat", padx=15, pady=15,
                                 highlightbackground=Config.PRIMARY_BLUE, highlightthickness=0)
        self.input_box.pack(fill="x")
        
        # Binding preserved
        self.input_box.bind("<KeyRelease>", self.on_key_release)

        # Spacing
        tk.Frame(container, bg=Config.BG_COLOR, height=20).pack()

        # ---------------------------------------------------------
        # RESULTS SECTION (Updated Grid Layout)
        # ---------------------------------------------------------
        results_frame = tk.Frame(container, bg=Config.BG_COLOR)
        results_frame.pack(fill="x")
        results_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(1, weight=1)

        # --- PREDICTION CARD (Blue Accent) ---
        pred_card_frame = tk.Frame(results_frame, bg=Config.CARD_WHITE, padx=20, pady=20)
        pred_card_frame.grid(row=0, column=0, sticky="ew", padx=(0, 10))
        pred_card_frame.configure(highlightbackground=Config.PRIMARY_BLUE, highlightthickness=1) 
        
        # Accent Line
        tk.Frame(pred_card_frame, bg=Config.PRIMARY_BLUE, height=3).place(relx=0, rely=0, relwidth=1)

        tk.Label(pred_card_frame, text="NEXT WORD PREDICTION", font=self.card_header_font, 
                 bg=Config.CARD_WHITE, fg=Config.PRIMARY_BLUE).pack(anchor="w")
        
        self.prediction_label = tk.Label(pred_card_frame, text="...", font=self.result_font, 
                                         bg=Config.CARD_WHITE, fg=Config.TEXT_DARK, pady=15)
        self.prediction_label.pack(anchor="w")

        # --- CORRECTION CARD (Red Accent) ---
        corr_card_frame = tk.Frame(results_frame, bg=Config.CARD_WHITE, padx=20, pady=20)
        corr_card_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))
        corr_card_frame.configure(highlightbackground=Config.ACCENT_RED, highlightthickness=1)

        # Accent Line
        tk.Frame(corr_card_frame, bg=Config.ACCENT_RED, height=3).place(relx=0, rely=0, relwidth=1)

        tk.Label(corr_card_frame, text="AUTOCORRECT", font=self.card_header_font, 
                 bg=Config.CARD_WHITE, fg=Config.ACCENT_RED).pack(anchor="w")
        
        self.correction_label = tk.Label(corr_card_frame, text="...", font=self.result_font, 
                                         bg=Config.CARD_WHITE, fg=Config.TEXT_DARK, pady=15)
        self.correction_label.pack(anchor="w")

        # Footer
        tk.Label(self.root, text="Designed for SmartType", font=self.footer_font,
                 bg=Config.BG_COLOR, fg=Config.TEXT_LIGHT).pack(side="bottom", pady=10)

    # ---------------------------------------------------------
    # LOGIC (PRESERVED EXACTLY AS IS)
    # ---------------------------------------------------------

    def load_resources(self):
        # Step 1: Download/Verify NLTK data
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/gutenberg')
        except LookupError:
            nltk.download('gutenberg')

        # Step 1b: Build Bigram Model
        print("Building Bigram Model...")
        words = gutenberg.words()
        
        prev_word = None
        for word in words:
            word = word.lower()
            if not word.isalpha(): 
                continue
                
            if prev_word:
                self.bigram_model[prev_word][word] += 1
            prev_word = word
            
        print("Model Built.")

    def on_key_release(self, event):
        # 1) Get full text
        full_text = self.input_box.get("1.0", "end-1c")
        
        # 2) rpartition to get last word
        head, sep, tail = full_text.rpartition(' ')
        last_word = tail
        
        # 3) If last word is empty (user pressed space), use previous word
        if not last_word and sep:
             _, _, prev = head.rpartition(' ')
             last_word = prev if prev else head
        
        # Clean the word
        clean_word = ''.join(filter(str.isalpha, last_word))
        
        if not clean_word:
            self.correction_label.config(text="...")
            self.prediction_label.config(text="...")
            return

        # 5) SpellChecker
        corrected = self.spell.correction(clean_word)
        if corrected is None:
            corrected = clean_word

        # 6) Show corrected word
        self.correction_label.config(text=f"{corrected}")

        # 7) Search in Bigram Model
        lookup_word = corrected.lower()
        next_words = self.bigram_model.get(lookup_word)

        # 8) Show most probable next word
        if next_words:
            best_guess = next_words.most_common(1)[0][0]
            self.prediction_label.config(text=best_guess)
        else:
            self.prediction_label.config(text="...")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutocorrectKeyboard(root)
    root.mainloop()
