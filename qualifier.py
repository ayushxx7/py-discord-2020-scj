#### LIBRARIES ####
import datetime
import typing
import textwrap # for TC#104 (short_introduction)
from collections import Counter # for TC#105 (most common n words)
import re # for TC#105 (most common n words)
import itertools # for intermediate tc#201: (article should have unique id)
####

class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    #TC301: should be able to get and set values of any valid type (including custom types).
    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field = field_type()

    #TC302: each object/instance should have separate values.
    def __get__(self, obj, objtype): 
        return obj.field
  
    #TC301: should be able to get and set values of any valid type.
    def __set__(self, obj, value): 
        if isinstance(value, type(self.field)): 
            #TC302: each object/instance should have separate values.
            obj.field = value
        else: 
            print(f"Incorrect Type: {type(value)}. Type should be: {type(self.field)} ||| {self.name}")
            #TC302: wrong assignment should raise type error. 
            #TC304: type error should have attribute name, expected type, actual type.
            raise TypeError(f"expected an instance of type '{type(self.field).__name__}' for attribute '{self.name}', got '{type(value).__name__}' instead") 
    
    #TC304: type error should have attribute name, expected type, actual type.
    def __set_name__(self, owner, name):
        self.name = name

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

    ### TC202: changing article content should update the last edited time.
    @content.setter
    def content(self, value):
        self._content = value 
        self.last_edited = datetime.datetime.now()

    def __lt__(self, other):
        """TC203: articles should be sortable by publication date."""
        return self.publication_date < other.publication_date

