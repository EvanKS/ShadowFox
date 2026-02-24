#  SmartType – Intelligent Autocorrect & Next Word Prediction System

##  Problem Statement

Develop an autocorrect keyboard system that anticipates the next word in a sentence by leveraging contextual information provided by preceding words.

This project involves implementing **N-gram language modeling** to enhance predictive capabilities and create an intuitive keyboard interface that improves user experience by:

- Detecting and correcting spelling errors in real-time
- Predicting the next likely word based on context
- Facilitating efficient and error-free text input

---

##  Project Objective

The goal of this project is to:

- Build a real-time smart keyboard system
- Implement autocorrection using probabilistic spell checking
- Use **Bigram (2-gram) language modeling** for next-word prediction
- Enhance typing efficiency through contextual suggestions
- Provide a clean and interactive graphical interface

---

## 🛠 Technologies & Libraries Used

- **Python**
- **Tkinter** – GUI development
- **NLTK (Natural Language Toolkit)** – N-gram language modeling
- **PySpellChecker** – Spell correction
- **Gutenberg Corpus (NLTK dataset)** – Training data source

---

##  Core NLP Concepts Used

### 1️⃣ N-Gram Language Modeling (Bigram Model)

The system uses a **Bigram model**, which predicts the next word based on the previous word:

\[
P(w_n | w_{n-1})
\]

Example:
If the user types:

```
thank you
```

The system predicts:
```
much
```

Because in the training corpus, "you much" appears frequently in context.

---

### 2️⃣ Autocorrect Mechanism

- Detects misspelled words using `PySpellChecker`
- Suggests the most probable correction
- Updates suggestions dynamically as the user types

Example:
```
hello evan hwo
```

Autocorrect suggests:
```
how
```

---

##  System Features

###  Real-Time Processing
Updates suggestions on every key release event.

###  Smart Autocorrection
Corrects typos instantly based on probability scoring.

###  Context-Based Prediction
Uses Bigram frequency distribution to suggest the next word.

###  Interactive GUI
- Large typing area
- Separate panels for:
  - Next Word Prediction
  - Autocorrect Suggestions
- "System Ready" indicator

---

## 📂 Project Structure

```
Task1_Beginner_Autocorrect_Keyboard_System/
│
├── main.py
├── ui_demo.py
├── requirements.txt
└── README.md
```

---

##  How to Run the Project

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

If needed:

```bash
pip install nltk pyspellchecker
```

---

### Step 2: Download NLTK Data (First Time Only)

```python
import nltk
nltk.download('gutenberg')
nltk.download('punkt')
```

---

### Step 3: Run the Application

```bash
python main.py
```

---

### Step 4: Usage

- Wait for the **"System Ready"** indicator.
- Start typing in the typing area.
- View:
  -  Next Word Prediction (bottom left)
  -  Autocorrect Suggestion (bottom right)

---

## 📊 Example Outputs

| User Input            | Autocorrect | Next Word Prediction |
|----------------------|------------|----------------------|
| hello evan hwo       | how        | much                 |
| thank you so         | so         | much                 |

---

##  Key Highlights

- Implements probabilistic NLP model using real corpus data
- Demonstrates contextual understanding using N-grams
- Real-time event-driven processing
- Combines GUI + NLP + Language Modeling
- Lightweight and efficient implementation

---

##  Future Enhancements

- Upgrade from Bigram to Trigram model
- Implement RNN / LSTM based neural language model
- Add auto-complete suggestions list
- Improve UI with suggestion click selection
- Add mobile keyboard integration concept

---

##  Conclusion

SmartType successfully demonstrates the implementation of an intelligent keyboard system using NLP techniques.

By combining:

- N-gram language modeling
- Spell correction algorithms
- Real-time GUI interaction

The system enhances typing efficiency and improves user experience through contextual prediction and error correction.

This project showcases practical application of Natural Language Processing concepts in real-world user interfaces.

---

## 👨‍💻 Author

**Evan KS**  
AIML Intern – ShadowFox  
