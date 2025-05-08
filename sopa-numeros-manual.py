import random
import string
from fpdf import FPDF

# Este script fue adaptado del original utilizado por chat gpt. 
# Genera las sopas de numeros manualmente, no con una libreria (numbersearch).

def create_numbersearch(numbers, size=20):
    grid = [['' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    def can_place(number, x, y, dx, dy):
        for i in range(len(number)):
            nx, ny = x + dx*i, y + dy*i
            if not (0 <= nx < size and 0 <= ny < size):
                return False
            if grid[ny][nx] not in ('', number[i]):
                return False
        return True

    def place_number(number):
        attempts = 100
        while attempts > 0:
            dx, dy = random.choice(directions)
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if can_place(number, x, y, dx, dy):
                for i in range(len(number)):
                    grid[y + dy*i][x + dx*i] = number[i]
                return True
            attempts -= 1
        return False

    for number in numbers:
        place_number(number)

    for y in range(size):
        for x in range(size):
            if grid[y][x] == '':
                grid[y][x] = random.choice(string.digits)

    return grid

pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.set_auto_page_break(auto=True, margin=10)

categories = {
    "Lista de Números #1": ["2837401", "5981273", "6403958", "7842039", "1342856", "9482710", "7628391", "3049582", "9283746", "1738495"], # "6203948", "8051739", "2950481", "7602839", "1938472"
    "Lista de Números #2": ["4728193", "6502948", "1928374", "8374620", "9837125", "2049583", "7593021", "1847392", "9083746", "2738491"], # "7462918", "5820394", "3198472", "6250391", "7941820"],
    "Lista de Números #3": ["1839472", "7092846", "2381749", "4628910", "3029481", "7192830", "8547291", "9203847", "1938475", "8462910"], # "1372846", "9283740", "3748291", "6182739", "4928371"],
    "Lista de Números #4": ["5382719", "1748293", "6928471", "3184720", "9823741", "4071928", "2948571", "6382714", "7129843", "8203947"], # "5392847", "7419203", "3958271", "6039482", "2847391"],
}

for title, numbers in categories.items():
    grid = create_numbersearch(numbers)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, f"{title}", ln=True) # Sopa de Letras - {title}
    pdf.set_font("Courier", size=10)
    for row in grid:
        pdf.cell(0, 6, " ".join(row), ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "Números a encontrar:", ln=True) # Palabras
    pdf.set_font("Arial", size=10)
    for number in numbers:
        pdf.cell(0, 6, number, ln=True)

pdf.output("Sopa_de_Numeros_Abuela.pdf")