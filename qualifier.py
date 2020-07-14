"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import textwrap # for TC#4 (short_introduction)

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

        return None

    def __repr__(self):

        formatted_datetime = self.publication_date.strftime(
            "%Y-%m-%dT%H:%M:%S")
        representation = f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{formatted_datetime}'>"

        return representation

    def __len__(self):

        return len(self.content)
    
    def short_introduction(self, n_characters):

        return textwrap.wrap(self.content, n_characters)[0]
    
    def most_common_words(self, n):
       
        from collections import Counter 
          
        # split() returns list of all the words in the string 
        split_it = self.content.split() 
          
        # Pass the split_it list to instance of Counter class. 
        Counter = Counter(split_it) 
  
        # most_common() produces k frequently encountered 
        # input values and their respective counts. 
        most_occur = dict(Counter.most_common(n))


        return most_occur

