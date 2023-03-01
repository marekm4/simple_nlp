import re
from typing import List


def remove_multiple_spaces(text: str) -> str:
    return ' '.join(text.split())


def leave_only_uncased_letters(text: str) -> str:
    return re.sub('[^a-z ]+', '', text.lower())


def remove_stop_words(tokens: List[str]) -> List[str]:
    stop_words = ['the']
    return [token for token in tokens if token not in dict.fromkeys(stop_words)]


def retrieve_semantic_tokens(text: str) -> List[str]:
    text = remove_multiple_spaces(text)
    text = leave_only_uncased_letters(text)
    tokens = remove_stop_words(text.split())
    return tokens
