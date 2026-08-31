import math

def calculate_ibw(gender: str, height_cm: float) -> float:
    """حساب الوزن المثالي (IBW) باستخدام معادلة Devine."""
    height_inches = height_cm / 2.54
    over_60_inches = max(0.0, height_inches - 60)
    
    if gender.lower() in ['m', 'male', 'ذكر']:
        return 50.0 + (2.3 * over_60_inches)
    elif gender.lower() in ['f', 'female', 'أنثى', 'انثى']:
        return 45.5 + (2.3 * over_60_inches)
    else:
        raise ValueError("الجنس يجب أن يكون 'male' أو 'female'.")

def calculate_abw(actual_weight: float, ibw: float) -> float:
    """حساب الوزن المعدل (ABW) للحالات التي تعاني من السمنة."""
    return ibw + 0.4 * (actual_weight - ibw)

def calculate_bsa(height_cm: float, weight_kg: float) -> float:
    """حساب مساحة سطح الجسم (BSA) باستخدام معادلة Mosteller."""
    return math.sqrt((height_cm * weight_kg) / 3600)

def calculate_crcl(gender: str, age: int, weight_kg: float, height_cm: float, scr: float) -> dict:
    """
    حساب تصفية الكرياتينين (CrCl) مع التحديد التلقائي للوزن الأنسب.
    """
    if scr <= 0 or age <= 0 or height_cm <= 0 or weight_kg <= 0:
        raise ValueError("جميع المدخلات الرقمية يجب أن تكون أكبر من الصفر.")

    ibw = calculate_ibw(gender, height_cm)
    bsa = calculate_bsa(height_cm, weight_kg)
    
    # اختيار الوزن المناسب طبياً لحساب CrCl
    if weight_kg < ibw:
        selected_weight = weight_kg
        weight_type = "Actual Body Weight (Underweight)"
    elif weight_kg > (1.2 * ibw):
        selected_weight = calculate_abw(weight_kg, ibw)
        weight_type = "Adjusted Body Weight (Obesity)"
    else:
        selected_weight = ibw
        weight_type = "Ideal Body Weight (Normal range)"

    # معادلة Cockcroft-Gault
    crcl_base = ((140 - age) * selected_weight) / (72 * scr)
    
    if gender.lower() in ['f', 'female', 'أنثى', 'انثى']:
        crcl_final = crcl_base * 0.85
    else:
        crcl_final = crcl_base

    return {
        "CrCl_mL_min": round(crcl_final, 2),
        "IBW_kg": round(ibw, 2),
        "BSA_m2": round(bsa, 2),
        "Weight_Used_Type": weight_type,
        "Weight_Used_kg": round(selected_weight, 2)
    }

# مثال للتجربة المباشرة:
if __name__ == "__main__":
    # مريض ذكر، 65 سنة، وزنه 95 كجم، طوله 175 سم، الكرياتينين 1.4 mg/dL
    result = calculate_crcl(gender="male", age=65, weight_kg=95, height_cm=175, scr=1.4)
    print("--- نتائج الحاسبة السريرية v1.1 ---")
    for key, value in result.items():
        print(f"{key}: {value}")
