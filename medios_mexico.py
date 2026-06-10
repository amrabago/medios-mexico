#!/usr/bin/env python3
"""
medios_mexico.py
Genera y muestra la lista de principales medios de comunicación de México,
incluyendo medios nacionales y regionales de Baja California.

Autor: Maxicomm
"""

import json
import os

ARCHIVO_DATOS = os.path.join(os.path.dirname(__file__), "medios_mexico.json")


def cargar_medios(ruta: str) -> list[dict]:
    """Carga la lista de medios desde el archivo JSON."""
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def filtrar_por_region(medios: list[dict], region: str) -> list[dict]:
    """Filtra medios por región (parcial, sin distinción de mayúsculas)."""
    region_lower = region.lower()
    return [m for m in medios if region_lower in m["region"].lower()]


def filtrar_por_formato(medios: list[dict], formato: str) -> list[dict]:
    """Filtra medios que incluyan el formato indicado."""
    formato_lower = formato.lower()
    return [m for m in medios if formato_lower in m["formato"].lower()]


def imprimir_tabla(medios: list[dict]) -> None:
    """Imprime los medios en formato de tabla legible."""
    if not medios:
        print("  (Sin resultados)")
        return

    col_nom = max(len(m["nombre"]) for m in medios) + 2
    col_tipo = max(len(m["tipo"]) for m in medios) + 2
    col_reg = max(len(m["region"]) for m in medios) + 2

    encabezado = (
        f"{'#':<4} {'Nombre':<{col_nom}} {'Tipo':<{col_tipo}} "
        f"{'Región':<{col_reg}} {'URL'}"
    )
    print(encabezado)
    print("-" * (len(encabezado) + 20))

    for m in medios:
        notas = f"  ← {m['notas']}" if m.get("notas") else ""
        print(
            f"{m['id']:<4} {m['nombre']:<{col_nom}} {m['tipo']:<{col_tipo}} "
            f"{m['region']:<{col_reg}} {m['url']}{notas}"
        )


def main() -> None:
    medios = cargar_medios(ARCHIVO_DATOS)

    print("=" * 70)
    print("  PRINCIPALES MEDIOS DE COMUNICACIÓN DE MÉXICO")
    print("  Datos: medios_mexico.json  |  Proyecto: Maxicomm")
    print("=" * 70)

    # Lista completa
    print(f"\n📰  TODOS LOS MEDIOS ({len(medios)} registros)\n")
    imprimir_tabla(medios)

    # Filtro: solo Baja California
    bc = filtrar_por_region(medios, "Baja California")
    print(f"\n🌵  MEDIOS EN BAJA CALIFORNIA ({len(bc)} registros)\n")
    imprimir_tabla(bc)

    # Filtro: solo digitales
    digitales = filtrar_por_formato(medios, "Digital")
    print(f"\n💻  MEDIOS CON PRESENCIA DIGITAL ({len(digitales)} registros)\n")
    imprimir_tabla(digitales)

    print("\n✅  Fin del reporte.\n")


if __name__ == "__main__":
    main()
