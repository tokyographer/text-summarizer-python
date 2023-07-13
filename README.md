# Text Summarizer App
GUI app that uses NLTK Natural Language Toolkit to summarize large document files. 
Based on the Python script developed by lmeulen https://github.com/lmeulen/SummarizeText

Algorithm explained here: https://towardsdatascience.com/summarize-a-text-with-python-b3b260c60e72

## Introduction
This is a Python application that provides text summarization functionality. It utilizes the Summarizer class to generate summaries of text based on specific parameters.

## Clone the repository to your local machine.
Install the required dependencies.
Import the Summarizer class into your Python script.
Usage
To create an instance of the Summarizer class and customize its behavior, use the following code:

```python
from summarizer import Summarizer

summarizer = Summarizer(language='english', summary_length=5)
```

The above code instantiates the Summarizer class and assigns it to the variable summarizer. Let's break down the code to understand each part:

Summarizer: This is the name of the class being instantiated. It serves as a blueprint for creating text summarization objects.
language='english': This argument sets the language that the summarizer will use, in this case, English.
summary_length=5: This argument determines the length of the summaries created by the summarizer. Here, it is set to 5 sentences.
The line summarizer = Summarizer(language='english', summary_length=5) creates a new text summarizer with the specified language and summary length, and stores it in the variable summarizer.

Feel free to modify the values of language and summary_length according to your needs.

### Examples
Once you have created an instance of the Summarizer class, you can use its methods to generate summaries. Here's an example:

```python
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae ipsum sit amet metus tristique convallis. Quisque interdum libero nec ligula faucibus, id venenatis magna condimentum. Sed vestibulum, justo at malesuada viverra, ipsum est lobortis nisi, id fringilla velit arcu in elit."

summary = summarizer.summarize(text)
print(summary)
```

In the example above, the summarize method of the summarizer object is called with the text as the input. The method generates a summary based on the specified parameters and returns it. Finally, the summary is printed to the console.

## Conclusion
The Summarizer app provides a convenient way to generate text summaries using Python. By creating an instance of the Summarizer class and specifying the desired language and summary length, you can easily summarize text content in your applications.
