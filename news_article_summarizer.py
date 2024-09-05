import tkinter as tk
import nltk

from textblob import TextBlob
from newspaper import Article

def summarize():
    url = utext.get('1.0', "end").strip()
    article = Article(url)
    article.download()
    article.parse()
    
    # Perform NLP on the article
    article.nlp()

    # Enable the text boxes to insert content
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    # Clear existing content
    title.delete('1.0', 'end')
    author.delete('1.0', 'end')
    publication.delete('1.0', 'end')
    summary.delete('1.0', 'end')
    sentiment.delete('1.0', 'end')

    # Insert new content
    title.insert('1.0', article.title)
    author.insert('1.0', ', '.join(article.authors))  # Convert the list to a string

    # Check if publish_date is None, and handle it
    if article.publish_date:
        publication.insert('1.0', article.publish_date)
    else:
        publication.insert('1.0', "Unknown")

    summary.insert('1.0', article.summary)

    # Perform sentiment analysis
    analysis = TextBlob(article.text)
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

    # Disable the text boxes again
    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')


   

root = tk.Tk()
root.title('News Analysis')
root.geometry('1200x600')

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text="Author")
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text="Publishing Date")
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text="URL")
ulabel.pack()

utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()