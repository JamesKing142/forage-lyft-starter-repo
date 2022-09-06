from datetime import date

def add_year_to_date(original_date, years_to_add):
    result = original_date.replace(year = original_date.year + years_to_add)
    return result

def get_current_date():
    return date.today()