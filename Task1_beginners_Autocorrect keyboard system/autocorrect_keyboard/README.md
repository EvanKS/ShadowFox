# SmartType

A real-time Autocorrect Keyboard System with Next Word Prediction using Python, Tkinter, and NLTK.

## Objective
To build a smart keyboard interface that:
1.  Detects misspelled words in real-time.
2.  Autocorrects the current word.
3.  Predicts the next likely word based on a Bigram model trained on the Gutenberg corpus.

## Libraries Used
-   **Tkinter**: For the Graphical User Interface (GUI).
-   **Pyspellchecker**: For detecting and correcting misspelled words.
-   **NLTK (Natural Language Toolkit)**: For building the N-gram (Bigram) language model using the Gutenberg corpus.

## How to Run

1.  **Install Dependencies**:
    Open a terminal/command prompt in this directory and run:
    ```bash
    pip install -r requirements.txt
    ```

    *Note: If you have issues installing `pyspellchecker'`, try `pip install pyspellchecker`.*

2.  **Run the Application**:
    ```bash
    python main.py
    ```

3.  **Usage**:
    -   Wait for the "System Ready" message (it downloads NLTK data and builds the model on first run).
    -   Start typing in the large text box.
    -   See real-time **Corrections** on the bottom left.
    -   See **Next Word Predictions** on the bottom right.

## Features
-   **Real-time Processing**: Updates on every key release.
-   **Smart Correction**: Fixes typos instantly.
-   **Context Prediction**: Suggests the next word based on English literature patterns.
-   **Modern UI**: Dark-themed, clean interface with distinct panels.

