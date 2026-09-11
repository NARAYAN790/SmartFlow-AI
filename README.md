\# 💧 SmartFlow AI



\### AI-Enabled Smart Water Management System



SmartFlow AI is an AI-assisted smart water monitoring prototype designed to identify unusual water-flow patterns, classify anomaly severity, and recommend appropriate maintenance actions for campus water management.



The prototype combines \*\*IoT-style sensor data, Machine Learning, anomaly detection, decision logic, AI-assisted interpretation, and an interactive Streamlit dashboard\*\* into one workflow.



> \*\*Prototype Note:\*\* The current implementation uses synthetic IoT-style water sensor data to validate the AI detection workflow. Physical sensor deployment is proposed as a future implementation phase.



\---



\## 🚨 Problem Statement



Water leakage and abnormal water usage in campuses can remain unnoticed because continuous monitoring is difficult with manual inspection.



SmartFlow AI aims to address this problem by:



\* Continuously analyzing water-flow records

\* Detecting unusual usage patterns

\* Classifying events based on severity

\* Providing understandable explanations

\* Recommending maintenance actions

\* Presenting monitoring results through a dashboard



\---



\## 💡 Solution



SmartFlow AI follows this workflow:



```text

IoT-Style Water Sensor Data

&#x20;           ↓

&#x20;     Data Processing

&#x20;           ↓

&#x20;     Feature Engineering

&#x20;           ↓

&#x20;    Isolation Forest

&#x20;           ↓

&#x20;  Anomaly Detection

&#x20;           ↓

&#x20;Severity Classification

&#x20;           ↓

&#x20;   Decision Layer

&#x20;           ↓

&#x20;AI-Assisted Interpretation

&#x20;           ↓

&#x20;   Streamlit Dashboard

&#x20;           ↓

&#x20;Maintenance Recommendation

```



\---



\## 🧠 Machine Learning Approach



SmartFlow AI uses \*\*Isolation Forest\*\* for unsupervised anomaly detection.



\### Input Features



The model analyzes:



\* Flow rate

\* Water consumption

\* Duration

\* Hour

\* Day of week

\* Weekend indicator



The original `scenario` label is not used as a model input. It is retained for validation and comparison.



\### Model Configuration



```text

Algorithm: Isolation Forest

Estimators: 200

Contamination: 0.10

Random State: 42

```



The model produces:



```text

1   → Normal

\-1  → Anomaly

```



Anomalies are further classified into:



\* 🟢 Normal

\* 🟡 Suspicious

\* 🔴 Critical



\---



\## ⚙️ Decision Layer



The decision layer converts detected anomalies into understandable maintenance information.



\### Normal



\*\*Reason:\*\*

Water usage pattern is within the expected range.



\*\*Action:\*\*

No immediate maintenance action is required.



\### Suspicious



\*\*Reason:\*\*

Unusual flow pattern indicating possible abnormal usage or early leakage.



\*\*Action:\*\*

Schedule inspection and continue monitoring.



\### Critical



\*\*Reason:\*\*

Very high flow, prolonged duration, and high water consumption.



\*\*Action:\*\*

Immediate inspection of taps, pipes, valves, fittings, and nearby water lines is recommended.



> SmartFlow AI identifies \*\*possible or suspected leakage patterns\*\*; it does not claim physical leakage confirmation without real-world sensor validation.



\---



\## 🤖 AI Water Agent



The AI-assisted interpretation layer converts anomaly information into human-readable insights.



It provides:



\* Zone-wise anomaly analysis

\* Severity information

\* Flow and consumption context

\* Explanation of unusual patterns

\* Maintenance recommendations



\### Example



```text

Zone: AI Lab

Severity: Critical

Flow Rate: 24.81 L/min

Duration: 59.77 min

Consumption: 1482.62 L



Explanation:

Critical water-flow anomaly detected in AI Lab.

This pattern indicates possible continuous water flow

or suspected leakage.



Recommendation:

Immediate inspection is recommended. Check taps, pipes,

valves, fittings, and nearby water lines.

```



\---



\## 📊 Dashboard



The SmartFlow AI dashboard is built using \*\*Streamlit\*\*.



\### Dashboard Features



\* Total sensor records

\* Critical anomaly count

\* Suspicious event count

\* Normal pattern count

\* Water-flow monitoring table

\* Priority alerts

\* Anomaly overview

\* Pattern distribution

\* Zone-wise analysis

\* AI Water Agent

\* Downloadable reports

\* Monitoring settings



\### Dashboard Pages



| Page            | Purpose                                      |

| --------------- | -------------------------------------------- |

| Dashboard       | Overall water monitoring and priority alerts |

| Water Flow Data | Filter and inspect sensor records            |

| Zone Analysis   | Analyze water usage by campus zone           |

| AI Agent        | View AI-assisted anomaly explanations        |

| Reports         | View statistics and download reports         |

| Settings        | Configure monitoring preferences             |



\---



\## 📈 Prototype Results



The prototype dataset contains:



\* \*\*8,000\*\* water-flow records

\* \*\*12\*\* campus zones

\* \*\*6\*\* original sensor/data attributes



\### Dataset Scenario Distribution



| Scenario   |   Records |

| ---------- | --------: |

| Normal     |     6,836 |

| Suspicious |       771 |

| Critical   |       393 |

| \*\*Total\*\*  | \*\*8,000\*\* |



\### Isolation Forest Output



| Classification |   Records |

| -------------- | --------: |

| Normal         |     7,200 |

| Suspicious     |       549 |

| Critical       |       251 |

| \*\*Total\*\*      | \*\*8,000\*\* |



During validation, the prototype identified all injected critical anomaly patterns while maintaining normal classification for the normal-pattern records.



\---



\## 🗂️ Project Structure



```text

SmartFlow-AI/

│

├── agent/

│   └── smartflow\_agent.py

│

├── dashboard/

│   └── app.py

│

├── data/

│   ├── generate\_dataset.py

│   ├── water\_sensor\_data.csv

│   ├── processed\_water\_data.csv

│   ├── anomaly\_results.csv

│   └── decision\_results.csv

│

├── decision/

│   └── decision\_layer.py

│

├── model/

│   └── anomaly\_detection.py

│

├── processing/

│   └── data\_processing.py

│

├── .gitignore

├── requirements.txt

└── README.md

```



\---



\## 🛠️ Technology Stack



\### Programming \& Data



\* Python

\* Pandas

\* NumPy

\* Scikit-learn



\### Machine Learning



\* Isolation Forest

\* Feature Engineering

\* Anomaly Detection



\### Application



\* Streamlit

\* Plotly



\### AI



\* Local AI-assisted interpretation layer

\* Rule-based decision logic

\* Explainable anomaly recommendations



\### Future IoT Layer



\* Water Flow Sensor

\* ESP32

\* Wi-Fi / IoT Connectivity

\* Real-time sensor transmission



\---



\## 🚀 How to Run



\### 1. Clone the repository



```bash

git clone https://github.com/NARAYAN790/SmartFlow-AI.git

```



\### 2. Open the project



```bash

cd SmartFlow-AI

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Run the Streamlit dashboard



```bash

streamlit run dashboard/app.py

```



The dashboard will open in your browser.



\---



\## 🔬 Future Scope



The current prototype can be extended into a physical IoT-based water monitoring system.



\### Proposed Future Architecture



```text

Flow Sensor

&#x20;    ↓

&#x20;  ESP32

&#x20;    ↓

Wi-Fi / IoT Network

&#x20;    ↓

Cloud / Data Platform

&#x20;    ↓

Anomaly Detection

&#x20;    ↓

AI Interpretation

&#x20;    ↓

Alert / Dashboard

&#x20;    ↓

Maintenance Team

```



Future improvements may include:



\* Real-time flow sensors

\* ESP32-based data acquisition

\* Cloud data storage

\* Real-time alerts

\* Mobile notifications

\* More advanced anomaly detection

\* Historical trend prediction

\* Automated valve control

\* Campus-wide deployment



\---



\## 📚 Research \& Conceptual References



SmartFlow AI was developed with reference to existing research and open-source implementations related to:



\* IoT-based water monitoring

\* Water leakage detection

\* Isolation Forest anomaly detection

\* Smart campus water management

\* AI-assisted water network monitoring



The implementation is an independent prototype combining these concepts with a synthetic dataset, custom severity classification, decision logic, AI-assisted interpretation, and a Streamlit dashboard.



\### Selected References



\* IIIT Bangalore — Water Management System

&#x20; https://github.com/mukund01001/Water-Management-System-IIITB



\* IEEE — Machine Learning Schemes for Leak Detection in IoT-enabled Water Transmission System

&#x20; https://ieeexplore.ieee.org/document/10100175/



\* IEEE — Low-Cost IoT-Enabled Water Leak Detection and Prevention System Using Anomaly Detection in Sensor Networks

&#x20; https://ieeexplore.ieee.org/document/11493178/



\* IIT Jodhpur — Campus Water Distribution and Digital Twin Research

&#x20; https://www.sciencedirect.com/science/article/pii/S2405896324000491



\---



\## 👨‍💻 Developer



\*\*Narayan Gupta\*\*



B.Tech — Electrical \& Electronics Engineering

Dr. Ambedkar Institute of Technology for Divyangjan, Kanpur

AKTU | Batch 2027



\---



\## 📌 Project Disclaimer



SmartFlow AI is currently a prototype developed using synthetic IoT-style water-flow data.



No physical water sensors have been deployed as part of the current prototype. Real-world leakage confirmation and automated control would require physical sensor deployment, calibration, field testing, and appropriate safety validation.



\---



\## 🌱 Project Vision



> \*\*Detect early. Understand clearly. Act quickly. Save water.\*\*



SmartFlow AI aims to demonstrate how AI and IoT technologies can support smarter, more sustainable water management in educational campuses and similar environments.



