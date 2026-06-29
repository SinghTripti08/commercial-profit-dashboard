# Commercial Growth & Profit Margin Dashboard (Vibrational Number: 8)

## 📌 Project Overview
This repository contains an end-to-end Sales & Profit Performance solution engineered for **Business Analytics** and **Business Consulting** frameworks. Operating on the frequency of **Number 8**, this project is fundamentally designed around material optimization, financial scale, and structural efficiency. 

Instead of focusing purely on top-line vanity metrics (gross sales), this dashboard deep-dives into bottom-line realities: **margin health, regional variance, and supply chain cost vulnerabilities.**

### 📊 Key Features
* **Dynamic Margin Tracking:** Real-time visibility into Gross Margin % and Net Profit Margin % across diverse product segments and territories.
* **Executive "What-If" Simulation Tool:** A parameter-driven engine allowing C-suite executives to model how fluctuations in supply chain costs ($+5\%$, $+10\%$, etc.) or shifts in pricing strategies immediately impact the bottom-line net profit.
* **Strategic Variance Analysis:** Deep-dives into underperforming regional sales teams and product lines bleeding cash.

---

## 🛠️ Tech Stack & Tools
* **BI & Visualization:** Power BI (DAX, Power Query)
* **Data Generation & Pipeline:** Python 3.x (Pandas, NumPy)
* **Version Control:** Git

---

## 📂 Repository Architecture
* `data/`: Contains the generated raw sales datasets and cost tables used to populate the model.
* `scripts/`: Python modular scripts to scale or regenerate the underlying business data.
* `dashboard/`: The core Power BI (.pbix) template file housing the data model, interactive visual layers, and DAX calculations.

---

## 🧮 Core DAX Measures (Financial Logic)

To maintain absolute financial rigor, the dashboard utilizes the following primary calculations:

### Total Sales:
$$Total\ Sales = SUM(Sales[Revenue])$$

### Gross Profit Margin:
$$Gross\ Margin\ \% = DIVIDE(SUM(Sales[Revenue]) - SUM(Sales[COGS]), SUM(Sales[Revenue]))$$

### Simulated Net Profit (What-If Parameter Integration):
$$Simulated\ Net\ Profit = [Total\ Gross\ Profit] - (SUM(Costs[SupplyChainCosts]) * (1 + 'Cost Scenario Parameter'[Cost Scenario Parameter Value]))$$

---

## 🎥 Executive Briefing (CFO Presentation)
A 3-minute recorded walkthrough simulating an executive boardroom presentation to the Chief Financial Officer is included below:

* **0:00 - 1:00:** Highlighting systemic margin erosion within underperforming regional quadrants.
* **1:00 - 2:15:** Deploying the "What-If" parameter tool to showcase the severe threat of a $5\%$ spike in supply chain costs.
* **2:15 - 3:00:** Actionable consulting recommendations for price optimization and cost containment.

👉 **[Link to Your Video Walkthrough (YouTube/Loom/Vimeo)]**

---

## 🚀 How to Run the Project
1. Clone this repository to your local machine.
2. Run `pip install -r requirements.txt` and execute `python scripts/data_generator.py` if you wish to generate fresh mock data.
3. Open `dashboard/Commercial_Profit_Dashboard.pbix` in Power BI Desktop to interact with the visualizations and "What-If" parameters.
