# 🕵️‍♂️ Cyber Threat Intelligence Dashboard

## 📌 Project Overview

A web-based OSINT (Open Source Intelligence) dashboard that allows users to gather public threat data using domain, email, IP address, or username as input. This dashboard integrates tools and APIs like `theHarvester`, `Shodan`, `emailrep.io`, and `whois` to display actionable intelligence.

---

## 🎯 Features

- 🔍 Accepts input: domain, email, username, or IP
- 🛠 Integrates multiple tools:
  - `theHarvester` – gathers emails & hosts
  - `Shodan API` – fetches exposed devices
  - `emailrep.io` – reputation & breach check
  - `whois` – domain ownership info
- 📊 Displays results in clean UI
- 🕓 Search history tracking (session-based)
- 📤 Export result as PDF

---

## 🧰 Tech Stack

| Layer      | Tools Used              |
|------------|--------------------------|
| Backend    | Python, Django            |
| Frontend   | HTML, CSS, JavaScript     |
| OSINT Tools| theHarvester, whois       |
| APIs       | Shodan API, emailrep.io   |

---

## 🚀 Setup Instructions

### Clone the Repo

```bash
git clone https://github.com/prince-python/cyberSecurityInternship.git
cd final_project_cyber_dashboard
