import math
import json
import gradio as gr

# 1. المعادلات الأساسية
def calculate_ibw(gender: str, height_cm: float) -> float:
    height_inches = height_cm / 2.54
    over_60_inches = max(0.0, height_inches - 60)
    if gender in ['male', 'ذكر']:
        return 50.0 + (2.3 * over_60_inches)
    else:
        return 45.5 + (2.3 * over_60_inches)

def calculate_abw(actual_weight: float, ibw: float) -> float:
    return ibw + 0.4 * (actual_weight - ibw)

def calculate_bsa(height_cm: float, weight_kg: float) -> float:
    return math.sqrt((height_cm * weight_kg) / 3600)

# 2. منطق التوصيات السريرية للأدوية (Clinical Decision Support)
def get_drug_dosing(crcl: float) -> dict:
    # Vancomycin
    if crcl > 50:
        vanco = "15-20 mg/kg q8-12h (Normal renal function)"
    elif 20 <= crcl <= 50:
        vanco = "15-20 mg/kg q24h (Moderate renal impairment)"
    else:
        vanco = "Dose based on TDM levels (Severe impairment)"

    # Rivaroxaban (AFib dosing reference)
    if crcl > 50:
        riva = "20 mg once daily with evening meal"
    elif 15 <= crcl <= 50:
        riva = "15 mg once daily with evening meal"
    else:
        riva = "Avoid use or use with extreme caution (CrCl < 15)"

    # Enoxaparin (Treatment dosing reference)
    if crcl >= 30:
        enoxa = "1 mg/kg every 12 hours OR 1.5 mg/kg once daily"
    else:
        enoxa = "1 mg/kg once daily (Severe renal impairment)"

    return {
        "Vancomycin": vanco,
        "Rivaroxaban": riva,
        "Enoxaparin": enoxa
    }

def calculate_clinical_support(gender, age, weight_kg, height_cm, scr):
    if scr <= 0 or age <= 0 or height_cm <= 0 or weight_kg <= 0:
        return "خطأ: جميع المدخلات الرقمية يجب أن تكون أكبر من الصفر."

    gender_code = 'male' if gender == "ذكر (Male)" else 'female'
    ibw = calculate_ibw(gender_code, height_cm)
    bsa = calculate_bsa(height_cm, weight_kg)
    
    if weight_kg < ibw:
        selected_weight = weight_kg
        weight_type = "Actual Body Weight (Underweight)"
    elif weight_kg > (1.2 * ibw):
        selected_weight = calculate_abw(weight_kg, ibw)
        weight_type = "Adjusted Body Weight (Obesity)"
    else:
        selected_weight = ibw
        weight_type = "Ideal Body Weight (Normal range)"

    crcl_base = ((140 - age) * selected_weight) / (72 * scr)
    crcl_final = crcl_base * 0.85 if gender_code == 'female' else crcl_base
    
    drug_recommendations = get_drug_dosing(crcl_final)

    res = {
        "CrCl (mL/min)": round(crcl_final, 2),
        "IBW (kg)": round(ibw, 2),
        "BSA (m²)": round(bsa, 2),
        "Weight Used Type": weight_type,
        "Weight Used (kg)": round(selected_weight, 2),
        "Clinical Dosing Guidance": drug_recommendations
    }
    return json.dumps(res, indent=4, ensure_ascii=False)

# 3. بناء الواجهة
interface = gr.Interface(
    fn=calculate_clinical_support,
    inputs=[
        gr.Radio(["ذكر (Male)", "أنثى (Female)"], label="الجنس (Gender)", value="ذكر (Male)"),
        gr.Number(label="العمر (Age - years)", value=66),
        gr.Number(label="الوزن (Weight - kg)", value=80),
        gr.Number(label="الطول (Height - cm)", value=160),
        gr.Number(label="سيروم كرياتينين (SCr - mg/dL)", value=1.4)
    ],
    outputs=gr.Textbox(label="مخرجات التقييم وتوصيات الأدوية السريرية", lines=15),
    title="🧪 Multi-Drug Clinical Calculator (v1.3)",
    description="أداة دعم القرار السريري لحساب الكرياتينين وضبط جرعات الفانكومايسين، الريفاروكسابان، والإنوكسابارين."
)

interface.launch(share=True)
