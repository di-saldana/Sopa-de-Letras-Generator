import random
import string
import os
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

# Add Unicode font for grid (monospace for better alignment)
unicode_font_path = None
unicode_font_name = None
possible_paths = [
    '/System/Library/Fonts/Supplemental/Courier New.ttf',  # Monospace Unicode font
    '/Library/Fonts/Courier New.ttf',
    '/System/Library/Fonts/Supplemental/Arial.ttf',  # Fallback
    '/Library/Fonts/Arial.ttf',
]
for path in possible_paths:
    if os.path.exists(path):
        unicode_font_path = path
        break

if unicode_font_path:
    try:
        # Use Courier New for monospace grid, or Arial as fallback
        unicode_font_name = 'CourierNewUnicode' if 'Courier' in unicode_font_path else 'ArialUnicode'
        pdf.add_font(unicode_font_name, '', unicode_font_path)
        pdf.add_font(unicode_font_name, 'B', unicode_font_path)
    except Exception as e:
        # If font loading fails, we'll use a workaround
        print(f"Warning: Could not load Unicode font: {e}")
        unicode_font_path = None
        unicode_font_name = None

# NO DEJAR ESPACIOS ENTRE LAS PALABRAS
categories = {
    "Heated Rivalry": [
        "Heated", "Rivalry", "Hockey", "Enemies", "Lovers", "Canada", "Shane", "Hollander", "Ilya", "Rozanov", "Hudson", "Connor", "Storrie", "Rachel", "Reid", "HBO"
    ],
    
    "NBA: Timberwolves": [
        "Anthony", "Edwards", "Rudy", "Gobert", "Naz", "Reid", "Julius", "Randle", "Donte", "DiVincenzo", "Mike", "Conley", "Jaden", "McDaniels", "Rob", "Dillingham"
    ],

    "Letterboxd: Best movies of 2026": [
        "The Odyssey", "Wuthering Heights", "Practical Magic 2", "The Bride", "Digger", "Toy Story 5", "The Drama", "Mother Mary", "Dune Messiah", "The Sheep Detectives", "Hoppers", "Bugonia", "Sinners", "Hamnet"
    ],

    "Sephora Brands": [
        "Fenty", "Patrick Ta", "Huda", "NARS", "Too Faced", "Urban Decay", "One Size", "Tower 28", "Laura Mercier",  "Charlotte Tilbury", "Tarte", "Morphe", "Glossier", "Makeup by Mario", "Haus Labs"
    ],
    
    "Harry Styles - Harry Styles (2017)": [
        "Sign of the Times", "Carolina", "Two Ghosts", "Sweet Creature", "Only Angel",
        "Kiwi", "Ever Since New York", "Woman", "Meet Me in the Hallway", "From the Dining Table"
    ],

    "Harry Styles - Fine Line (2019)": [
        "Golden", "Watermelon Sugar", "Adore You", "Lights Up", "Cherry", "Falling", "Treat People With Kindness",
        "She", "To Be So Lonely", "Sunflower", "Canyon Moon", "Fine Line"
    ],

    "Harry Styles - Harry's House (2022)": [
        "As It Was", "Late Night Talking", "Matilda", "Cinema", "Boyfriends",
        "Daylight", "Grapejuice", "Love of My Life", "Keep Driving", "Satellite", "Little Freak", "Daydreaming", "Music for a Sushi Restaurant"
    ],

    "One Direction - Up All Night (2011)": [
        "What Makes You Beautiful", "Gotta Be You", "One Thing", "More Than This",
        "Up All Night", "I Wish", "Tell Me a Lie", "Taken", "I Want", "Everything About You", "Moments", "Same Mistakes"
    ],

    "One Direction - Take Me Home (2012)": [
        "Live While Were Young", "Kiss You", "Little Things", "Cmon Cmon", "Last First Kiss", "Heart Attack", "They Dont Know About Us",
        "Over Again", "Rock Me", "Summer Love", "Loved You First", "Change My Mind", "I Would", "Magic"
    ],

    "One Direction - Midnight Memories (2013)": [
        "Best Song Ever", "Story of My Life", "Midnight Memories", "You and I", "Something Great",
        "Strong", "Happily", "Little Black Dress", "Diana", "Through the Dark", "Right Now", "Little White Lies", "Alive", "Half A Heart"
    ],

    "One Direction - FOUR (2014)": [
        "Steal My Girl", "Night Changes", "No Control", "Fireproof", "Girl Almighty", "Stockholm Syndrome",
        "Ready to Run", "Fools Gold", "Clouds", "Spaces", "Where Do Broken Hearts Go", "18", "Illusion"
    ],

    "One Direction - Made in the A.M. (2015)": [
        "Drag Me Down", "Perfect", "Infinity", "History", "Long Way Down", "Never Enough", "Olivia", "Wolves", "A.M.",
        "Love You Goodbye", "End of the Day", "What a Feeling", "If I Could Fly", "Hey Angel", "Temporary Fix", "Walking in the Wind"
    ],

    "Bad Bunny - X100PRE (2018)": [
        "Ni Bien Ni Mal", "200 MPH", "Caro",
        "Tenemos Que Hablar", "Otra Noche En Miami", "Mía", "Solo de Mí",
        "La Romana", "Si Estuviésemos Juntos", "Estamos Bien", "Como Antes",
        "Bye Me Fui"
    ],

    "Bad Bunny - YHLQMDLG (2020)": [
        "Pero Ya No", "La Difícil", "Bichiyal", "Hablamos Mañana",
        "Safaera", "La Santa", "Yo Perreo Sola", "Vete", "Ignorantes", "A Tu Merced", "25/8",
        "<3", "Soliá"
    ],

    "Bad Bunny - El Último Tour del Mundo (2020)": [
        "Dakiti", "Yo Visto Así", "Hoy Cobré", "Booker T",
        "La Noche de Anoche", "Te Deseo Lo Mejor", "Haciendo Que Me Amas",
        "120", "Antes Que Se Acabe", "El Mundo Es Mío", "Te Mudaste"
    ],

    "Bad Bunny - Un Verano Sin Ti (2022)": [
        "Moscow Mule", "Después de la Playa", "Me Porto Bonito", "Tití Me Preguntó",
        "Un Ratito", "Yo No Soy Celoso", "Tarot", "Neverita",
        "La Corriente", "Efecto", "Party", "Aguacero",
        "Enséñame a Bailar", "Ojitos Lindos", "Dos Mil 16", "El Apagón",
        "Otro Atardecer", "Un Coco", "Andrea", "Agosto"
    ],

    "BB - Nadie Sabe Lo Que Va a Pasar Mañana (2023)": [
        "Nadie Sabe", "Monaco", "Fina", "Hibiki", "Mr October",
        "Cybertruck", "Vou 787", "Seda", "Teléfono Nuevo",
        "Baby Nueva", "Mercedes Carota", "Los Pits", 
        "Baticano", "No Me Quiero Casar", "Thunder y Lightning", "Acho PR"
    ], 

    "Bad Bunny - DtMF (2025)": [
        "NUEVAYoL", "BAILE INoLVIDABLE", "VeLDÁ", "KETU TeCRÉ", "BOKeTE", "KLOuFRENS", "EoO", "LA MuDANZA", "WELTiTA", "TURiSTA", "DtMF", "LA MuDANZA"
    ],
}


for title, words in categories.items():
    # Remove spaces from words for grid placement, but keep original for display
    words_for_grid = [word.replace(' ', '') for word in words]
    grid = create_wordsearch(words_for_grid)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 20)
    pdf.cell(0, 10, f"{title}", ln=True)
    # Use Unicode font if available, otherwise use Courier (may have issues with special chars)
    if unicode_font_name:
        pdf.set_font(unicode_font_name, size=13)
    else:
        pdf.set_font("Courier", size=13)
    pdf.ln(6)
    for row in grid:
        pdf.cell(0, 6, " ".join(row), ln=True)

    pdf.ln(4)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Palabras a encontrar:", ln=True)
    if unicode_font_name:
        pdf.set_font(unicode_font_name, size=13)
    else:
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

pdf.output("Sopa_de_Letras_Kenya.pdf")