def sprawdz_poprawnosc_symboli(symbole):
    stos = []
    dopasowanie = {
        '}': '{',
        ']': '[',
        '>': '<',
        ')': '(',
        '"': '"',
        "'": "'",
        '}': '{',
        ']': '[',
        '>': '<',
    }

    for symbol in symbole:
        if symbol in dopasowanie.values():
            stos.append(symbol)
        elif symbol in dopasowanie.keys():
            if len(stos) == 0 or stos.pop() != dopasowanie[symbol]:
                return False

    return len(stos) == 0

symbole = "{[<abc>]} 'sample'"
if sprawdz_poprawnosc_symboli(symbole):
    print("Symbole są poprawne.")
else:
    print("Symbole są niepoprawne.")