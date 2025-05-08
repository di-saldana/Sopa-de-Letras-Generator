from wordsearch import WordSearch
from fpdf import FPDF
import os

# Este Script utiliza la libreria de WordSearch

# Define all categories and words
categories = {
    "Familia": [
        "Cesar", "Julio", "Madelyn", "Filiberto", "Mikal", "Michelle", "Steven", 
        "Danelyn", "Dianelys", "Daynaliz", "Oly"
    ],
    "Bisnietos": [
        "Manuel", "Diego", "King", "Galilea", "Alessandra", "Nikolas", "Maia", "Spot"
    ],
    "Comida Boricua": [
        "Pasteles", "Yuca", "Mofongo", "Pana", "Arroz", "Habichuelas", "Sancocho",
        "Tembleque", "Bacalaitos", "Viandas", "Gandules", "Aguacate", "Alcapurrias",
        "Tostones", "Ñame"
    ],
    "Vegetales": [
        "Zanahoria", "Brócoli", "Lechuga", "Ajo", "Cebolla", "Tomate", "Pimiento", 
        "Pepinillo", "Calabaza", "Apio", "Espinaca", "Berenjena", "Papa", "Ñame", "Yuca"
    ],
    "Frutas": [
        "Mangó", "Piña", "Guayaba", "Papaya", "Coco", "Plátano", "Guineo", "Parcha", 
        "Tamarindo", "Toronja", "Limón", "Acerola", "Uva", "Melón", "Carambola"
    ],
    "Cosas de Costura": [
        "Aguja", "Hilo", "Tijeras", "Dedal", "Botón", "Zipper", "Alfiler", "Tela", 
        "Encaje", "Costura", "Máquina", "Cinta", "Bordado", "Puntada", "Bobina"
    ],
    "Flora de Puerto Rico": [
        "Amapola", "Maga", "Flamboyán", "Ceiba", "Palma", "Yagrumo", "Roble", 
        "Hibisco", "Helecho", "Orquídea", "Tabonuco", "Guayacán", "Mamey"
    ],
    "Fauna de Puerto Rico": [
        "Cotorra", "Boa", "Coquí", "Iguana", "Jutía", "Múcaro", "Manatí", "Cobo", 
        "Culebra", "Carey", "Zorzal", "Tinglar", "Concho", "Gallo"
    ],
    "Pueblos de Puerto Rico": [
        "Mayagüez", "Cabo Rojo", "Hormigueros", "San Juan", "Ponce", "Bayamón", 
        "Arecibo", "Fajardo", "Humacao", "Guayama", "Manatí", "Aguadilla", 
        "Utuado", "Adjuntas", "Cidra", "Vieques"
    ],
    "Apóstoles de Jesús": [
        "Andrés", "Bartolomé", "Santiago Alfeo", "Santiago Zebedeo", "Juan", 
        "Judas Tadeo", "Mateo", "Pedro", "Felipe", "Simón", "Tomás", "Judas Iscariote"
    ],
    "Cantantes Cristianos": [
        "Samuel Hernández", "Jesús Adrián Romero", "Daniel Calveti", "Christine D'Clario",
        "Marcela Gándara", "Danny Berrios", "Alex Zurdo", "Alex Campos", 
        "Marco Barrientos", "Marcos Yaroide"
    ],
    "Fe y Espiritualidad": [
        "Dios", "Jesús", "Espíritu", "Biblia", "Oración", "Iglesia", "Fe", "Ángel", 
        "Paz", "Amor", "Esperanza", "Bendición", "Milagro", "Gracia", "Cielo", "Luz"
    ]
}

# Create PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=10)

# Generate word searches and add to PDF
for title, words in categories.items():
    ws = WordSearch(words, height=20, width=20)
    grid = ws.grid
    solution = ws.solution

    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Sopa de Letras: {title}", ln=True)

    # Print grid
    pdf.set_font("Courier", size=10)
    for row in grid:
        line = " ".join(row)
        pdf.cell(0, 7, line, ln=True)

    # Print word list
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Palabras:", ln=True)
    pdf.set_font("Arial", size=10)
    for word in words:
        pdf.cell(0, 6, word, ln=True)

# Save PDF
output_path = "/mnt/data/sopa_de_letras_abuela.pdf"
pdf.output(output_path)
output_path
