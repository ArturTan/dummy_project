import spacy
from typing import Any, Dict, List
from dataclasses import dataclass, asdict
from ner_system.language_map import LANGUAGE_MAP


@dataclass
class Entity:
    text: str
    type: str
    start_pos: int
    end_pos: int


EntityType = Dict[str, Any]


class LanguageError(Exception):
    pass


def show_ners(string: str, language: str) -> List[EntityType]:
    try:
        nlp_handler = spacy.load(LANGUAGE_MAP[language])
    except KeyError:
        raise LanguageError(f"Language {language} does not exist in language map")
    doc = nlp_handler(string)
    entities = [
        Entity(word.text, word.label_, word.start, word.end) for word in doc.ents
    ]
    return [asdict(entity) for entity in entities]
