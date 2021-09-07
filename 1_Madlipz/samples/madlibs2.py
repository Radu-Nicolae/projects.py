def madlib():
    adj = input("Adjective: ").lower()
    verb1 = input("Verb 1: ").lower()
    verb2 = input("Verb 2: ").lower()
    famous_person = input("Famous person: ").lower()

    string = f"Python is so {adj}. I am very happy when I {verb1} beacause I" \
             f"love programming. \nBesides, I usually {verb2} when I think about {famous_person}"

    print(string)