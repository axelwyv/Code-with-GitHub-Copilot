from PIL import Image
from colorama import Fore, Style, init
import random
import os
import time

init(autoreset=True)

def image_to_ascii(image_path, output_width=100):
    img = Image.open(image_path)
    img = img.convert("L")
    width, height = img.size
    aspect_ratio = height / width
    output_height = int(output_width * aspect_ratio * 0.55)
    img = img.resize((output_width, output_height))
    pixels = img.getdata()

    ascii_art = []
    for i, pixel in enumerate(pixels):
        # Ajusta los colores para mayor contraste y visibilidad
        if pixel > 200:
            ascii_art.append(Fore.WHITE + "*")      # Muy claro: blanco
        elif pixel > 150:
            ascii_art.append(Fore.LIGHTYELLOW_EX + "*")  # Claro: amarillo claro
        elif pixel > 100:
            ascii_art.append(Fore.LIGHTRED_EX + "*")     # Medio: rojo claro
        elif pixel > 60:
            ascii_art.append(Fore.RED + ",")       # Oscuro: rojo
        elif pixel > 30:
            ascii_art.append(Fore.BLUE + ".")      # Más oscuro: azul
        else:
            ascii_art.append(" ")                  # Fondo: negro (espacio)
        if (i + 1) % output_width == 0:
            ascii_art.append("\n")
    return ascii_art, output_height, output_width

def add_fireworks(ascii_art, output_height, output_width, n_fireworks=10, padding=10):
    art = ascii_art.copy()
    colors = [Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.LIGHTWHITE_EX]
    for _ in range(n_fireworks):
        row = random.randint(0, output_height - 1)
        col = random.randint(0, output_width - 1)
        idx = row * (output_width + 1) + col  # +1 por el salto de línea
        if 0 <= idx < len(art) and art[idx] != "\n":
            art[idx] = random.choice(colors) + "*"
    lines = "".join(art).split('\n')
    padded = [(" " * padding) + line for line in lines]
    return "\n".join(padded)

# Ruta a tu imagen
image_file = "yisus5.png"  
ascii_art, h, w = image_to_ascii(image_file, output_width=100)

# Animación de fuegos artificiales
for _ in range(100):  # Número de cuadros de animación
    os.system("clear")  # Limpia la terminal en Linux/Mac
    print(add_fireworks(ascii_art, h, w, n_fireworks=15, padding=10))
    time.sleep(0.15) 