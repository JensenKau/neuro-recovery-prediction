from __future__ import annotations

from src.patientdata.data_enum import PatientOutcome, PatientSex

class PatientMetaData:
    def __init__(self, patient_id: int, hospital: str, age: int, sex: PatientSex, rosc: float, ohca: bool, shockable_rhythm: bool, ttm: int, outcome: PatientOutcome, cpc: int) -> None:
        self.patient_id = patient_id
        self.hospital = hospital
        self.age = age
        self.sex = sex
        self.rosc = rosc
        self.ohca = ohca
        self.shockable_rhythm = shockable_rhythm
        self.ttm = ttm
        self.outcome = outcome
        self.cpc = cpc
    
    
    @classmethod
    def load_patient_meta_data(cls, filename: str) -> PatientMetaData:
        output = {
            "Outcome": PatientOutcome.NONE,
            "CPC": None
        }
        parsers = {
            "Patient": lambda x: int(x),
            "Hospital": lambda x: x,
            "Age": lambda x: float(x),
            "Sex": lambda x: PatientSex.NONE if x.lower() == "nan" else (PatientSex.MALE if x.lower() == "male" else PatientSex.FEMALE),
            "ROSC": lambda x: float(x),
            "OHCA": lambda x: float(x) if x.lower() == "nan" else x.lower() == "true",
            "Shockable Rhythm": lambda x: float(x) if x.lower() == "nan" else x.lower() == "true",
            "TTM": lambda x: float(x),
            "Outcome": lambda x: PatientOutcome.NONE if x.lower() == "nan" else (PatientOutcome.GOOD if x.lower() == "good" else PatientOutcome.POOR),
            "CPC": lambda x: int(x)
        }
        
        with open(filename, "r", encoding="utf-8") as file:            
            for line in file.read().strip().split("\n"):
                line = line.split(": ")
                output[line[0]] = parsers[line[0]](line[1])
        
        return PatientMetaData(
            patient_id=output["Patient"],
            hospital=output["Hospital"],
            age=output["Age"],
            sex=output["Sex"],
            rosc=output["ROSC"],
            ohca=output["OHCA"],
            shockable_rhythm=output["Shockable Rhythm"],
            ttm=output["TTM"],
            outcome=output["Outcome"],
            cpc=output["CPC"]
        )


    def get_patient_id(self) -> int:
        return self.patient_id

    
    def get_hospital(self) -> str:
        return self.hospital

    
    def get_age(self) -> int:
        return self.age

    
    def get_sex(self) -> PatientSex:
        return self.sex

    
    def get_rosc(self) -> float:
        return self.rosc

    
    def get_ohca(self) -> bool:
        return self.ohca

    
    def get_shockable_rhythm(self) -> bool:
        return self.shockable_rhythm

    
    def get_ttm(self) -> int:
        return self.ttm

    
    def get_outcome(self) -> PatientOutcome:
        return self.outcome

    
    def get_cpc(self) -> int:
        return self.cpc




if __name__ == "__main__":
    pass