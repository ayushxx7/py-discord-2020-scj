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
import itertools # for intermediate tc#1

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        # print("Init:",field_type)
        self.field = field_type()

    def __get__(self, obj, objtype): 
        # print("Get:", obj, objtype)
        return self.field
  
    def __set__(self, obj, value): 
        # print("Set:", obj, value)
        if isinstance(value, type(self.field)): 
            # print('value,field_type:',value,self.field)
            self.field = value
        else: 
            print(f"Incorrect Type: {type(value)}. Type should be: {type(self.field)}")
            raise TypeError(f"Incorrect Type: {type(value)}. Type should be: {type(self.field)}") 


class Article:
    """The `Article` class you need to write for the qualifier."""
    

    article_id = itertools.count() #TC201: each article object should have unique id.
    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        """TC101: set values from init"""
        self.id = next(Article.article_id)
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content
        self.last_edited = None

        return None

    def __repr__(self):
        """TC102: class should have repr function"""
        representation = f"<Article title=\"{self.title}\" author='{self.author}' publication_date='{self.publication_date.isoformat()}'>"

        return representation

    def __len__(self):
        """TC103: class should have len function that checks length of content"""
        return len(self.content)

    def short_introduction(self, n_characters):
        """TC104: short intro that returns upto n complete worlds"""
        return textwrap.wrap(self.content, n_characters)[0]

    def most_common_words(self, n):
        """TC105: generate stats of most common n case insensitive worlds. special chars are word boundaries"""
        lower_case_content = self.content.lower()
        split_all_except_lower_alpha = re.split(r'[^a-z]',lower_case_content)
        remove_empty_from_list = list(filter(None, split_all_except_lower_alpha))
        most_common_n_words = dict(Counter(remove_empty_from_list).most_common(n))

        return most_common_n_words

    ### TC202: changing article content should update the last edited time.
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value 
        self.last_edited = datetime.datetime.now()

    ### TC203: articles should be sortable by publication date.
    def __lt__(self, other):
        return self.publication_date < other.publication_date

