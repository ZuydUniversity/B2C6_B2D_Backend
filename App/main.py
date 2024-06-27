# fatsoenlijke main.py: copie van ./main.py, maar in ./App/
# - nodig voor Docker (zodat ./App/ kan worden gecopieerd)
# - oorspronkelijk ./main.py verwijderen gaat branches breken)

from App import initializeApp

app = initializeApp()
