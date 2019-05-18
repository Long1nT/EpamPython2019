# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""
from collections import Counter


def is_permutation(a: str, b: str) -> bool:
	a, b = Counter(a), Counter(b)
	return True if a == b else False


assert is_permutation('baba', 'abab')
assert is_permutation('abbba', 'abab')