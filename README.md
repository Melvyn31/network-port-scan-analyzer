# 🌐 Network Port Scan & Analyzer

Projet personnel réalisé dans le cadre de ma 2ᵉ année en cybersécurité.

---

## 🎯 Objectifs

- Réaliser un scan réseau pour détecter les hôtes et ports ouverts  
- Analyser automatiquement les résultats avec un script Python  
- Identifier les services exposés et les risques associés  

---

## ⚙️ Environnement utilisé

- 🐧 Kali Linux / Parrot OS  
- 🔎 Nmap  
- 🐍 Python 3.x  

---

## 💻 Scripts

### `scripts/analyzer.py`

Script Python qui analyse un fichier XML généré par Nmap, affiche les hôtes détectés, leurs ports ouverts, les services associés, et alerte sur les services sensibles exposés (FTP, SSH, Telnet, SMB).

### Fichiers importants liés au script

- `scripts/analyzer.py` : le script d’analyse principal  
- `scans/scan-result.xml` : exemple de fichier XML généré par Nmap pour tester le script  

---

## 💡 Exemple de commande Nmap

```bash
nmap -sS -T4 -A -v 192.168.1.0/24 -oX scans/scan-result.xml
