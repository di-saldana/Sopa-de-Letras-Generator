import random
import string
from fpdf import FPDF

# Este fue el script utilizado por chat gpt

# Función para generar una cuadrícula de sopa de letras
def create_wordsearch(words, size=20):
    grid = [['' for _ in range(size)] for _ in range(size)]

    directions = [
        (0, 1), (1, 0), (1, 1), (-1, 1)
    ]

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

# Crear PDF
pdf = FPDF(orientation='P', unit='mm', format='Letter')
pdf.set_auto_page_break(auto=True, margin=10)

# Lista de temas y palabras
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
    "Fe y Espiritualidad": ["Dios", "Jesús", "Espíritu", "Biblia", "Oración", "Iglesia", "Fe", "Ángel", "Paz", "Amor", "Esperanza", "Bendición", "Milagro", "Gracia", "Cielo", "Luz"]
}

# Generar cada página
for title, words in categories.items():
    grid = create_wordsearch(words)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, f"Sopa de Letras - {title}", ln=True)

    pdf.set_font("Courier", size=10)
    for row in grid:
        pdf.cell(0, 6, " ".join(row), ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "Palabras a encontrar:", ln=True)
    pdf.set_font("Arial", size=10)
    for word in words:
        pdf.cell(0, 6, word, ln=True)

# Guardar PDF
pdf_path = "/mnt/data/Sopa_de_Letras_Abuela.pdf"
pdf.output(pdf_path)
pdf_path