# Indonesian Mid-Cap Stock Analyzer
### Identifying "Big Money" Accumulation in Volatile Markets

## 📌 Project Overview
This project focuses on analyzing daily trading data of Indonesian Mid-Cap stocks. The primary goal is to detect **Institutional Accumulation** (Foreign/Big Association movement) to mitigate risk and identify "Alpha" growth opportunities.

## 🛠 Strategic Framework
1. **Regime Identification:** Segmenting data into four market phases (Stable, Euphoria, Crash, Recovery).
2. **Feature Stratification:** Separating IHSG-dependent stocks from Foreign-driven Tickers.
3. **Clustering:** Using K-Means to categorize stocks into performance tiers and Wyckoff accumulation stages.
4. **Predictive Modeling:** Generating probability-based price forecasts for each market regime.

## ⚙️ Technical Implementation & Environment
The project is structured into a modular pipeline to ensure data integrity and reproducibility.

### **Data Pipeline Architecture**
1. **Ingestion:** Automated collection of Indonesian stock trading data using `glob` and custom `config` parameters.
2. **Masking:** Implementation of data privacy through unique ticker hashing and removal of sensitive corporate metadata.
3. **Cleaning & Filtering:** - **Sanitization:** Regex-based cleaning of Indonesian currency/date formats.
    - **Universe Gatekeeper:** Filtering for 'Utama' and 'Pengembangan' boards.
    - **Market Cap Segmentation:** Narrowing focus to the $2\text{T} - 20\text{T}$ IDR Mid-Cap range.
4. **Exploratory Data Analysis (EDA):** - **Statistical Validation:** Multicollinearity (VIF) and ARA/ARB detection.
    - **Strategic Audit:** Identification of "Alpha Tickers" (Foreign-correlated) and "Coiling Springs" (Volume breakouts).

## 🧬 Data Science Stack
- **Languages:** Python (Pandas, NumPy, Importlib)
- **Visualization:** Seaborn, Matplotlib
- **Analysis:** Statsmodels (VIF), YFinance
- **Machine Learning:** Scikit-Learn (Planned for Phase 3)

## 📂 Data Sources
- **Primary Trading Data:** [IDX - Ringkasan Saham](https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/)
- **Master List:** [IDX - Daftar Saham](https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/)
- **Benchmark Data:** IHSG ($^JKSE$) via `yfinance` API.
