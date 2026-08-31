# 🧪 Multi-Drug Clinical Pharmacy Calculator (v1.3)
An interactive Clinical Decision Support System (CDSS) built with Python and Gradio to compute **Creatinine Clearance (CrCl)** using the Cockcroft-Gault equation and provide patient-specific dosing recommendations for multiple high-alert medications.
---
## 🌟 Key Features
- **Smart Weight Selection:** Automatically detects Obesity ($Actual > 1.2 \times IBW$) or Underweight status to use Adjusted Body Weight ($ABW$) or Actual Weight ($ABW$) accordingly.
- **BSA & IBW Calculation:** Computes Ideal Body Weight (Devine Formula) and Body Surface Area (Mosteller Formula).
- **Multi-Drug Dosing Support:**
  - **Vancomycin:** Interval guidance based on renal excretion levels.
  - **Rivaroxaban (DOAC):** Dose adjustments for NVAF based on renal thresholds.
  - **Enoxaparin (LMWH):** Therapeutic dosing guidelines for normal vs. impaired renal clearance ($CrCl < 30\text{ mL/min}$).
- **Interactive Web Interface:** User-friendly GUI powered by **Gradio**.
---
## 📊 Clinical Logic Flow

| Parameter | Formula / Condition |
| :--- | :--- |
| **IBW (Male)** | $50 + 2.3 \times (Height\_in - 60)$ |
| **IBW (Female)** | $45.5 + 2.3 \times (Height\_in - 60)$ |
| **ABW** | $IBW + 0.4 \times (Actual - IBW)$ |
| **CrCl** | $\frac{(140 - Age) \times Weight}{72 \times SCr} \times [0.85\text{ if female}]$ |

---
## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/clinical-pharmacy-calculator.git](https://github.com/YOUR_USERNAME/clinical-pharmacy-calculator.git)
2. Install requirements:
pip install gradio
3. Run the application:
python app.py

👨‍⚕️ Author
Developed by Anas Ahmad — Pharmacist & Business Development Specialist | HealthTech & AI Solutions.
