# 📰 Principales Medios de Comunicación de México

Repositorio generado por **Maxicomm** para monitoreo y referencia de medios nacionales y regionales de México.

## Contenido

| Archivo | Descripción |
|---|---|
| `medios_mexico.json` | Base de datos de medios en formato JSON (25 registros) |
| `medios_mexico.py` | Script Python para leer, filtrar e imprimir la lista |

## Medios incluidos

### Nacionales
- El Universal, Reforma, La Jornada, Milenio, El Financiero, Excélsior
- El Economista, Proceso, Animal Político, Expansión
- Sin Embargo, Aristegui Noticias, Forbes México
- Televisa / Noticieros Televisa, TV Azteca / ADN40, Imagen Televisión
- W Radio, MVS Noticias

### Baja California
- **La Estampida Digital** — https://laestampidadelosbufalos.com.mx/la-estampida-digital
- **El Vigía (Issuu)** — https://issuu.com/editorialelvigia
- Frontera, ZETA Semanario, El Mexicano

### Otros regionales
- Diario de Yucatán (Sureste), El Norte (Noreste)

## Estructura del JSON

```json
{
  "id": 20,
  "nombre": "La Estampida Digital",
  "tipo": "Portal de noticias digital Baja California",
  "url": "https://laestampidadelosbufalos.com.mx/la-estampida-digital",
  "region": "Baja California",
  "formato": "Digital"
}
```

## Uso del script Python

```bash
python medios_mexico.py
```

El script imprime:
1. Lista completa de medios
2. Filtro por región: Baja California
3. Filtro por formato: Digital

## Agregar un medio nuevo

Edita `medios_mexico.json` y agrega un objeto con la misma estructura. El campo `notas` es opcional.

---

## Cómo subir este repositorio a GitHub

```bash
# 1. Crea un repositorio nuevo en github.com (sin inicializar)
# 2. En tu máquina local, desde la carpeta con estos archivos:

git init
git add .
git commit -m "feat: lista inicial de principales medios de México"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/medios-mexico.git
git push -u origin main
```

> Reemplaza `TU_USUARIO` con tu nombre de usuario de GitHub.

---

*Proyecto: Maxicomm — Ensenada, Baja California, México*
