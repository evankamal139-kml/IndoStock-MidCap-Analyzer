# Indonesian Mid-Cap Stock Analyzer
### Identifying "Big Money" Accumulation in Volatile Markets

## 📌 Project Overview
This project focuses on analyzing daily trading data of Indonesian Mid-Cap stocks ($2\text{T}–20\text{T}$ IDR). The primary goal is to detect **Institutional Accumulation** (Foreign/Big Money movement) to mitigate risk and identify "Alpha" growth opportunities through a quantitative, regime-aware framework.

## 🛠 Strategic Framework & Roadmap
The project is executed across six distinct phases, transitioning from raw data engineering to predictive machine learning.

- [x] **Phase 1: Automated Data Engineering** – Resilient Python pipeline for 3-month longitudinal IDX summaries and metadata synchronization.
- [x] **Phase 2: Strategic EDA** – Statistical normalization (`RobustScaler`) and Multicollinearity validation (VIF) to isolate $Y$ (Price), $X_1$ (Foreign Intensity), and $X_2$ (Volume).
- [ ] **Phase 3: Tiered Filtering (The Bucket System)** – *In Development.* Segmenting market cycles (Stable, Euphoria, Crash, Recovery) and bifurcating tickers into IHSG-Dominant ($K=3$) and Foreign-Dominant ($K=5$) buckets.
- [ ] **Phase 4: Deviation & Regime Shift Analysis** – Implementing Euclidean Distance checks and **Idiosyncratic Risk Isolation Audits** to detect "Category Flips" (Alpha de-coupling).
- [ ] **Phase 5: Strategic Synthesis** – Data-driven execution signals for "Tactical Liquidity Harvesting" (Exit) and "Asymmetric Opportunity Identification" (Entry).
- [ ] **Phase 6: Predictive Synthesis** – Forward-testing via XGBoost/Hybrid Neural Architectures and real-time inference for "Regime Flips."

## ⚙️ Technical Implementation
### **Data Pipeline Architecture**
1. **Ingestion:** Automated collection of IDX trading data using `glob` and `config` parameters.
2. **Masking:** Implementation of data privacy through unique ticker hashing and removal of sensitive corporate metadata.
3. **Cleaning & Filtering:** * **Sanitization:** Regex-based cleaning of Indonesian-localized currency and date formats.
    * **Universe Gatekeeper:** Strict filtering for 'Utama' and 'Pengembangan' boards within the Mid-Cap market cap range.
4. **Exploratory Data Analysis (EDA):** * **Strategic Audit:** Identification of "Alpha Tickers" (Foreign-correlated) and "Coiling Springs" (Volume breakouts).

## 🧬 Data Science Stack
- **Languages:** Python (Pandas, NumPy, Importlib)
- **Visualization:** Seaborn, Matplotlib
- **Analysis:** Statsmodels (VIF), YFinance
- **Machine Learning:** Scikit-Learn (Clustering), XGBoost (Planned for Phase 6)

## 📂 Data Sources
- **Primary Trading Data:** [IDX - Ringkasan Saham](https://www.idx.co.id/id/data-pasar/ringkasan-perdagangan/ringkasan-saham/)
- **Master List:** [IDX - Daftar Saham](https://www.idx.co.id/id/data-pasar/data-saham/daftar-saham/)
- **Benchmark Data:** IHSG ($^JKSE$) via `yfinance` API.

---

> **Disclaimer:** *This project is for educational and data science portfolio purposes only. It does not constitute financial advice. All investment decisions should be made based on individual research and risk tolerance.*
