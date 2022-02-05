# Requirements:
```
- python3.7
- create separate environment
- activate it and install requirements
- install at least one model: python -m spacy download en_core_web_sm
```

# Run script:
```
python ner_system --string "Apple is a company of John Doe" --language en
[{'text': 'Apple', 'type': 'ORG', 'start_pos': 0, 'end_pos': 1}, {'text': 'John Doe', 'type': 'PERSON', 'start_pos': 5, 'end_pos': 7}]
```

# Error handling
In the case when `LanguageError` is raised, please download proper model and add key and value to the `LANGUAGE_MAP` in `ner_system/ner_system.py`:

```
"your_language_model_code": "spacy_language_name"
```


# Run tests:
```
pytest
```