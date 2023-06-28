import math
#savings
def savings(gross_pay, tax_rate, expenses):
    after_tax=int(gross_pay)-(int(gross_pay)*float(tax_rate))
    take_home=int(math.floor(after_tax))-int(expenses)
    take_home=int(take_home)

    if tax_rate >= 0 <= 1:
        print(f'your money (in centavos) after taxes and expenses {int(take_home)}')
    else:
        print("invalid tax rate")
    return int(take_home)

#material_waste
def material_waste(total_material, material_units, num_jobs, job_consumption):
    material_consumed=int(num_jobs) * int(job_consumption)
    waste=int(total_material)-int(material_consumed)
    waste=str(waste)+material_units

    print(waste)
    return waste

#interest
def interest(principal, rate, periods):
    simple_interest=int(principal)*(float(rate)*int(periods))
    final_value=int(principal)+int(simple_interest)
    final_value=int(math.floor(final_value))

    print(f'Final Value of the investment is {final_value}')
    return final_value

def body_mass_index(weight, height):
    weight = weight / 2.205
    height = (height[0] * 0.3048) + (height[1]*0.0254)
    bmi=weight / (height**2)

    print(f'your bmi {bmi}')
    return bmi

#tests
savings(956472,0.1,2000)
material_waste(100,"kg",10,9)
interest(10000,0.5,4)
body_mass_index(180,[5,6])