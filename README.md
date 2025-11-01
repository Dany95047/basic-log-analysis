# 🔐 Basic Log Analysis — Windows Failed Login Investigation (Event ID 4625)

This project analyzes Windows Security.evtx logs to investigate failed logon attempts (Event ID 4625) and find patterns that may indicate brute force attacks, credential guessing, or suspicious authentication behavior.
The dataset comes from a Windows endpoint (local machine) — the logs were exported from **Event Viewer → Windows Logs → Security** and then parsed with Python.
This is an **entry-level SOC analyst project** in my portfolio.



## 🧰 Tools Used


| Category | Tools |

| Language | Python |

| Notebook | Jupyter Notebook |

| Parsing | python-evtx, lxml |

| Analysis | pandas |

| Visualization | matplotlib |



## 🎯 Project Goals

- Parse Windows Security.evtx logs from a local Windows machine
- Extract key fields: timestamp, user, IP, logon type, status, substatus
- Identify failed logon attempts (Event ID 4625)
- Visualize patterns to detect potential credential-based attacks such as:
&nbsp; - repeated failed login attempts (burst analysis)
&nbsp; - remote vs local logon types (network vs console)
&nbsp; - time-of-day clustering
&nbsp; - successful login shortly after failures




## 📈 Key Findings (Highlights)

- Total Security events analyzed: **29,738**
- Failed logons (4625): **5 total**
- All failed logons were **LogonType 2** (Interactive / local console)
- No evidence of remote brute force or credential spraying in this dataset
- Successful logons after failures: not observed within threshold window

## 🖼️ Screenshots

These visualizations were generated directly from the parsed log data.

| ![Logon Type distribution](screenshots/logon\_type\_distribution.png) | Local vs network vs RDP logon type comparison |
| ![Failed logons by hour](screenshots/failed\_by\_hour.png) | Time-of-day pattern of failed logins |


## 📂 Repository Structure


basic-log-analysis/

├─ data/

│ ├─ failed\_logons.csv

│ └─ success\_logons.csv

├─ reports/

│ └─ Log\_Analysis\_Report.pdf ← (will be added later)

├─ screenshots/

│ ├─ failed\_by\_user.png

│ ├─ logon\_type\_distribution.png

│ └─ failed\_by\_hour.png

├─ scripts/

│ └─ analysis.ipynb

├─ requirements.txt

└─ README.md

