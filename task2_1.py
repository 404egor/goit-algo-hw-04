def total_salary(path):
    salaries = []

    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            employee, salary = line.split(",")
            salaries.append(float(salary))
    try:
        total = sum(salaries)
        average_salary = total/len(salaries)
    except ZeroDivisionError:
        print("Зарплат немає")

    return(total, average_salary)
    
total, average = total_salary(r"Text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")