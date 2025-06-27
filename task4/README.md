# 🛡️ Cyber Security Internship – Task 4

## 📌 Task Title: Setup and Use a Firewall on Windows

## 🎯 Objective:
To configure basic inbound firewall rules on Windows 10 to control and filter network traffic using Windows Defender Firewall.

---

## 🛠 Tools Used:
- Windows Defender Firewall with Advanced Security
- OS: Windows 10

---

## 🔧 Configuration Steps:

### 1. Block Inbound Traffic on Telnet Port (TCP 23)
- Created a new inbound rule to block TCP port 23.
- Rule applied to all profiles: Domain, Private, Public.

### 2. Allow Inbound SSH Traffic (Port 22)
- Added a rule to explicitly allow TCP traffic on port 22.

### 3. (Optional) Deleted the Telnet rule after testing.

---

## 🔍 Understanding:

- **Port 23** (Telnet) is blocked because it's insecure and often used by attackers.
- **Port 22** (SSH) is allowed for secure remote connections.
- Firewalls filter traffic based on port, IP, and protocol rules.

---

## 📁 Files Included:
- `README.md`
- `screenshot_telnet_block.png`
- `screenshot_ssh_allow.png`

---



---

## 👤 Author:
**Prince Chaudhary**  
Cyber Security Intern at Elevate Labs  
📍 Indore, India
