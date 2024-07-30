def test_add_to_phonebook(phonebook):
    phonebook.add('Jan Kowalski', 123456789)
    assert len(phonebook.contacts) == 1


def test_lookup_by_name(phonebook):
    phonebook.add('Jan Kowalski', 123456789)
    number = phonebook.lookup('Jan Kowalski')
    assert number == 123456789
