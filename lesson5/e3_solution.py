

"""
PR chel2

Certainly! Here's a programming exercise related to a doctor:

Exercise: Patient Diagnosis

Description:
Create a program that simulates a doctor diagnosing patients based on their symptoms. The program should take input from the user regarding their symptoms and provide a possible diagnosis.

Instructions:
1. Create a dictionary called `symptoms` that maps symptoms to possible diagnoses. Each symptom should be a key, and the value should be a list of possible diagnoses associated with that symptom.
   Example:
   ```python
   symptoms = {
       'fever': ['flu', 'malaria', 'COVID-19'],
       'cough': ['cold', 'pneumonia', 'bronchitis'],
       'headache': ['migraine', 'sinusitis', 'tension headache'],
       # Add more depends on the symptomps.json
   }
   ```

2. Prompt the user to enter their symptoms. They can enter multiple symptoms, separated by commas.
   Example:
   ```
   Enter your symptoms (comma-separated): fever, cough
   ```

3. Split the user input into individual symptoms and store them in a list called `user_symptoms`.

4. Implement a function called `diagnose_patient()` that takes `user_symptoms` as a parameter and returns the possible diagnoses based on the symptoms. Inside the function, iterate through `user_symptoms` and check each symptom in the `symptoms` dictionary. If a symptom is found, add the corresponding diagnoses to a list called `possible_diagnoses`.


5. Print the possible diagnoses to the user.

Example Output:
```
Enter your symptoms (comma-separated): fever, cough

Possible Diagnoses:
- flu
- malaria
- COVID-19
- cold
- pneumonia
- bronchitis
```

Happy coding!

Bikin file namanya symptomps.json yah trus copy paste ini::


```
{
 "fever": ["Flu", "Malaria"]
 "cough": ["Flu", "COVID-19"]
}

## 2 Case
1. BLOM ADA KEYNYA: BIKIN + INITIATE VALUE (LIST)
2. KLO ADA KEYNYA: TAMBAHIN DISEASE/DIAGNOSIS KE VALUE YG DIRUJUK OLEH KEY

{
  "Flu": ["fever", "cough", "sore throat", "body aches", "fatigue"],
  "Malaria": ["fever", "chills", "headache", "nausea", "vomiting"],
  "COVID-19": ["fever", "cough", "shortness of breath", "loss of taste or smell", "fatigue"],
  "Common Cold": ["sneezing", "runny nose", "sore throat", "cough", "mild fever"],
  "Pneumonia": ["cough", "fever", "shortness of breath", "chest pain", "fatigue"],
  "Bronchitis": ["cough", "sore throat", "fatigue", "shortness of breath", "chest discomfort"],
  "Migraine": ["headache", "nausea", "vomiting", "sensitivity to light", "throbbing pain"],
  "Sinusitis": ["facial pain or pressure", "nasal congestion", "headache", "cough", "fatigue"],
  "Tension Headache": ["dull, aching head pain", "tightness or pressure around the forehead or back of the head", "neck pain", "sensitivity to light or noise"],
  "Gastroenteritis": ["nausea", "vomiting", "diarrhea", "abdominal pain", "dehydration"],
  "Urinary Tract Infection": ["frequent urination", "painful urination", "cloudy or bloody urine", "abdominal pain", "fatigue"],
  "Allergic Rhinitis": ["sneezing", "runny or stuffy nose", "itchy or watery eyes", "itchy throat or ears", "fatigue"]
}

{
    "fever": ["Flu", "Malaria"],
    "cough": ["Flu"],
    "sore throat": ["Flu"],
    "body aches": ["Flu"],
    "fatigue": ["Flu"],
    "chills": ["Malaria"],
}
```

Baca filenya trus ubah jadi bentuk kyk diatas

"""

"""

1. Ngertiin dulu apa yang diminta, Validasi 
2. Step by step (general)
"""

"""
inp_user (symptomps) -> output (diagnose_patient) -> print (possible_diagnoses)
"""

# file json
# PACKAGE JSON

# kodingan2 yang kita install di python, trus kita pake
import json  
from pprint import pprint

with open("symptomps.json", "r") as f:
    symptomps_from_json = json.load(f)

# TODO: CREATE SYMPTOMPS DICTIONARY DONE HOREEE

transformed_symptomps = {} # initialize empty dict
# TODO: Reverse the symptomps_from_json into symptomps D

# Tuple : ("Archel", 18)  # immutable (ga bisa diubah)
# List: ["Archel", 18]  # mutable (bisa diubah)

# symptomps_from_json returns a list of tuples (diagnosis, symptomps[list])
# print(symptomps_from_json.items())
# print(list(symptomps_from_json.items())[0])



for diagnosis, symptomps in symptomps_from_json.items():
    # symptomps_from_json ("Flu", ["fever", "cough", "sore throat", "body aches", "fatigue"])
    # diagnosis: "Flu"
    # symptomps: ["fever", "cough", "sore throat", "body aches", "fatigue"],
    """
    
    # KITA MAU APA?
    ## REVERSE
    ### 1. symptomps: key, diagnosis: value [] ## CARANYA GIMANA
    ### 2. Loop symptomps , setiap instance we ??? "fever" -> DIJADIIN KEY,  
    ##
    transformed_symptomps = {
        "fever": ["Flu"],
        "cough": ["Flu"]
    }

    'fever': ['Pneumonia'],
    """
    # for i in range(5):

    # for i in [0,1,2,3,4]
    #    i = 0
    # 
    for symptomp in symptomps:
        # Case 1: if key blom ada
        if symptomp not in transformed_symptomps:
            transformed_symptomps[symptomp] = [diagnosis]
        else:
            # Case 2: kalau key symptompnya ada
            transformed_symptomps[symptomp].append(diagnosis)
    
# pprint(transformed_symptomps)

# TODO: PROMPT USER AND SPLIT ITS INPUT

prompt_user = input("Enter your symptoms (comma-separated): ")
# prompt_user = "fever, nausea"
splitted_symptomps_user: list[str] = prompt_user.split(",")
print()   # as a line break for a space

# Need to handle space before the user's input

# TODO: CREATE FUNCTION DIAGNOSE_PATIENT

# example_user_input: fever, nausea
# output: ['Flu', 'Malaria', 'COVID-19', 'Pneumonia', 'Malaria', 'Migraine', 'Gastroenteritis']  # Need to handle double output
# output: ['Flu', 'Malaria', 'COVID-19', 'Pneumonia', 'Migraine', 'Gastroenteritis']

# splitted_prompt_user: fever, nausea
# transformed_symptomps: {key: symptomp -> value: disease}


def diagnose_patient(user_symptoms):

    collected_diagnosis = []

    for user_symptomp in user_symptoms:
        # print(user_symptomp)
        # Now the trailing space is handled!!!
        handled_user_symptomp = user_symptomp.strip() # " sore throat  " -> "sore throat"

        # take list of diagnosis from the symptomp
        symptomp_diagnosises = transformed_symptomps[handled_user_symptomp]
        # e.g.: ['Malaria', 'Migraine', 'Gastroenteritis']

        # Extract the diagnosis 
        # DEBUG / CHECK
        for diagnosis in symptomp_diagnosises:
            # Need to handle duplicate output
            if diagnosis not in collected_diagnosis:
                collected_diagnosis.append(diagnosis)
    return collected_diagnosis

# a = [1,44,5] -> a[1] -> 44
# a = {'a': 1, "b": 44, "c": 5} -> a['c'] -> 5
# TODO: PRINT THE POSSIBLE DIAGNOSES TO THE USER

diagnose_results = diagnose_patient(splitted_symptomps_user)
print("Possible Diagnoses:")
for i, result in enumerate(diagnose_results):
    print(f"- {result}", end="")
    if i != len(diagnose_results) - 1:
        print("\n", end="")

"""
Possible Diagnoses:
- flu
- malaria
- COVID-19
- cold
- pneumonia
- bronchitis
"""


## MISC


# None = Kosong 
# num_person = 10
# print(num_person)
# num_person = 2423
# print(num_person)

# 2 Mesin pembuat minuman 1. ngasilin botol berisi minuman (NGOCOK AIR, NGASIH HASIL KOCOKAN KE KITA) | 2. dia ternya rusak (ngocok2 air, DIA GA NGASIH HASIL KOCOKAN KE KITA) ga ngeluarin apa
# Ada return: Restoran
#   -> restoran bel buat panggil pelayan | PENCET BEL pencet_bel() -> pelayan
# Pelayannya proses pesanan kita, terus pelayannya mencet_bel_chef(bikin_pesanan) CHEF NYA BANDEL, DIMAKAN SENDIRI
## -> mencet_bel_chef(bikin_pesanan) -> masak, chef_makan_sendiri, trus_ga_balikin_makanannya
#   -> Pencet
#   -> 

# def mesin_pembuat_minuman():
#    

# mesin_pembuat_minuman()

# print("INI TIDAK JELAS", type(new_function_2()), new_function_2())

# new_function(3)  # 6
# new_function(i) =  i * 2
# new_function(3) = 6

# print() | Dia nerima argumen | ga ngeluarin output / return
# print() # function

# print(var_print)
# print("ayam")

# for diagnosis, symptoms in symptomps_from_json.items():
#     for symptom in symptoms:
#         if symptom not in symptomps:
#             symptomps[symptom] = [diagnosis]
#         else:
#             symptomps[symptom].append(diagnosis)
