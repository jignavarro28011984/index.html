import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from datetime import datetime

def buscar_google_jobs():
    # Palabras clave orientadas a Recursos Humanos / Gestión Humana en Uruguay
    query = '("recursos humanos" OR "gestion humana" OR "seleccion de personal" OR "generalista rrhh") site:uy.computrabajo.com OR site:buscojobs.com.uy OR site:gallito.com.uy'
    url = f"https://news.google.com/rss/search?q={urllib.parse.quote(query)}&hl=es-419&gl=UY&ceid=UY:es-419"
    
    vacantes = []
    
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req) as response:
            xml_data = response.read()
            
        root = ET.fromstring(xml_data)
        items = root.findall('.//item')
        
        for item in items[:10]: # Tomar hasta 10 ofertas relevantes
            title = item.find('text').text if item.find('text') is not None else item.find('title').text
            link = item.find('link').text
            pub_date = item.find('pubDate').text if item.find('pubDate').text is not None else "Reciente"
            
            # Detectar el portal de origen en base al enlace
            portal = "Portal UY"
            if "computrabajo" in link:
                portal = "Computrabajo UY"
            elif "buscojobs" in link:
                portal = "BuscoJobs UY"
            elif "gallito" in link:
                portal = "El Gallito"
                
            vacantes.append({
                "titulo": title.split(' - ')[0] if ' - ' in title else title,
                "empresa": portal,
                "ubicacion": "Montevideo, Uruguay",
                "horas": 4,
                "portal": portal,
                "descripcion": f"Oportunidad detectada en vivo a través de fuentes indexadas en Uruguay.",
                "url": link
            })
    except Exception as e:
        print(f"Error al conectar: {e}")
        
    return vacantes

def generar_json():
    vacantes_encontradas = buscar_google_jobs()
    
    # Si por alguna razón la búsqueda no devuelve nada, usamos datos de respaldo limpios
    if not vacantes_encontradas:
        vacantes_encontradas = [
            {
                "titulo": "Analista de Selección y Gestión Humana",
                "empresa": "BuscoJobs UY",
                "ubicacion": "Montevideo",
                "horas": 2,
                "portal": "BuscoJobs UY",
                "descripcion": "Búsqueda activa de perfiles corporativos y entrevistas masivas.",
                "url": "https://www.buscojobs.com.uy"
            }
        ]

    data = {
        "ultima_actualizacion": datetime.now().strftime("%d/%m/%Y a las %H:%M"),
        "vacantes": vacantes_encontradas
    }
    
    with open("vacantes.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("¡Archivo vacantes.json actualizado con éxito!")

if __name__ == "__main__":
    generar_json()
