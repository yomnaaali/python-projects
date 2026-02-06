import random
import webbrowser

def open_random_website():
    websites = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.stackoverflow.com",
        "https://www.github.com",
        "https://www.iti.gov.eg",
    ]

    chosen = random.choice(websites)
    print("Opening:", chosen)
    webbrowser.open(chosen)

if __name__ == "__main__":
    open_random_website()
