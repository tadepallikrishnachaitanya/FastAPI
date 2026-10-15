#module - BAL

def checker(income: float, age: int, employee_type: str) -> bool:
    return (income >= 50000) and (21 <= age < 45) and (employee_type == 'employee')