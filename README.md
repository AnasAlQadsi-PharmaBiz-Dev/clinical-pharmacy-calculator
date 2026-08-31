# Clinical Pharmacy Calculator (v1.1) 🧪

حاسبة سريرية متقدمة مصممة بلغة Python لحساب تصفية الكرياتينين (CrCl) بدقة، مع التحديد التلقائي للوزن الأنسب (الفعلي، المثالي، أو المعدل) وحساب مساحة سطح الجسم (BSA).

---

## 🔬 المعادلات السريرية المعتمدة (Clinical Formulas)

### 1. Cockcroft-Gault Equation (CrCl)
$$\text{CrCl (Male)} = \frac{(140 - \text{Age}) \times \text{Weight (kg)}}{72 \times \text{SCr (mg/dL)}}$$
$$\text{CrCl (Female)} = \text{CrCl (Male)} \times 0.85$$

### 2. Devine Formula (Ideal Body Weight - IBW)
$$\text{IBW (Male)} = 50 + 2.3 \times (\text{Height in inches} - 60)$$
$$\text{IBW (Female)} = 45.5 + 2.3 \times (\text{Height in inches} - 60)$$

### 3. Adjusted Body Weight (ABW)
$$\text{ABW} = \text{IBW} + 0.4 \times (\text{Actual Weight} - \text{IBW})$$
*(يُستخدم تلقائياً في حسابات CrCl إذا كان وزن المريض الفعلي أكبر من 120% من وزنه المثالي)*.

### 4. Mosteller Formula (Body Surface Area - BSA)
$$\text{BSA (m²)} = \sqrt{\frac{\text{Height (cm)} \times \text{Weight (kg)}}{3600}}$$

---

## 🛡️ Medical Disclaimer
هذه الأداة مخصصة للأغراض التعليمية، والتدريبية، والتوثيق الميداني فقط. لا تُعد بديلاً عن التقدير السريري المباشر للصيدلاني أو الممارس الصحي المعتمد.
