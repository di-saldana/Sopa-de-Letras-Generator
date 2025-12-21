import random
import string
from fpdf import FPDF

# Este script fue adaptado del original utilizado por chat gpt. 
# Genera las sopas de letra manualmente, no con una libreria (WordSearch).

def create_wordsearch(words, size=32):
    grid = [['' for _ in range(size)] for _ in range(size)]
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    def can_place(word, x, y, dx, dy):
        for i in range(len(word)):
            nx, ny = x + dx*i, y + dy*i
            if not (0 <= nx < size and 0 <= ny < size):
                return False
            if grid[ny][nx] not in ('', word[i]):
                return False
        return True

    def place_word(word):
        attempts = 100
        word = word.upper()
        while attempts > 0:
            dx, dy = random.choice(directions)
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            if can_place(word, x, y, dx, dy):
                for i in range(len(word)):
                    grid[y + dy*i][x + dx*i] = word[i]
                return True
            attempts -= 1
        return False

    for word in words:
        place_word(word)

    for y in range(size):
        for x in range(size):
            if grid[y][x] == '':
                grid[y][x] = random.choice(string.ascii_uppercase)

    return grid

pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.set_margins(20, 10, 10)  # left, top, right margins in mm
pdf.set_auto_page_break(auto=True, margin=10)  # bottom margin in mm

# NO DEJAR ESPACIOS ENTRE LAS PALABRAS
categories = {
    "Familia": ["Cesar", "Julio", "Madelyn", "Filiberto", "Mikal", "Michelle", "Steven", "Danelyn", "Dianelys", "Daynaliz", "Oly"],
    "Bisnietos": ["Manuel", "Diego", "King", "Galilea", "Alessandra", "Nikolas", "Maia", "Spot"],
    "Comida Boricua": ["Pasteles", "Yuca", "Mofongo", "Pana", "Arroz", "Habichuelas", "Sancocho", "Tembleque", "Bacalaitos", "Viandas", "Gandules", "Aguacate", "Alcapurrias", "Tostones", "Ñame"],
    "Vegetales": ["Zanahoria", "Brócoli", "Lechuga", "Ajo", "Cebolla", "Tomate", "Pimiento", "Pepinillo", "Calabaza", "Apio", "Espinaca", "Berenjena", "Papa", "Ñame", "Yuca"],
    "Frutas": ["Mangó", "Piña", "Guayaba", "Papaya", "Coco", "Plátano", "Guineo", "Parcha", "Tamarindo", "Toronja", "Limón", "Acerola", "Uva", "Melón", "Carambola"],
    "Cosas de Costura": ["Aguja", "Hilo", "Tijeras", "Dedal", "Botón", "Zipper", "Alfiler", "Tela", "Encaje", "Costura", "Máquina", "Cinta", "Bordado", "Puntada", "Bobina"],
    "Flora de Puerto Rico": ["Amapola", "Maga", "Flamboyán", "Ceiba", "Palma", "Yagrumo", "Roble", "Hibisco", "Helecho", "Orquídea", "Tabonuco", "Guayacán", "Mamey"],
    "Fauna de Puerto Rico": ["Cotorra", "Boa", "Coquí", "Iguana", "Jutía", "Múcaro", "Manatí", "Cobo", "Culebra", "Carey", "Zorzal", "Tinglar", "Concho", "Gallo"],
    "Pueblos de Puerto Rico": ["Mayagüez", "Cabo Rojo", "Hormigueros", "San Juan", "Ponce", "Bayamón", "Arecibo", "Fajardo", "Humacao", "Guayama", "Manatí", "Aguadilla", "Utuado", "Adjuntas", "Cidra", "Vieques"],
    "Apóstoles de Jesús": ["Andrés", "Bartolomé", "Santiago Alfeo", "Santiago Zebedeo", "Juan", "Judas Tadeo", "Mateo", "Pedro", "Felipe", "Simón", "Tomás", "Judas Iscariote"],
    "Cantantes Cristianos": ["Samuel Hernández", "Jesús Adrián Romero", "Daniel Calveti", "Christine D'Clario", "Marcela Gándara", "Danny Berrios", "Alex Zurdo", "Alex Campos", "Marco Barrientos", "Marcos Yaroide"],
    "Fe y Espiritualidad": ["Dios", "Jesús", "Espíritu", "Biblia", "Oración", "Iglesia", "Fe", "Ángel", "Paz", "Amor", "Esperanza", "Bendición", "Milagro", "Gracia", "Cielo", "Luz"],
}

for title, words in categories.items():
    grid = create_wordsearch(words)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, f"{title}", ln=True)
    pdf.set_font("Courier", size=13)
    pdf.ln(6)
    for row in grid:
        pdf.cell(0, 6, " ".join(row), ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Palabras a encontrar:", ln=True)
    pdf.set_font("Arial", size=10)
    
    # Calculate number of columns (at least 4 words per column)
    words_per_column = 4
    num_columns = max(1, (len(words) + words_per_column - 1) // words_per_column)
    column_width = 180 / num_columns  # Page width is 210mm, minus 20mm left and 10mm right margins
    start_y = pdf.get_y()
    
    # Distribute words across columns
    words_per_col = (len(words) + num_columns - 1) // num_columns
    for i, word in enumerate(words):
        col = i // words_per_col
        row_in_col = i % words_per_col
        x = pdf.l_margin + col * column_width  # Use left margin (20mm) instead of hardcoded value
        y = start_y + row_in_col * 6
        pdf.set_xy(x, y)
        pdf.cell(column_width, 6, word)

pdf.output("Sopa_de_Letras_Abuela.pdf")