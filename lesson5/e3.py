symptoms = {
    'fever': ['flu', 'malaria', 'COVID-19', 'pneumonia'],
    'cough': ['flu', 'COVID-19', 'cold', 'pneumonia', 'bronchitis', 'sinusitis'],
    'headache': ['malaria', 'migraine', 'sinusitis', 'tension headache'],
    'sore throat': ['flu', 'cold', 'bronchitis'],
    'body aches': ['flu'],
    'fatigue': ['flu', 'COVID-19', 'pneumonia', 'bronchitis', 'sinusitis', 'urinary tract infection', 'allergic rhinitis'],
    'chills': ['malaria'],
    'nausea': ['malaria', 'migraine', 'gastroenteritis'],
    'vomiting': ['malaria', 'migraine', 'gastroenteritis'],
    'shortness of breath': ['COVID-19'],
    'loss of taste or smell': ['COVID-19'],
    'chest pain': ['pneumonia'],
    'sneezing': ['cold'],
    'runny nose': ['cold'],
    'mild fever': ['cold'],
    'chest discomfort': ['bronchitis'],
    'sensitivity to light': ['migraine', 'tension headache'],
    'throbbing pain': ['migraine'],
    'facial pain or pressure': ['sinusitis'],
    'nasal congestion': ['sinusitis'],
    'dull, aching head pain': ['tension headache'],
    'tightness or pressure around the forehead or back of the head': ['tension headache'],
    'neck pain': ['tension headache'],
    'sensitivity to light or noise': ['tension headache'],
    'diarrhea': ['gastroenteritis'],
    'abdominal pain': ['gastroenteritis', 'urinary tract infection'],
    'dehydration': ['gastroenteritis'],
    'frequent urination': ['urinary tract infection'],
    'painful urination': ['urinary tract infection'],
    'cloudy or bloody urine': ['urinary tract infection'],
    'runny or stuffy nose': ['allergic rhinitis'],
    'itchy or watery eyes': ['allergic rhinitis'],
    'itchy throat or ears': ['allergic rhinitis'],
    'user_symptomps': []
}


print(symptoms.keys)
user_symptomps = []

enter_symptoms = input("Enter your symptoms (comma-separated): ")
symptoms_mentioned = enter_symptoms.split(', ')

# G baik (ga kohesi dalam dictionarynya) pada akhrinya nyulitin diri sendiri
user_symptomps = symptoms_mentioned

## 1. Dia dapat input dari user: fever, nausea (enter_symptomps)
## 2. "fever, nausea" ->  ['fever', 'nausea']   (symptoms_mentioned) (LIST)
## 3. ['fever', 'nausea'] -> ['malaria', 'migraine', 'gastroenteritis'] (result) (LIST)
def diagnose_patient():
    for symtoms_mentioned in symptoms:
        if symptoms_mentioned == symptoms.keys:
            result = print(symptoms_mentioned.values)
        return result

print(diagnose_patient)
# diagnose_patient()
#
## 
# 1. Scope
# 2. Kamu langsung koding dan ga liat itu programnya ngapain. Naikkan curiousity.
# 3. function [parameters]
# 4. I/O

##
#
# 1. Latihan how to explain
# 2. Formulate problem (Identify the problem)
# 3. Mindset: Why? How? What?  | Ngapain kita ini? Gimana sih buat ngelakuinnya? Ngodingnya gimana?
#   => Kerasa beda orang yg lulusan Gundar vs Lulusan UI , ITB # pola pikir / problem
#   --> Bina nusantara  | ngehambat orang maju 
#  Susah berkembang. Starts With Why?
# 4. Latian 1 soal di leet code? per hari? (luangan 30 menit). 
#
##
