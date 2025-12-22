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

    "pueblos de puerto rico 1": [
        "adjuntas", "aguada", "aguadilla", "aguas buenas", "aibonito",
        "arecibo", "arroyo", "barceloneta", "cabo rojo", "caguas",
        "camuy", "canóvanas", "carolina", "cataño", "cayey"
    ],

    "pueblos de puerto rico 2": [
        "ceiba", "ciales", "cidra", "coamo", "comerío",
        "corozal", "culebra", "dorado", "fajardo", "florida",
        "guanica", "guayama", "guayanilla", "guaynabo", "gurabo"
    ],

    "pueblos de puerto rico 3": [
        "hatillo", "hormigueros", "humacao", "isabela", "jayuya",
        "juana díaz", "juncos", "lajas", "lares", "las marías",
        "las piedras", "loíza", "luquillo", "manatí", "maricao"
    ],

    "pueblos de puerto rico 4": [
        "mayagüez", "moca", "morovis", "naguabo", "naranjito",
        "orocovis", "patillas", "peñuelas", "ponce", "quebradillas",
        "rincón", "rio grande", "salinas", "san germán"
    ],

    "pueblos de puerto rico 5": [
        "san juan", "san lorenzo", "san sebastián", "santa isabel",
        "toa alta", "toa baja", "trujillo alto", "utuado",
        "vega alta", "vega baja", "vieques", "villalba", "yabucoa", "yauco"
    ],

    "navidad boricua": [
        "parranda", "lechón", "arroz", "gandules", "pasteles", "coquito",
        "trulla", "aguinaldo", "asalto", "jíbaro", "cuatro",
        "vejigantes", "bembé", "villancico", "güiro"
    ],

    "comidas típicas de puerto rico": [
        "mofongo", "tostones", "alcapurria", "bacalaíto", "tembleque",
        "coquito", "flan", "asopao", "sancocho", "sorullos",
        "piragua", "pionono", "quesito", "empanadillas", "tripleta"
    ],

    "costumbres boricuas": [
        "parrandear", "chinchorrear", "patronales", "trova",
        "plena", "bomba", "vejigante", "reyes", "sanse"
    ],

    "frutas tropicales": [
        "mangó", "papaya", "guanábana", "piña", "tamarindo",
        "quenepa", "guayaba", "coco", "acerola",
        "jagua", "níspero", "higuera", "parcha"
    ],

    "playas de puerto rico": [
        "flamenco", "crash boat", "buyé", "boquerón", "playa sucia",
        "steps", "survival", "jobos", "domes", "piñones",
        "luquillo", "ocean park", "isla verde", "combate", "posita"
    ],

    "palabras boricuas": [
        "acho", "brutal", "jangueo", "zafacón", "bregar", "al garete",
        "embuste", "gufeo", "pana", "chavos", "ñangotao",
        "fiao", "revolú", "cantazo", "jíbaro", "mano", "chevere",
        "nítido", "guagua", "corillo"
    ],

    "música boricua": [
        "reggaeton", "salsa", "plena", "bomba", "merengue",
        "bolero", "trap", "guaracha", "parranda", "trova"
    ],

    "animales del caribe": [
        "coquí", "guaraguao", "manatí", "tinglar", "carey",
        "murciélago", "jutía", "sapo concho", "juey",
        "pelícano", "tiburón", "delfín", "pezleón", "garza"
    ],

    "flora de borinquen": [
        "ceiba", "maga", "yagrumo", "flamboyán", "palmareal",
        "bambú", "helecho", "orquídea", "amapola",
        "ucar", "roble", "manglar", "nigua"
    ],

    "próceres boricuas": [
        "betances", "hostos", "albizu", "muñóz rivera", "lolita",
        "blanca canales", "baldorioty", "de diego",
        "julia de burgos", "roberto clemente"
    ],

    "pasteles puertorriqueños": [
        "masa", "hoja", "hilo", "achiote", "cerdo", "viandas",
        "plátano", "guineo", "yuca", "sofrito", "garbanzos",
        "caldo", "hoja de plátano", "amarrar", "pastel"
    ],

    "vegetales del caribe": [
        "yuca", "yautía", "ñame", "calabaza",
        "aguacate", "batata", "pana", "guineo",
        "berenjena", "pimiento", "cebolla",
        "ajo", "apio", "recao"
    ],

    "mariscos caribeños": [
        "camarón", "pulpo", "langosta", "carrucho",
        "mero", "dorado", "chapín", "chillo",
        "atún", "cangrejo", "ostión", "almeja",
        "caracol", "cazón", "pargo"
    ],

    "deportes populares en puerto rico": [
        "béisbol", "baloncesto", "boxeo", "voleibol",
        "atletismo", "tenis", "natación", "judo",
        "lucha", "gimnasia", "fútbol", "surf",
        "pesca", "ciclismo", "ajedrez"
    ],

    "deportistas puertorriqueños": [
        "roberto clemente", "tito trinidad", "miguel cotto",
        "mónica puig", "ivan rodríguez", "carlos delgado",
        "edwin díaz", "francisco lindor", "yadier molina",
        "javier báez", "alex cintrón",
    ],

    "proceres puertorriqueños": [
        "betances", "hostos",
        "muñoz rivera", "lola rodz de tió",
        "josé de diego",
        "ramón baldorioty", "julia de burgos",
        "albizu campos", "rafael cordero",
        "mariana bracetti", "salvador brau",
    ],

    "pasteles puertorriqueños": [
        "bizcocho", "guayaba", "queso", "vainilla",
        "chocolate", "almendra", "piña", "coco",
        "tres leches", "merengue", "buttercream",
        "fondant", "relleno", "horno", "molde"
    ],

    "panadería": [
        "pan sobao", "pan de agua", "mallorca",
        "quesito", "croissant", "galleta",
        "bizcocho", "levadura", "harina",
        "amasar", "hornear", "fermentar",
        "azúcar", "sal", "mantequilla"
    ],

    "enamorándonos univisión": [
        "cupido", "amor", "corazón",
        "compatibilidad", "presentador", "cita",
        "romance", "soltero",
        "flechado", "ilusión", "química", "que si que si",
        "beso", "ana patricia", "rafael"
    ],

    "palabras raras": [
        "efímero", "inefable", "limerencia",
        "sonder", "serendipia", "petrichor",
        "susurro", "incandescente", "etéreo",
        "melancolía", "ataraxia", "inmarcesible",
        "nefelibata", "epifanía", "resiliencia"
    ],

    "costura": [
        "aguja", "hilo", "tijeras", "dedal", "patrón",
        "costura recta", "zigzag", "bastidor", "alfileres",
        "cinta métrica", "botones", "cierres", "bordado",
        "remiendo", "puntada"
    ],

    "técnicas de costura": [
        "hilvanar", "embridar", "remallar", "fruncir",
        "sobrehilar", "dobladillar", "forrar",
        "encintar", "plisado", "entallar",
        "bastilla", "rematar", "traslazar",
        "hilera", "montar"
    ],

    "tipos de telas": [
        "algodón", "lino", "seda", "satén", "poliéster",
        "lana", "denim", "terciopelo", "encaje",
        "tul", "fieltro", "franela", "pana",
        "cuero", "organza"
    ],

    "palabras de cocina": [
        "sazón", "mezclar", "batir", "sofreír", "picar",
        "colar", "amasar", "hervir", "adobar",
        "marinar", "saltear", "flamear", "reposar",
        "cortar", "freír"
    ],

    "objetos comunes": [
        "mesa", "silla", "lámpara", "ventana", "cortina",
        "reloj", "zapato", "libro", "lápiz",
        "celular", "cartera", "botella", "llave",
        "almohada", "espejo"
    ],

    "viajes y turismo": [
        "aeropuerto", "maleta", "mapa", "pasaporte", "hotel",
        "reserva", "aventura", "guía", "tren",
        "museo", "playa", "montaña", "comida",
        "fotos", "recuerdos"
    ],

    "naturaleza": [
        "montaña", "río", "valle", "bosque", "cascada",
        "playa", "desierto", "cueva", "nube",
        "lluvia", "trueno", "sol", "luna",
        "estrella", "horizonte"
    ],

    "hobbies": [
        "pintar", "tejer", "hornear", "leer", "bailar",
        "cocinar", "cantar", "programar", "dibujar",
        "yoga", "jardinería", "fotografía",
        "viajar", "coleccionar", "escribir"
    ],

    "cosas del día a día": [
        "llaves", "cartera", "celular", "reloj", "gafas",
        "libreta", "lápiz", "botella", "audífonos",
        "billetera", "mascarilla", "cargador",
        "pañuelo", "tarjeta", "monedas"
    ],
    
    "manualidades": [
        "pegamento", "cartulina", "pintura", "brocha",
        "papel", "recorte", "collage", "brillantina",
        "estambre", "plantilla", "decoración", "molde",
        "marcadores", "sellos", "listones"
    ],

    "cocina básica": [
        "freír", "hervir", "asar", "hornear",
        "picar", "mezclar", "sazonar",
        "saltear", "batir", "colador",
        "sartén", "olla", "cuchillo",
        "tabla", "receta"
    ],

    "cosas del hogar": [
        "escoba", "mapo", "lavadora", "secadora",
        "nevera", "estufa", "gabinetes",
        "cortinas", "alfombra", "cojines",
        "abanico", "lámpara", "televisor",
        "reloj", "espejo"
    ],

    "jardinería": [
        "regar", "maceta", "tierra",
        "abono", "semilla", "pala",
        "rastrillo", "podar", "fertilizante",
        "sol", "sombra", "raíz",
        "tallo", "hojas", "flor"
    ],

    "recuerdos de antes": [
        "radio", "tocadiscos", "casete",
        "fotografía", "álbum", "carta",
        "estampillas", "postales", "agenda",
        "calendario", "reloj de cuerda",
        "teléfono", "televisor", "revistas",
        "libreta"
    ],

    "juegos tradicionales": [
        "dominó", "parchís", "damas"
        "ajedrez", "barajas", "lotería",
        "bingo", "canicas", "trompo",
        "yoyo", "escondite",
        "balero", "brincar"
    ],

    "emociones": [
        "alegría", "tristeza", "enojo",
        "miedo", "amor", "calma",
        "ansiedad", "nostalgia", "ilusión",
        "orgullo", "vergüenza", "esperanza",
        "frustración", "gratitud", "paz"
    ],

    "valores": [
        "respeto", "honestidad", "amor",
        "solidaridad", "empatía", "lealtad",
        "responsabilidad", "paciencia",
        "humildad", "gratitud", "justicia",
        "tolerancia", "perseverancia",
        "compasión", "bondad"
    ],

    "palabras bonitas": [
        "luz", "abrazo", "hogar",
        "sonrisa", "ternura", "alma",
        "cariño", "armonía", "calidez",
        "confianza", "dulzura", "paz",
        "amor", "magia", "gratitud"
    ],

    "instrumentos musicales": [
        "güiro", "cuatro", "maracas", "tres",
        "pandereta", "bongó", "timbal", "violín",
        "piano", "guitarra", "bajo", "clarinete",
        "saxofón", "flauta", "trompeta"
    ],

    "transporte": [
        "carro", "camión", "guagua", "tren",
        "metro", "bicicleta", "motocicleta",
        "avión", "barco", "ferry", "patineta",
        "taxi", "colectivo", "helicóptero", "submarino"
    ],

    "profesiones": [
        "doctor", "ingeniero", "maestro",
        "abogado", "enfermera", "arquitecto",
        "químico", "bombero", "periodista",
        "chef", "microbiologo", "cantante",
        "mecánico", "diseñador", "fotógrafo"
    ],

    "ropa y accesorios": [
        "camisa", "pantalón", "falda",
        "sombrero", "zapatos", "sandalias",
        "bolso", "collar", "anillo",
        "bufanda", "abrigo", "calcetines",
        "corbata", "gafas", "chaqueta"
    ],

    "cosas de escuela": [
        "lápiz", "pluma", "cuaderno",
        "borrador", "regla", "mochila",
        "pizarrón", "tiza", "libro",
        "carpeta", "silla", "mesa",
        "calculadora", "marcador", "grapadora"
    ],

    "animales domésticos": [
        "perro", "gato", "pez", "loro", "conejo",
        "hamster", "tortuga", "periquito", "caballo",
        "gallina", "pato", "cabra", "oveja",
        "cerdo", "paloma"
    ],

    "animales salvajes": [
        "león", "tigre", "elefante",
        "jirafa", "cebra", "hipopótamo",
        "rinoceronte", "cocodrilo", "lobo",
        "oso", "puma", "canguro",
        "búfalo", "camello", "gorila"
    ],

    "objetos de la casa": [
        "silla", "mesa", "cama",
        "armario", "espejo", "lámpara",
        "cortina", "reloj", "sofá",
        "televisor", "ventana", "puerta",
        "alfombra", "estantería", "perchero"
    ],

    "elementos de la naturaleza": [
        "sol", "luna", "estrella",
        "árbol", "flor", "rio",
        "montaña", "playa", "océano",
        "nube", "viento", "lluvia",
        "arena", "roca", "hierba"
    ],

    "lista del supermercado": [
        "pan", "leche", "huevos",
        "arroz", "frijoles", "carne",
        "pollo", "pescado", "verduras",
        "frutas", "aceite", "azúcar",
        "sal", "harina", "jugo"
    ],

    "juguetes": [
        "muñeca", "carrito", "rompecabezas",
        "lego", "pelota", "tren",
        "trompo", "yoyo", "puzzle",
        "marioneta", "kit de ciencia", "muñeco de acción",
        "balero", "avión de papel", "figuras"
    ],

    "cosas del baño": [
        "jabón", "champú", "acondicionador",
        "cepillo", "pasta dental", "toalla",
        "esponja", "gel", "crema",
        "peine", "rastrillo", "shampoo seco",
        "pañuelo", "secador", "espejo"
    ],

    "días de la semana": [
        "lunes", "martes", "miércoles",
        "jueves", "viernes", "sábado",
        "domingo"
    ],

    "meses del año": [
        "enero", "febrero", "marzo",
        "abril", "mayo", "junio",
        "julio", "agosto", "septiembre",
        "octubre", "noviembre", "diciembre"
    ],

    "caso cerrado": [
        "ana maría polo", "demandante", "demandado", "martillazo",
        "veredicto", "testigo", "evidencia", "abogado",
        "conflicto", "sentencia", "drama", "polémica",
        "tribunal", "caso"
    ],

    "chavo del ocho": [
        "chespirito", "chavo", "chilindrina", "don ramón",
        "florinda", "kiko", "chapulín", "jirafales",
        "ñoño", "barriga", "botija", "ñañaras"
    ],

    "programas de tv latinos": [
        "sabado gigante", "rosa de guadalupe", "reina del sur",
        "top chef", "master chef", "la voz",
        "chavo del ocho", "chapulín colorado"
    ],

    "telenovelas clásicas": [
        "maria mercedes", "marimar", "maria del barrio", "rubí",
        "teresa", "betty la fea", "pasion de gavilanes",
        "sortilegio", "destilando amor", "la madrastra",
        "rebelde", "doña bárbara"
    ],

    "artistas latinos populares": [
        "shakira", "karol g", "romeo santos", "pitbull",
        "nicky jam", "camilo", "luis miguel",
        "juan gabriel", "enrique iglesias",
        "marco antonio solís", "marc anthony"
    ],

    "artistas boricuas populares": [
        "bad bunny", "ricky martín", "don omar", "wisin",
        "yandel", "gilberto santa rosa", "ismael rivera",
        "tito puente", "kany garcía", "edita nazario",
        "hector lavoe"
    ],

    "películas famosas": [
        "titanic", "avatar", "rocky", "gladiator", "matrix",
        "frozen", "encanto", "coco", "starwars",
        "avengers", "jurassic", "harry potter",
        "notebook", "inception", "forrest gump"
    ],

    "palabras raras en español": [
        "ataraxia", "petrichor", "epifanía", "serendipia",
        "melifluo", "taciturno", "nefelibata",
        "etéreo", "ignoto", "elucidar",
        "utopía", "nimiedad", "óbice",
        "perenne", "onírico"
    ],

    "objetos comunes en ingles": [
        "phone", "wallet", "keys", "watch", "glasses",
        "bag", "bottle", "book", "pen", "notebook",
        "charger", "umbrella", "mirror", "camera", "clock"
    ],

    "ropa y accesorios en ingles": [
        "shirt", "pants", "dress", "skirt", "jacket",
        "coat", "shoes", "socks", "hat", "belt",
        "scarf", "gloves", "sunglasses", "backpack", "purse"
    ],

    "trabajo y oficina en ingles": [
        "office", "job", "work", "meeting", "project",
        "email", "computer", "keyboard", "screen", "printer",
        "document", "file", "deadline", "schedule", "report"
    ],

    "naturaleza y medio ambiente en ingles": [
        "nature", "tree", "flower", "river", "mountain",
        "forest", "beach", "ocean", "lake", "sun",
        "moon", "star", "cloud", "rain", "wind"
    ],

    "series en inglés": [
        "friends", "the office", "gilmore girls",
        "greys anatomy", "gossip girl", "stranger things",
        "bridgerton", "suits", "lost", "homeland",
        "modern family", "supernatural", "shameless"
    ],

    "saludos y expresiones en ingles": [
        "hello", "hi", "goodbye", "bye", "please",
        "thank you", "sorry", "excuse me", "welcome", "good morning",
        "good afternoon", "good evening", "good night", "see you", "take care"
    ],

    "familia y relaciones en ingles": [
        "family", "mother", "father", "sister", "brother",
        "son", "daughter", "grandmother", "grandfather", "cousin",
        "aunt", "uncle", "friend", "partner", "love"
    ],

    "casa y habitaciones en ingles": [
        "house", "room", "kitchen", "bathroom", "bedroom",
        "living room", "garden", "balcony", "door", "window",
        "floor", "wall", "ceiling", "chair", "table"
    ],

    "escuela y educacion en ingles": [
        "school", "class", "student", "teacher", "lesson",
        "book", "pen", "notebook", "homework", "exam",
        "desk", "study", "learn", "education", "subject"
    ],

    "comida y bebidas en ingles": [
        "food", "bread", "pasta", "pizza", "cheese",
        "meat", "fish", "salad", "fruit", "vegetables",
        "water", "juice", "coffee", "tea", "milk"
    ],

    "animales comunes en ingles": [
        "dog", "cat", "bird", "fish", "horse",
        "cow", "sheep", "pig", "rabbit", "mouse",
        "lion", "tiger", "bear", "monkey", "wolf"
    ],

    "colores en ingles": [
        "red", "blue", "green", "yellow", "black",
        "white", "orange", "purple", "pink", "gray",
        "brown", "gold", "silver", "dark", "light"
    ],

    "transportes en ingles": [
        "car", "bus", "train", "plane", "boat",
        "bicycle", "motorcycle", "subway", "taxi", "truck",
        "van", "ferry", "tram", "scooter", "ship"
    ],

    "emociones y sentimientos en ingles": [
        "happy", "sad", "angry", "afraid", "surprised",
        "calm", "excited", "bored", "nervous", "proud",
        "love", "hate", "hope", "fear", "joy"
    ],

    "verbos comunes en ingles": [
        "be", "have", "go", "come", "eat",
        "drink", "see", "hear", "speak", "read",
        "write", "learn", "work", "play", "sleep"
    ],

    "saludos y despedidas en italiano": [
    "ciao", "buongiorno", "buonasera", "arrivederci", "grazie",
    "prego", "scusa", "per favore", "salve", "a presto",
    "benvenuto", "addio", "ciao ciao", "a domani", "buonanotte"
],

    "familia y relaciones en italiano": [
    "amore", "famiglia", "amico", "sorella", "fratello",
    "figlio", "figlia", "cugino", "cugina", "nonno",
    "nonna", "zio", "zia", "marito", "moglie"
],

    "hogar y partes de la casa en italiano": [
    "casa", "appartamento", "stanza", "cucina", "bagno",
    "soggiorno", "giardino", "balcone", "porta", "finestra",
    "tetto", "soffitta", "cantina", "scala", "corridoio"
],

    "escuela y educación en italiano": [
    "scuola", "lezione", "studente", "professore", "classe",
    "libro", "penna", "quaderno", "compito", "esame",
    "matita", "lavagna", "banco", "zaino", "orario"
],

    "comida y bebida en italiano": [
    "cibo", "pane", "pasta", "pizza", "formaggio",
    "carne", "pesce", "insalata", "frutta", "verdura",
    "acqua", "vino", "birra", "caffè", "latte"
],

    "animales en italiano": [
    "cane", "gatto", "uccello", "pesce", "cavallo",
    "mucca", "pecora", "asino", "coniglio", "topo",
    "tigre", "leone", "elefante", "orso", "volpe"
],

    "colores en italiano": [
    "rosso", "blu", "verde", "giallo", "nero",
    "bianco", "arancione", "viola", "rosa", "marrone",
    "grigio", "celeste", "turchese", "beige", "oro"
],

    "transporte en italiano": [
    "auto", "bicicletta", "treno", "autobus", "aereo",
    "barca", "moto", "camminare", "metropolitana", "taxi",
    "camion", "monopattino", "tram", "elicottero", "nave"
],

    "estaciones y clima en italiano": [
    "primavera", "estate", "autunno", "inverno", "sole",
    "pioggia", "neve", "vento", "temporale", "nebbia",
    "grandine", "uragano", "arcobaleno", "temporale", "caldo"
],

    "emociones y sentimientos en italiano": [
    "felice", "triste", "arrabbiato", "paura", "sorpreso",
    "annoia", "entusiasta", "innamorato", "preoccupato", "geloso",
    "sciocco", "timido", "stanco", "grato", "sorpresa"
],

    "verbos comunes en italiano": [
    "essere", "avere", "andare", "venire", "fare",
    "dire", "potere", "volere", "dovere", "sapere",
    "vedere", "parlare", "mangiare", "bere", "dormire"
],

    "objetos y cosas en italiano": [
    "tavolo", "sedia", "libro", "penna", "telefono",
    "computer", "zaino", "occhiali", "orologio", "porta",
    "lampada", "letto", "quaderno", "cuscino", "specchio"
],

    "ciudades de Italia": [
    "roma", "milano", "napoli", "torino", "palermo",
    "genova", "bologna", "firenze", "venezia", "verona",
    "messina", "trieste", "padova", "brescia", "taranto"
],

    "días de la semana y tiempo en italiano": [
    "lunedì", "martedì", "mercoledì", "giovedì", "venerdì",
    "sabato", "domenica", "oggi", "domani", "ieri",
    "mattina", "pomeriggio", "sera", "notte", "mezzogiorno"
],

    "conceptos generales en italiano": [
    "tempo", "cuore", "felicità", "sogno", "musica",
    "viaggio", "fortuna", "vita", "amico", "cultura",
    "libertà", "pace", "gioia", "forza", "energia"
],

    "saludos y expresiones en francés": [
    "bonjour", "salut", "bonsoir", "au revoir", "à bientôt",
    "merci", "s il vous plaît", "pardon", "excusez moi", "bienvenue",
    "à demain", "bonne nuit", "félicitations", "allô", "coucou"
],

    "familia y relaciones en francés": [
    "famille", "père", "mère", "frère", "saeur",
    "fils", "fille", "oncle", "tante", "grand père",
    "grand mère", "cousin", "cousine", "époux", "épouse"
],

    "casa y habitaciones en francés": [
    "maison", "appartement", "chambre", "cuisine", "salle de bain",
    "salon", "jardin", "balcon", "porte", "fenêtre",
    "toit", "grenier", "cave", "escalier", "couloir"
],

    "escuela y educación en francés": [
    "école", "classe", "élève", "professeur", "leçon",
    "livre", "stylo", "cahier", "devoir", "examen",
    "crayon", "tableau", "bureau", "sac à dos", "horaires"
],

    "comida y bebidas en francés": [
    "pain", "fromage", "pâtes", "pizza", "viande",
    "poisson", "salade", "fruit", "légume", "eau",
    "vin", "bière", "café", "thé", "jus"
],

    "animales en francés": [
    "chien", "chat", "oiseau", "poisson", "cheval",
    "vache", "mouton", "âne", "lapin", "souris",
    "tigre", "lion", "éléphant", "ours", "renard"
],

    "colores en francés": [
    "rouge", "bleu", "vert", "jaune", "noir",
    "blanc", "orange", "violet", "rose", "marron",
    "gris", "cyan", "turquoise", "beige", "or"
],

    "transportes en francés": [
    "voiture", "vélo", "train", "bus", "avion",
    "bateau", "moto", "marcher", "métro", "taxi",
    "camion", "trotinette", "tram", "hélicoptère", "navire"
],

    "estaciones y clima en francés": [
    "printemps", "été", "automne", "hiver", "soleil",
    "pluie", "neige", "vent", "orage", "brouillard",
    "grêle", "ouragan", "arc en ciel", "froid", "chaud"
],

    "emociones y sentimientos en francés": [
    "heureux", "triste", "en colère", "peur", "surpris",
    "ennuyé", "enthousiaste", "amoureux", "préoccupé", "jaloux",
    "bête", "timide", "fatigué", "reconnaissant", "excité"
],

    "verbos comunes en francés": [
    "être", "avoir", "aller", "venir", "faire",
    "dire", "pouvoir", "vouloir", "devoir", "savoir",
    "voir", "parler", "manger", "boire", "dormir"
],

    "objetos y cosas en francés": [
    "table", "chaise", "livre", "stylo", "téléphone",
    "ordinateur", "sac", "lunettes", "montre", "porte",
    "lampe", "lit", "cahier", "oreiller", "miroir"
],

    "ciudades francesas": [
    "paris", "marseille", "lyon", "toulouse", "nice",
    "nantes", "strasbourg", "montpellier", "bordeaux", "lille",
    "rennes", "reims", "le havre", "saint étienne", "toulon"
],

    "días de la semana y tiempo en francés": [
    "lundi", "mardi", "mercredi", "jeudi", "vendredi",
    "samedi", "dimanche", "aujourd hui", "demain", "hier",
    "matin", "après midi", "soir", "nuit", "midi"
],

    "conceptos generales en francés": [
    "temps", "caeur", "bonheur", "rêve", "musique",
    "voyage", "chance", "vie", "ami", "culture",
    "liberté", "paix", "joie", "force", "énergie"
],

    "saludos y expresiones en portugués": [
    "olá", "bom dia", "boa tarde", "boa noite", "adeus",
    "até logo", "obrigado", "por favor", "desculpe", "bem vindo",
    "até amanhã", "feliz", "parabéns", "oi", "tchau"
],

    "familia y relaciones en portugués": [
    "família", "pai", "mãe", "irmão", "irmã",
    "filho", "filha", "tio", "tia", "avô",
    "avó", "primo", "prima", "marido", "mulher"
],

    "casa y habitaciones en portugués": [
    "casa", "apartamento", "quarto", "cozinha", "banheiro",
    "sala", "jardim", "varanda", "porta", "janela",
    "telhado", "sótão", "porão", "escada", "corredor"
],

    "escuela y educación en portugués": [
    "escola", "classe", "aluno", "professor", "aula",
    "livro", "caneta", "caderno", "tarefa", "exame",
    "lápis", "quadro", "mesa", "mochila", "horário"
],

    "comida y bebidas en portugués": [
    "pão", "queijo", "massa", "pizza", "carne",
    "peixe", "salada", "fruta", "legume", "água",
    "vinho", "cerveja", "café", "chá", "suco"
],

    "animales en portugués": [
    "cachorro", "gato", "pássaro", "peixe", "cavalo",
    "vaca", "ovelha", "burro", "coelho", "rato",
    "tigre", "leão", "elefante", "urso", "raposa"
],

    "colores en portugués": [
    "vermelho", "azul", "verde", "amarelo", "preto",
    "branco", "laranja", "roxo", "rosa", "marrom",
    "cinza", "ciano", "turquesa", "bege", "dourado"
],

    "transportes en portugués": [
    "carro", "bicicleta", "trem", "ônibus", "avião",
    "barco", "moto", "andar", "metrô", "táxi",
    "caminhão", "patinete", "bonde", "helicóptero", "navio"
],

    "estaciones y clima en portugués": [
    "primavera", "verão", "outono", "inverno", "sol",
    "chuva", "neve", "vento", "tempestade", "neblina",
    "granizo", "furacão", "arco íris", "frio", "quente"
],

    "emociones y sentimientos en portugués": [
    "feliz", "triste", "zangado", "medo", "surpreso",
    "entediado", "entusiasmado", "apaixonado", "preocupado", "ciumento",
    "bobo", "tímido", "cansado", "agradecido", "animado"
],

    "verbos comunes en portugués": [
    "ser", "estar", "ter", "ir", "vir",
    "fazer", "dizer", "poder", "querer", "dever",
    "ver", "falar", "comer", "beber", "dormir"
],

    "objetos y cosas en portugués": [
    "mesa", "cadeira", "livro", "caneta", "telefone",
    "computador", "mochila", "óculos", "relógio", "porta",
    "lâmpada", "cama", "caderno", "travesseiro", "espelho"
],

    "ciudades en portugués": [
    "lisboa", "porto", "coimbra", "funchal", "faro",
    "braga", "evora", "setúbal", "aveiro", "guimarães",
    "sintra", "leiria", "beja", "viana do castelo", "bragança"
],

    "días de la semana y tiempo en portugués": [
    "segunda feira", "terça feira", "quarta feira", "quinta feira", "sexta feira",
    "sábado", "domingo", "hoje", "amanhã", "ontem",
    "manhã", "tarde", "noite", "meio dia", "meia noite"
],

    "conceptos generales en portugués": [
    "tempo", "coração", "felicidade", "sonho", "música",
    "viagem", "sorte", "vida", "amigo", "cultura",
    "liberdade", "paz", "alegria", "força", "energia"
],
    "saludos y expresiones en alemán": [
    "hallo", "guten tag", "guten morgen", "guten abend", 
    "tschüss", "bitte", "danke", "entschuldigung", "hi", "servus", 
    "bis bald", "glücklich", "auf wiedersehen", "herzlichen glückwuns", "herzlich willkommen",
],

    "familia y relaciones en alemán": [
    "familie", "vater", "mutter", "bruder", "schwester",
    "sohn", "tochter", "onkel", "tante", "opa",
    "oma", "cousin", "cousine", "ehemann", "ehefrau"
],

    "casa y habitaciones en alemán": [
    "haus", "wohnung", "zimmer", "küche", "bad",
    "wohnzimmer", "garten", "balkon", "tür", "fenster",
    "dach", "keller", "boden", "treppe", "flur"
],

    "escuela y educación en alemán": [
    "schule", "klasse", "schüler", "lehrer", "unterricht",
    "buch", "stift", "heft", "aufgabe", "prüfung",
    "bleistift", "tafel", "tisch", "rucksack", "stundenplan"
],

    "comida y bebidas en alemán": [
    "brot", "käse", "nudeln", "pizza", "fleisch",
    "fisch", "salat", "obst", "gemüse", "wasser",
    "wein", "bier", "kaffee", "tee", "saft"
],

    "animales en alemán": [
    "hund", "katze", "vogel", "fisch", "pferd",
    "kuh", "schaf", "esel", "kaninchen", "maus",
    "tiger", "löwe", "elefant", "bär", "fuchs"
],

    "colores en alemán": [
    "rot", "blau", "grün", "gelb", "schwarz",
    "orange", "violett", "rosa", "braun",
    "grau", "cyan", "türkis", "beige", "gold"
],

    "transportes en alemán": [
    "auto", "fahrrad", "zug", "bus", "flugzeug",
    "boot", "motorrad", "gehen", "u bahn", "taxi",
    "lkw", "roller", "hubschrauber", "schiff"
],

    "estaciones y clima en alemán": [
    "frühling", "sommer", "herbst", "winter", "sonne",
    "regen", "schnee", "wind", "sturm", "nebel",
    "hagel", "orkan", "regenbogen", "kalt"
],

    "emociones y sentimientos en alemán": [
    "glücklich", "traurig", "wütend", "angst", "überrascht",
    "gelangweilt", "begeistert", "verliebt", "besorgt", "eifersüchtig",
    "dumm", "schüchtern", "müde", "dankbar", "aufgeregt"
],

    "verbos comunes en alemán": [
    "sein", "haben", "gehen", "kommen", "machen",
    "sagen", "können", "wollen", "müssen", "sehen",
    "sprechen", "essen", "trinken", "schlafen", "lesen"
],

    "objetos y cosas en alemán": [
    "tisch", "stuhl", "buch", "stift", "telefon",
    "computer", "rucksack", "brille", "uhr", "tür",
    "lampe", "bett", "heft", "kissen", "spiegel"
],

    "ciudades en alemán": [
    "berlin", "hamburg", "münchen", "köln", "frankfurt",
    "stuttgart", "düsseldorf", "dortmund", "essen", "leipzig",
    "bremen", "hannover", "dresden", "nürnberg", "bonn"
],

    "días de la semana y tiempo en alemán": [
    "montag", "dienstag", "mittwoch", "donnerstag", "freitag",
    "samstag", "sonntag", "heute", "morgen", "gestern",
    "morgen", "nachmittag", "abend", "mittag", "mitternacht"
],

    "conceptos generales en alemán": [
    "zeit", "herz", "glück", "traum", "musik",
    "reise", "glück", "leben", "freund", "kultur",
    "freiheit", "frieden", "freude", "kraft", "energie"
],
    "saludos y expresiones en japonés (romanizado)": [
    "konnichiwa", "ohayou", "konbanwa", "sayounara", "arigatou",
    "sumimasen", "onegaishimasu", "ogenki desu ka", "hai", "iie",
    "hajimemashite", "yoroshiku", "oyasuminasai", "mata ne", "gomen nasai"
],

    "familia y relaciones en japonés (romanizado)": [
    "kazoku", "chichi", "haha", "ani", "ane",
    "otouto", "imouto", "sofu", "sobo", "oji",
    "oba", "itoko", "otto", "tsuma", "kodomo"
],

    "casa y habitaciones en japonés (romanizado)": [
    "ie", "apāto", "heya", "daidokoro", "yokushitsu",
    "ima", "niwa", "barukonī", "doa", "mado",
    "yane", "chikashitsu", "kaidan", "rouka", "yuka"
],

    "escuela y educación en japonés (romanizado)": [
    "gakkou", "jugyou", "gakusei", "sensei", "kyoushitsu",
    "hon", "enpitsu", "nōto", "shukudai", "shiken",
    "kokuban", "tsukue", "ryukku", "jikanwari", "benkyou"
],

    "comida y bebidas en japonés (romanizado)": [
    "gohan", "pan", "pasuta", "piza", "niku",
    "sakana", "sarada", "kudamono", "yasai", "mizu",
    "ocha", "kōhī", "jūsu", "bīru", "wain"
],

    "animales en japonés (romanizado)": [
    "inu", "neko", "tori", "sakana", "uma",
    "ushi", "hitsuji", "roba", "usagi", "nezumi",
    "tora", "raion", "zou", "kuma", "kitsune"
],

    "colores en japonés (romanizado)": [
    "aka", "ao", "midori", "kiiro", "kuro",
    "shiro", "orenji", "murasaki", "pinku", "chairo",
    "haiiro", "mizuiro", "kin", "gin", "tākoizu"
],

    "transportes en japonés (romanizado)": [
    "kuruma", "jitensha", "densha", "basu", "hikouki",
    "fune", "baiku", "aruku", "chikatetsu", "takushī",
    "torakku", "sukūtā", "kaitenbune", "bōto", "shinkansen"
],

    "estaciones y clima en japonés (romanizado)": [
    "haru", "natsu", "aki", "fuyu", "taiyou",
    "ame", "yuki", "kaze", "arashi", "kumori",
    "hare", "shitsuren", "taifu", "kōri", "shio"
],

    "emociones y sentimientos en japonés (romanizado)": [
    "ureshii", "kanashii", "okotteiru", "kowai", "odoroku",
    "taikutsu", "kandō", "ren ai", "shinpai", "yokatta",
    "sabishii", "yasashii", "jiman", "hantai", "tanoshii"
],

    "verbos comunes en japonés (romanizado)": [
    "iru/aru", "aru/iru", "iku", "kuru", "suru",
    "iu", "dekiru", "hoshii", "tabe ru",
    "nomu", "miru", "kiku", "hanasu", "oyogu", "shinakereba naranai"
],

    "objetos cotidianos en japonés (romanizado)": [
    "tsukue", "isu", "hon", "enpitsu", "denwa",
    "konpyūta", "zainō", "megane", "tokei", "kaban",
    "tegami", "kamera", "purezento", "heya no doa", "mado"
],

    "ciudades en japonés (romanizado)": [
    "rōma", "mirano", "naporu", "tōrino", "parumero",
    "jenova", "borōnya", "firentse", "venzēya", "kyouto",
    "osaka", "sapporo", "hiroshima", "fukuoka", "nagoya"
],

    "días y tiempo en japonés (romanizado)": [
    "nichiyoubi", "getsuyoubi", "kayoubi", "suiyoubi", "mokuyoubi",
    "kinyoubi", "doyoubi", "kyou", "ashita", "ototoi",
    "kinou", "shuumatsu", "asa", "hiru", "yoru"
],

    "cosas de la vida cotidiana en japonés (romanizado)": [
    "ai", "kazoku", "tomodachi", "hikari", "tsuki",
    "arigatou", "onegai", "jikan", "kokoro", "shiawase",
    "yume", "ongaku", "ryokou", "kouun", "kaze"
],

    "saludos y expresiones en coreano (romanizado)": [
    "annyeong", "annyeonghaseyo",  "gomawo",
    "mianhae", "bwayo", "ne", "ani",
    "jal ga", "joesonghamnida", "gamsahamnida", "daedabhaeyo", "annyeonghi gaseyo", "annyeonghi gyeseyo", "ban gap seumnida", "jal jinaess eoyo"
],

    "familia y relaciones en coreano (romanizado)": [
    "gajok", "abeoji", "eomeoni", "hyeong", "unnie",
    "dongsaeng", "halabeoji", "halmeoni", "samchon", "imo",
    "chingu", "chingu ui abeoji", "chingu ui eomeoni", "hyeongje", "jageun dongsaeng"
],

    "casa y habitaciones en coreano (romanizado)": [
    "jip", "apateu", "bang", "bueok", "hwajangsil",
    "siksanbang", "daecheong", "balcony", "mun", "changmun",
    "daecheong", "cheongdang", "gyedan", "hall", "floor"
],

    "escuela y educación en coreano (romanizado)": [
    "hakgyo", "gyosil", "haksaeng", "seonsaengnim", "ban",
    "chaek", "pil", "notebook", "suje", "siheom",
    "heukpan", "chaeksang", "backpack", "siganbodae", "gongbu"
],

    "comida y bebidas en coreano (romanizado)": [
    "bap", "bbang", "pasta", "pija", "gogi",
    "saengseon", "saladeu", "gwail", "chae", "mul",
    "cha", "keopi", "jus", "maekju", "wain"
],

    "animales en coreano (romanizado)": [
    "gae", "goyang i", "sae", "saengseon", "mal",
    "so", "yang", "donkey", "tokki", "jwi",
    "ho rang i", "sa ja", "kokkiri", "gom", "kitsune"
],

    "colores en coreano (romanizado)": [
    "ppalgan", "parang", "chorok", "norang", "geomeun",
    "hayan", "orenji", "borasaek", "pink", "jilsaek",
    "hueru", "mizuiro", "geum", "eun", "ta koizu"
],

    "transportes en coreano (romanizado)": [
    "cha", "jajeongeo", "cheoncha", "beoseu", "bihaenggi",
    "bada boat", "baikeu", "georeuda", "jihatche", "taegsi",
    "truck", "scooter", "jido bunde", "boat", "kotsu"
],

    "estaciones y clima en coreano (romanizado)": [
    "bom", "yeoreum", "gaeul", "gyeoul", "hae",
    "bi", "nun", "baram", "poom", "gureum",
    "hae", "sil", "taepung", "ice", "sio"
],

    "emociones y sentimientos en coreano (romanizado)": [
    "haengbog", "seulpeun", "hwa", "neomuna", "nollada",
    "jjikjjik", "gamsahada", "sarang", "geogjeong", "gippeuda",
    "seulpeuda", "dalda", "jiman", "bandae", "jaemi"
],

    "verbos comunes en coreano (romanizado)": [
    "ida", "issda", "gada", "oda", "hada",
    "malhada", "hal su issda", "wonhada", "haeya hada", "meokda",
    "masida", "boda", "deudda", "malhada", "swida"
],

    "objetos cotidianos en coreano (romanizado)": [
    "chaeksang", "uija", "chaek", "pil", "jeonhwagi",
    "keompyuteo", "gabang", "angyeong", "sigye", "baenang",
    "pyeonji", "kamera", "present", "mun", "changmun"
],

    "ciudades en coreano (romanizado)": [
    "seoul", "busan", "incheon", "daegu", "daejeon",
    "gwangju", "suwon", "ulsan", "goyang", "yongin",
    "changwon", "seongnam", "cheongju", "jeonju", "pohang"
],

    "días y tiempo en coreano (romanizado)": [
    "iryoil", "woryoil", "hwayoil", "suyoil", "mogyoil",
    "geumyoil", "toyoil", "oneul", "naeil", "ojeon",
    "eonje", "ju mog", "achim", "bam", "oreun"
],

    "cosas de la vida cotidiana en coreano (romanizado)": [
    "sarang", "gajok", "chingu", "bit", "dal",
    "gomawo", "onegaehada", "sigan", "ma eum", "haengbok",
    "kkum", "eumak", "yuhang", "haeng un", "baram"
],
    "saludos y expresiones en arabe (romanizado)": [
    "marhaba", "ahlan", "sabah alkhair",
    "masa alkhair", "shukran", "afwan", "min fadlak", "la shukran",
    "keif halak", "ana bekhair", "ma a salama", "ila al liqa", "afwan ya sadiqi", "assalamu alaikum", "wa alaikum assalam"
],

    "familia y relaciones en arabe (romanizado)": [
    "usra", "ab", "umm", "akh", "ukht",
    "ibn", "bint", "jadd", "jadda", "amm",
    "amma", "sadiq", "sadiqa", "habib", "habiba"
],

    "casa y habitaciones en arabe (romanizado)": [
    "bayt", "shuqaq", "ghurfa", "matbakh", "hammam",
    "majlis", "hardaq", "balkon", "bab", "shubbak",
    "sullam", "qaa a", "maktab", "khizana", "ard"
],

    "escuela y educación en arabe (romanizado)": [
    "madrasa", "fasl", "talib", "ustadh", "kitab",
    "qalam", "daftar", "wazifa", "imtihan", "madrasah",
    "muhadara", "dirasa", "ta allum", "mu allim", "jamia"
],

    "comida y bebidas en arabe (romanizado)": [
    "ta am", "khobz", "laban", "lahm", "samak",
    "salata", "fawakih", "khudra", "shai", "qahwa",
    "ma", "asir", "nahm", "halawa", "baba ghanoush"
],

    "animales en arabe (romanizado)": [
    "kalb", "qitt", "tayr", "samak", "faras",
    "baqar", "ghanam", "himar", "arnab", "jarad",
    "samaak", "asad", "namir", "dabab", "ghazal"
],

    "colores en arabe (romanizado)": [
    "ahmar", "azraq", "akhadar", "asfar", "aswad",
    "abyad", "burtuqali", "banafsaji", "wardi", "ramadi",
    "zahri", "laymuni", "bunni", "fahmy", "turkui"
],

    "transportes en arabe (romanizado)": [
    "sayyara", "diraja", "qitar", "hafila", "tayara",
    "markab", "darraja", "mashi", "metro", "taaksi",
    "hafilah saghira", "sikla", "boot", "sawya"
],

    "estaciones y clima en arabe (romanizado)": [
    "rabee", "sayf", "khareef", "shita", "shams",
    "thalj", "rih", "ghaym", "aalim",
    "bard", "harara", "aalim aljaw", "aqlim", "saif"
],

    "emociones y sentimientos en arabe (romanizado)": [
    "sa id", "hazin", "ghaazib", "khawf", "mufaja a",
    "malal", "farah", "hubb", "qalb", "huzn",
    "iltihab", "jadhab", "ihsas", "ta assuf", "tahammul"
],

    "verbos comunes en arabe (romanizado)": [
    "yakun", "yaf al", "yadhhab", "ya ti", "yakul",
    "yashrab", "yarah", "yasma", "yatakallam", "yaftah",
    "yughliq", "yadrus", "yaktub", "ya mal", "yushahid"
],

    "objetos cotidianos en arabe (romanizado)": [
    "taawila", "kursi", "kitab", "qalam", "hatif",
    "hasub", "haqiba", "nadharat", "sa a", "warqa",
    "kamera", "hadaya", "bab", "shubbak", "misbah"
],

    "ciudades en arabe (romanizado)": [
    "riyadh", "jeddah", "dammam", "mecca", "medina",
    "cairo", "alexandria", "dubai", "abu dhabi", "doha",
    "amman", "beirut", "baghdad", "casablanca", "tunis"
],

    "días y tiempo en arabe (romanizado)": [
    "al ahad", "al ithnayn", "ath thulatha", "al arbia", "al khamis",
    "al jum a", "as sabt", "al yawm", "ghadan", "sabah",
    "masa", "layla", "saa a", "daqiqa", "thaniya"
],

    "cosas de la vida cotidiana en arabe (romanizado)": [
    "hubb", "usra", "sadiq", "shams", "qamar",
    "shukran", "min fadlak", "waqt", "qalb", "sa adah",
    "hulm", "musiqa", "safar", "hazz", "rih"
],
    "saludos y expresiones en chino (romanizado)": [
    "nǐ hǎo", "zǎo ān", "wǎn ān", "zàijiàn", "xièxiè",
    "bù kèqì", "qǐng", "duìbuqǐ", "méi guānxi", "nǐ hǎo ma",
    "wǒ hěn hǎo", "zhù nǐ hǎo yùn", "míngtiān jiàn", "hǎo de", "duō xiè"
],

    "familia y relaciones en chino (romanizado)": [
    "jiā", "fùqīn", "mǔqīn", "gēge", "jiějie",
    "dìdi", "mèimei", "sūnzi", "sūnnǚ", "bómǔ",
    "yímǔ", "péngyou", "nán péngyou", "nǚ péngyou", "àirén"
],

    "casa y habitaciones en chino (romanizado)": [
    "fángzi", "wòshì", "kètīng", "chúfáng", "xǐshǒujiān",
    "cāntīng", "yángtái", "mén", "chuānghu", "céng",
    "shūfáng", "chúzì", "dìtǎn", "yǐzi", "zhuōzi"
],

    "escuela y educación en chino (romanizado)": [
    "xuéxiào", "bān", "xuéshēng", "lǎoshī", "kè",
    "shū", "bǐ", "běnzi", "zuòyè", "kǎoshì",
    "jiàoshì", "lùn wén", "xuéxí", "jiàoyù", "tóngxué"
],

    "comida y bebidas en chino (romanizado)": [
    "shíwù", "miànbāo", "miàn", "pīsà", "rǔlào",
    "ròu", "yú", "shālā", "shuǐguǒ", "shūcài",
    "chá", "kāfēi", "guǒzhī", "píjiǔ", "shuǐ"
],

    "animales en chino (romanizado)": [
    "gǒu", "māo", "niǎo", "yú", "mǎ",
    "niú", "yáng", "lǘ", "tùzi", "hóuzi",
    "shīzi", "lǎohǔ", "xióng", "yáng", "láng"
],

    "colores en chino (romanizado)": [
    "hóngsè", "lánsè", "lǜsè", "huángsè", "hēisè",
    "báisè", "chéngsè", "zǐsè", "fěnsè", "huīsè",
    "tiānlánsè", "jínsè", "yínsè", "zōngsè", "yánsè"
],

    "transportes en chino (romanizado)": [
    "qìchē", "zìxíngchē", "huǒchē", "gōngchē", "fēijī",
    "chuán", "mótuōchē", "zǒulù", "dìtiě", "chūzūchē",
    "bǎochē", "fēichuán", "dīchē", "kāichē", "yùnshū"
],

    "estaciones y clima en chino (romanizado)": [
    "chūn", "xià", "qiū", "dōng", "tài yáng",
    "yǔ", "xuě", "fēng", "yún", "shī", 
    "lěng", "rè", "tiānqì", "zhuāngshì", "jìjié"
],

    "emociones y sentimientos en chino (romanizado)": [
    "gāoxìng", "bēishāng", "shēngqì", "kǒngjù", "jīngyà",
    "mèn", "kuàilè", "ài", "xīn", "yōulǜ",
    "yùhuò", "jīdòng", "shēnqíng", "bàoqiàn", "àixīn"
],

    "verbos comunes en chino (romanizado)": [
    "shì", "yǒu", "qù", "lái", "chī",
    "hē", "kàn", "tīng", "shuō", "dǎkāi",
    "guānbì", "xuéxí", "xiě", "zuò", "kànjiàn"
],

    "objetos cotidianos en chino (romanizado)": [
    "zhuōzi", "yǐzi", "shū", "bǐ", "diànhuà",
    "diànnǎo", "bēizi", "yǎnjìng", "shǒubiǎo", "bāo",
    "shūbāo", "lǐwù", "mén", "chuāng", "dēng"
],

    "ciudades en chino (romanizado)": [
    "běijīng", "shànghǎi", "guǎngzhōu", "shēnzhèn", "chóngqìng",
    "tiānjīn", "xī ān", "hángzhōu", "nánjīng", "chángshā",
    "wǔhàn", "qīngdǎo", "sūzhōu", "dàlǐ", "hǎikǒu"
],

    "días y tiempo en chino (romanizado)": [
    "xīngqī yī", "xīngqī èr", "xīngqī sān", "xīngqī sì", "xīngqī wǔ",
    "xīngqī liù", "xīngqī rì", "jīntiān", "míngtiān", "zuótiān",
    "zǎoshang", "wǎnshàng", "yè", "shí", "fēnzhōng"
],

    "cosas de la vida cotidiana en chino (romanizado)": [
    "ài", "jiārén", "péngyou", "tài yáng", "yuèliang",
    "xièxiè", "qǐng", "shíjiān", "xīn", "xìngfú",
    "mèng", "yīnyuè", "lǚxíng", "xìngyùn", "fēng"
],
    "palabras taínas": [
        "yucayeke", "batata", "huracán", "barbacoa", "yuca",
        "iguana", "bohío", "macana", "hamaca",
        "cacique", "nagua", "cemí", "guanín",
        "manatí", "areyto"
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

pdf.output("Sopa_de_Letras_Abuela.pdf")