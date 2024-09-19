import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import re  # Para usar expresiones regulares

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(
        title="Seleccionar archivo HTML",
        filetypes=(("Archivos HTML", "*.html;*.htm"), ("Todos los archivos", "*.*"))
    )

def extraer_preset_name(soup):
    meta_tag = soup.find('meta', {'name': 'arma:PresetName'})
    return meta_tag.get('content') if meta_tag else None

def extraer_display_names(soup):
    display_names = [td.text.strip().lower() for td in soup.find_all('td', {'data-type': 'DisplayName'})]
    
    # Usamos una expresión regular para eliminar cualquier cosa que no sea una letra o número
    display_names_limpiados = [re.sub(r'[^a-zA-Z0-9]', '', name) for name in display_names]
    
    return display_names_limpiados

def extraer_links(soup):
    links = [a['href'] for a in soup.find_all('a', {'data-type': 'Link'})]
    links_limpiados = [link.split('=')[-1] for link in links]
    
    return links_limpiados

# Seleccionar archivo HTML
archivo_html = seleccionar_archivo()
if archivo_html:
    with open(archivo_html, 'r', encoding='utf-8') as archivo:
        contenido_html = archivo.read()
        soup = BeautifulSoup(contenido_html, 'html.parser')

        preset_name = extraer_preset_name(soup)
        display_names = extraer_display_names(soup)
        links = extraer_links(soup)

        if preset_name:
            print(f"Preset Name: {preset_name}")
        
        # Ciclo for para imprimir Display Names y Links juntos
        for display_name, link in zip(display_names, links):
            print(f"----------------------------- {display_name} -----------------------------")
            print(f"Display Name: {display_name}  --> Link: {link}")
            print(f"workshop_download_item 107410 {link}")
            print(f"")
            
            print(f"ln -s /home/steam/Steam/steamapps/workshop/content/107410/{link} /home/steam/arma3gfn/mods/@{display_name}")
            print(f"")
 