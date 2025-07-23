# network-port-scan-analyzer
Projet perso : scan Nmap d'un réseau local et analyse automatique en Python.
# 🌐 Network Port Scan & Analyzer

Projet personnel réalisé dans le cadre de ma 2ᵉ année en cybersécurité.  
Objectif : scanner un réseau local à l’aide de **Nmap**, puis analyser les résultats avec un **script Python** personnalisé.

---

## ⚙️ Environnement utilisé

- 🐧 Kali Linux / Parrot OS
- 🔎 Nmap
- 🐍 Python 3.x

---

## Objectifs

- Réaliser un **scan réseau** pour détecter les hôtes et ports ouverts
- Analyser automatiquement les résultats avec un **script Python**
- Identifier les **services exposés** et les risques associés

---

## Exemple de commande Nmap

```bash
nmap -sS -T4 -A -v 192.168.1.0/24 -oX scans/scan-result.xml

## 🗂️ Fichiers importants

- `scripts/analyzer.py` : script Python pour analyser un fichier XML Nmap  
- `scans/scan-result.xml` : exemple de fichier XML généré par Nmap pour tester le script

### Lancer l’analyse

```bash
python3 scripts/analyzer.py scans/scan-result.xml

