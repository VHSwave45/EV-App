# Laadpaal Management Systeem
Dit project bevat een eenvoudige backend (Python + MySQL) en frontend (HTML/CSS/JS) voor het Laadpaal Management Systeem.
---
## Vereisten, zorg dat je deze geinstalleerd hebt:
- Python 3.12+
- Docker Desktop
- Browser (Chrome, Firefox, etc.)
## Setup
### 0. Startup
Zorg dat Docker op de achtergrond draait
### 1. Backend (Python + MySQL)
1. Start de database met Docker Compose:

```bash
docker compose up -d
````

2. Installeer Python dependencies:

```bash
cd backend
python -m pip install --user -r requirements.txt
```

3. Maak een bestand genaamd config.py

4. Vul deze velden in config.py:

```bash
DB_HOST = ""                # Database host (IP address or hostname, Bijv. localhost)
DB_PORT =                   # Database port (Bijv. 3306)
DB_NAME = ""                # Database name
DB_USER = ""                # Database user (Bijv. root)
DB_PASSWORD = ""            # Database password

SERVER_HOST = ""            # Server host (IP address or hostname, Bijv. localhost)
SERVER_PORT =               # Server port
```

5. Start de backend server:

```bash
python server.py
```

De backend draait nu op: [http://localhost:8000](http://localhost:8000)

---

### 2. Frontend
1. Open [http://localhost](http://localhost) in je browser.
2. De backend serveert automatisch de frontend.
3. De frontend haalt automatisch de messages op van de backend en toont deze.
4. Als alles correct werkt, zie je een webpagina met de tekst:

---

"Welkom bij het Laadpaal Management Systeem"

"Hello World"

---

## Database
* Database: `evbox_manager`
* Tabel: `messages`
* Kolommen: `id`, `message`

---

## Dependencies
Python-dependencies staan in `backend/requirements.txt`.
Om ze te installeren:

```bash
python -m pip install --user -r requirements.txt
```

---

## Veelvoorkomende issues

* **CORS fouten** → start backend via `server.py` en frontend vanaf hetzelfde domein of via `localhost`.
* **Python kan niet gevonden worden op windows** → check of python in je path staat. Zoek in windows naar environment variables. 
Deze staan in de system properties op de advanced settings tab rechts onder. Voeg `C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313` 
en `C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python313\Scripts`
toe als ze nog niet in je path staan. Herstart de terminal. Als dit het probleem nog niet oplost kun je in windows zoeken naar manage app aliases. 
zet op deze pagina alles met python in de naam uit. Herstart de terminal.Als dit het probleem nog steeds niet oplost kun je navigeren naar `C:\Users\%USERNAME%\AppData\Local\Microsoft\WindowsApps` 
en verwijder alles gerelateerd aan python. Herstart de terminal.

---

## Opzetten van een Virtuele Omgeving (Aanbevolen voor Mac en Linux gebruikers)

Om afhankelijkheden gescheiden te houden en te voorkomen dat de systeem-Python beschadigd raakt, gebruik je het beste een virtuele omgeving.

```bash
# Maak een virtuele omgeving in de projectmap
python3 -m venv venv

# Activeer de virtuele omgeving
source venv/bin/activate

# Installeer de vereiste pakketten
pip install -r requirements.txt

# Elke keer dat je terugkomt naar het project, activeer je de omgeving opnieuw met:
source venv/bin/activate
```
---

## Database updaten

Wanneer er wijzigingen zijn in de database-structuur (bijvoorbeeld nieuwe tabellen, kolommen of constraints), moet je de databasecontainers opnieuw opbouwen. Hieronder vind je de stappen:

### 1. Stop de database containers

Ga eerst naar de Database-map en stop de draaiende containers.

```bash
cd Database
docker compose down
```

### 2. Start en rebuild de containers

Start de containers opnieuw op. Door --build of een herstart via up -d worden de nieuwste wijzigingen toegepast.

```bash
docker compose up -d --build
```
* ```-d``` → draait de containers in de achtergrond.

* ```--build``` → forceert een rebuild, zodat de laatste wijzigingen in de configuratie worden meegenomen.

### 3. Verwijderd de ongebruikte volumes

Na een update kunnen oude volumes achterblijven die niet meer gebruikt worden. Deze kun je verwijderen om schijfruimte vrij te maken:

```bash
docker volume prune
```

Je krijgt een bevestigingsvraag:

```bash
Are you sure you want to continue? [y/N] y
```

Typ ```y``` om door te gaan. **Let op**: hiermee worden alle ongebruikte volumes verwijderd, dus ook die van andere projecten.