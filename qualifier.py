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
from collections import Counter # for TC#5 (most n words)
import re # for TC#5 (most n words)

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
       
        lower_case_content = self.content.lower()
        split_all_except_lower_alpha = re.split(r'[^a-z]',lower_case_content)
        remove_empty_from_list = list(filter(None, split_all_except_lower_alpha))
        most_common_n_words = dict(Counter(remove_empty_from_list).most_common(n))

        return most_common_n_words

