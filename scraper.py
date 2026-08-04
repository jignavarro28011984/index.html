import json
from datetime import datetime

def rastrear():
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M")
    vacantes = [
        {
            "id": 1,
            "titulo": "Generalista de Recursos Humanos",
            "empresa": "Empresa del Sector Servicios",
            "ubicacion": "Montevideo",
            "horas": 2,
            "portal": "BuscoJobs UY",
            "descripcion": "Coordinación de ingresos, inducción, clima organizacional y soporte a la dirección.",
            "url": "https://www.buscojobs.com.uy/ofertas/ts1016/trabajo-de-recursos-humanos/montevideo_"
        },
        {
            "id": 2,
            "titulo": "Responsable de Gestión Humana",
            "empresa": "ManpowerGroup",
            "ubicacion": "Montevideo",
            "horas": 5,
            "portal": "Computrabajo UY",
            "descripcion": "Gestión integral del departamento de Personas, reclutamiento activo y selección.",
            "url": "https://uy.computrabajo.com/trabajo-de-recursos-humanos-en-montevideo"
        },
        {
            "id": 3,
            "titulo": "Analista de Selección y Reclutamiento",
            "empresa": "Humanphi",
            "ubicacion": "Cordón, Montevideo",
            "horas": 9,
            "portal": "Computrabajo UY",
            "descripcion": "Publicación de avisos, filtros telefónicos y entrevistas por competencias.",
            "url": "https://uy.computrabajo.com/trabajo-de-recursos-humanos-en-montevideo"
        }
    ]

    datos = {
        "ultima_actualizacion": fecha_actual,
        "total": len(vacantes),
        "vacantes": vacantes
    }

    with open("vacantes.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=4)
    print("Vacantes guardadas con éxito.")

if __name__ == "__main__":
    rastrear()
