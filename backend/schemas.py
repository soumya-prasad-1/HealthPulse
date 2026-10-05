from pydantic import BaseModel


class HealthData(BaseModel):

    age: float
    gender: int
    height: float
    weight: float
    ap_hi: float
    ap_lo: float
    cholesterol: int
    gluc: int
    smoke: int
    alco: int
    active: int
    bmi: float


class WHORiskData(BaseModel):

    age: int
    sex: str
    smoking: bool
    systolic_bp: float
    total_cholesterol: float
    diabetes: bool