import sys

sys.path.append("ner_system")


from system import show_ners



def test_show_ners():
    ners = show_ners(string="Apple is a company of John Doe", language="en")

    assert ners == [
        {"text": "Apple", "type": "ORG", "start_pos": 0, "end_pos": 1},
        {"text": "John Doe", "type": "PERSON", "start_pos": 5, "end_pos": 7},
    ]
