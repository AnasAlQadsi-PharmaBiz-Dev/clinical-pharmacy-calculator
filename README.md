# Clinical Pharmacy Calculator (v1.2) 🧪

حاسبة سريرية متقدمة مصممة بلغة Python لحساب تصفية الكرياتينين (CrCl) بدقة، مع التحديد التلقائي للوزن الأنسب (الفعلي، المثالي، أو المعدل)، وحساب مساحة سطح الجسم (BSA)، وتوصيات سريرية أولية لضبط جرعة دواء الفانكومايسين (Vancomycin).

---

## 🔬 المعادلات السريرية المعتمدة (Clinical Formulas)

### 1. تصفية الكرياتينين (Cockcroft-Gault Equation)
- **الذكور:**
  $$\text{CrCl} = \frac{(140 - \text{Age}) \times \text{Weight}}{72 \times \text{SCr}}$$
- **الإناث:**
  $$\text{CrCl} = \text{CrCl (Male)} \times 0.85$$

---

### 2. معايير اختيار الوزن (Weight Selection Logic)
تختار الحاسبة تلقائياً نوع الوزن المناسب بناءً على الحالة السريرية للمريض:
- **نقص الوزن ($Actual < IBW$):** استخدام الوزن الفعلي ($Actual\ Weight$).
- **الوزن الطبيعي ($IBW \le Actual \le 1.2 \times IBW$):** استخدام الوزن المثالي ($IBW$).
- **السمنة ($Actual > 1.2 \times IBW$):** استخدام الوزن المعدل ($ABW$).

---

### 3. الوزن المثالي (Devine Formula)
- **الذكور:** $50 + 2.3 \times (\text{Height in inches} - 60)$
- **الإناث:** $45.5 + 2.3 \times (\text{Height in inches} - 60)$

---

### 4. الوزن المعدل (Adjusted Body Weight)
$$\text{ABW} = \text{IBW} + 0.4 \times (\text{Actual Weight} - \text{IBW})$$

---

### 5. مساحة سطح الجسم (Mosteller Formula)
$$\text{BSA} = \sqrt{\frac{\text{Height (cm)} \times \text{Weight (kg)}}{3600}}$$

---

## 💊 توصيات جرعات الفانكومايسين (Vancomycin Dosing v1.2)

| تصفية الكرياتينين (CrCl) | الفترة البينية الموصى بها (Interval) | الملاحظات السريرية (Clinical Notes) |
| :--- | :--- | :--- |
| **$> 50 \text{ mL/min}$** | كل 8 - 12 ساعة | وظائف كلى طبيعية، يوصى بمتابعة المستوى الأدنى للدواء (Trough Level). |
| **$20 - 50 \text{ mL/min}$** | كل 24 ساعة | قصور كلي متوسط، يتطلب تمديد الفترة البينية للجرعات. |
| **$< 20 \text{ mL/min}$** | حسب نتائج TDM | قصور كلي شديد، النظر في إعطاء جرعة تحميلية ومراقبة التركيز في الدم. |

---

## 💻 طريقة الاستخدام (Usage Example)

```python
from calculator import calculate_crcl

# مدخلات الحالة السريرية
result = calculate_crcl(
    gender="male",
    age=65,
    weight_kg=95,
    height_cm=175,
    scr=1.4
)

print(result)

📋 المخرجات النموذجية (Sample Output)
{
  "CrCl_mL_min": 52.48,
  "IBW_kg": 70.3,
  "BSA_m2": 2.15,
  "Weight_Used_Type": "Adjusted Body Weight (Obesity)",
  "Weight_Used_kg": 80.18,
  "Vancomycin_Dosing": {
    "Recommended_Interval": "Every 8 to 12 hours",
    "Clinical_Note": "Normal renal function dosing. Target trough monitoring recommended."
  }
}

تنويه: هذه الأداة مخصصة للمساعدة التعليمية والدعم السريري المبدئي، ولا تغني عن التقييم الطبي المباشر.

---

### **طريقة التنسيق والحفظ:**
1. انسخ الكود أعلاه كاملاً.
2. ألصقه في محرر ملف **`README.md`** عبر GitHub.
3. اضغط على الزر الأخضر **`Commit changes`**.

