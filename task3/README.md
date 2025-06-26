# 🛡️ Cyber Security Internship – Task 3

## 📌 Task Title: Perform a Basic Vulnerability Scan

## 🎯 Objective:
To perform a vulnerability scan on my local system using Nessus Essentials. The goal was to identify potential security risks, understand their severity, and propose remediation steps based on industry best practices.

---

## 🛠 Tools Used:
- **Nessus Essentials** by Tenable
- **Target:** 127.0.0.1 (localhost)
- **Scan Type:** Basic Network Scan
- **Operating System:** Kali Linux

---

## 🔍 Summary of Scan Findings:

| Vulnerability Name                            | CVE ID         | Severity |
|-----------------------------------------------|----------------|----------|
| OpenSSH User Enumeration                      | CVE-2023-38408 | High     |
| Apache Path Traversal                         | CVE-2021-41773 | High     |
| Git Configuration Vulnerability               | CVE-2022-24765 | Medium   |
| ICMP Vulnerability (FAD)                      | CVE-2020-25705 | Medium   |
| SMBv1 Remote Code Execution (EternalBlue)     | CVE-2017-0143  | Critical |
| SSL/TLS Certificate Expiry                    | -              | Info     |

---

## ⚠️ Vulnerability Severity Summary:
- 🔴 **Critical:** 1
- 🟠 **High:** 2
- 🟡 **Medium:** 2
- 🔵 **Info:** 1

---

## 🧠 Suggested Remediation:

- 🔐 **Update OpenSSH** to latest version
- 🔧 **Patch Apache** to fix path traversal
- 🚫 **Disable SMBv1** to prevent EternalBlue-like attacks
- 🧼 **Check Git user configs** for safety
- 🧾 **Renew self-signed or expired SSL certificates**
- 🌐 **Limit ICMP echo responses** via firewall rules

---

## 📂 Files Included:
- `scan_report.pdf` – Exported report from Nessus
- `README.md` – Task documentation

---

## 👨‍💻 Author:
**Prince Chaudhary**  
Cyber Security Intern at Elevate Labs  
📍 Indore, India
