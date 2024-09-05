# 📰 News Article Summarizer using Python

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [How It Works](#how-it-works)
6. [Screenshots](#screenshots)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)
10. [Contact](#contact)

## Introduction

The **News Article Summarizer** is a Python-based application that allows users to input the URL of any news article and generates a concise summary along with sentiment analysis. It’s designed to help users quickly grasp the key points of an article and understand its tone—whether positive, negative, or neutral.

The project leverages several Python libraries, including `nltk`, `TextBlob`, and `newspaper3k`, to process and analyze the article's content. The user-friendly interface is built using `tkinter`, allowing for a seamless experience.

## Features

- **Article Extraction**: Automatically parses the article content from a URL using the `newspaper3k` library.
- **Summarization**: Condenses the article to its key points using NLP techniques.
- **Sentiment Analysis**: Determines the overall sentiment (positive, negative, or neutral) of the article using `TextBlob`.
- **User-Friendly Interface**: Built with `tkinter` for ease of use.
- **Multi-Output**: Displays the article’s title, authors, publication date, summary, and sentiment analysis.

## Tech Stack

- **Python**: Core language
- **tkinter**: For building the graphical user interface
- **nltk**: Natural Language Toolkit for text processing
- **TextBlob**: For sentiment analysis
- **newspaper3k**: For extracting news articles from web pages

## Installation

Follow these steps to set up the project locally:

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/news-article-summarizer.git
cd news-article-summarizer
```

### 2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
```bash
python news_article_summarizer.py
```

## How It Works

1. **Input URL**: The user enters the URL of the news article they want summarized.
2. **Article Parsing**: The `newspaper3k` library scrapes the content of the article from the URL.
3. **Summarization**: The article is summarized using NLP techniques.
4. **Sentiment Analysis**: The `TextBlob` library determines the polarity of the article, indicating whether the sentiment is positive, negative, or neutral.
5. **Output**: The summarized content, along with key details such as the title, author(s), publication date, and sentiment analysis, is displayed in the GUI.

## Usage

1. Open the application by running the command:
   ```bash
   python news_article_summarizer.py
   ```
2. Enter the URL of a news article into the text field.
3. Click the **"Summarize"** button.
4. The summarized content will be displayed, including:
   - **Title**
   - **Authors**
   - **Publication Date**
   - **Summary**
   - **Sentiment Analysis**

## Contributing

We welcome contributions! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions about this project, feel free to contact me:

- LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/sambadi-sen-data-and-business-analyst-in-kolkata/)
- GitHub: [Your GitHub Profile](https://github.com/sambadi1012)
