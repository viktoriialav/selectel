from dataclasses import dataclass


@dataclass
class Text:
    input: str
    output: str


text_for_positive_search = Text(
    input='облачные серверы',
    output='Аренда облачного сервера | Cloud-хостинг от Selectel'
)

text_for_negative_search = Text(
    input='екнурввивщдыбсдллиыдмфифмивиамгшывамииагшиук',
    output='По вашему запросу ничего не найдено. Попробуйте изменить формулировку.'
)
