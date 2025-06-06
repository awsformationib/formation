
# 🧪 Fiche – Connexion Python à du matériel de mesure

## 🧰 1. **Bibliothèques Python spécialisées**

| Package                 | Utilité principale                                                      |
| ----------------------- | ----------------------------------------------------------------------- |
| `pyvisa`                | Interface VISA pour instruments GPIB, USB, RS232, Ethernet              |
| `pyserial`              | Communication série RS232/USB                                           |
| `python-gphoto2`        | Contrôle d’appareils photo via libgphoto2                               |
| `pyusb`                 | Accès aux périphériques USB (bas niveau)                                |
| `pymodbus`              | Connexion aux automates industriels (Modbus RTU/TCP)                    |
| `minimalmodbus`         | Alternative simple pour Modbus RTU (port série)                         |
| `python-can`            | Communication sur bus CAN                                               |
| `pymavlink`             | Contrôle de drones ou robots via protocole MAVLink                      |
| `scpi-parser`, `qcodes` | Contrôle d’instruments via commandes SCPI (oscilloscopes, multimètres…) |
| `labjack`, `ni-daqmx`   | Accès aux cartes d’acquisition LabJack ou National Instruments          |

---

## 🔌 2. **Protocoles de communication courants**

| Protocole           | Type                                   | Exemples de matériel utilisant ce protocole            |
| ------------------- | -------------------------------------- | ------------------------------------------------------ |
| **USB**             | Plug & play                            | Multimètres, stations météo, Arduino                   |
| **RS232/TTL/UART**  | Série                                  | Automates industriels, GPS, capteurs                   |
| **GPIB (IEEE-488)** | Bus parallèle                          | Instruments de laboratoire anciens                     |
| **VISA**            | Surcouche standard (GPIB, USB, TCP/IP) | Oscilloscopes Keysight, Tektronix, etc.                |
| **SCPI**            | Commandes standardisées via VISA       | Générateurs de signaux, multimètres, analyseurs        |
| **Modbus**          | Industriel                             | PLC, capteurs industriels, compteurs                   |
| **I2C / SPI**       | Bas niveau (bus)                       | Modules embarqués, capteurs sur Raspberry Pi / Arduino |
| **CAN**             | Réseau                                 | Véhicules, robots, capteurs industriels synchrones     |
| **TCP/IP, UDP**     | Réseau                                 | Instruments modernes connectés à Ethernet              |
| **Bluetooth / BLE** | Sans-fil                               | Appareils portables, IoT                               |

---

## 📦 3. **Cas d’usage typiques avec Python**

| Cas d’usage                              | Packages recommandés          | Exemple rapide                     |
| ---------------------------------------- | ----------------------------- | ---------------------------------- |
| Lire un capteur de température USB       | `pyserial`, `pyusb`           | `ser.readline()`                   |
| Contrôler un oscilloscope via USB ou LAN | `pyvisa`, SCPI                | `instr.write(\"MEAS:VOLT?\")`      |
| Lire une tension depuis une carte NI     | `ni-daqmx` (via NI-DAQmx)     | `AnalogInputTask()`                |
| Lire un compteur industriel Modbus       | `pymodbus`, `minimalmodbus`   | `client.read_input_registers(...)` |
| Recevoir données CAN d’un robot          | `python-can`                  | `bus.recv()`                       |
| Communiquer avec une station météo       | `pyserial` ou parfois `pyusb` | `ser.read(32)`                     |

---

## 🧑‍💻 4. **Exemple avec `pyvisa` + SCPI**

```python
import pyvisa

rm = pyvisa.ResourceManager()
scope = rm.open_resource('USB0::0x0957::0x1796::INSTR')
scope.write('*IDN?')
print(scope.read())  # Renvoie le modèle de l'appareil

scope.write('MEASure:VOLTage:DC? CHANNEL1')
print(scope.read())  # Mesure la tension DC sur CH1
```

---

## 🔍 5. Outils utiles et simulateurs

| Outil                        | Utilité                                                     |
| ---------------------------- | ----------------------------------------------------------- |
| **NI MAX**                   | Détection VISA et GPIB (National Instruments)               |
| **Keysight IO Libraries**    | Interface VISA pour instruments Keysight                    |
| **Sigrok + PulseView**       | Logiciel de décodage de signaux logiques                    |
| **QCoDeS**                   | Framework de mesure et pilotage instrumenté                 |
| **LabView**                  | Complément graphique à Python dans le contrôle de matériels |
| **Serial Plotter (Arduino)** | Visualisation rapide des signaux séries                     |

---

## ✅ Bonnes pratiques

* Utiliser `try/except` autour de toute communication physique
* Ajouter des `timeout` pour éviter les blocages
* Lire la documentation SCPI ou Modbus de l’instrument cible
* Utiliser un logger (`loguru`, `logging`) pour tracer les échanges
* Documenter soigneusement les adresses, ports, et configurations des appareils
