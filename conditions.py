'''
Description:
<A collection of functions for HW 3>
'''


def word_length(word, length):
    if len(word) > length:
        print("Longer than " + str(length) + " characters: " + word)
        
    elif len(word) < length:
        print("Shorter than " + str(length) + " characters: " + word)
        
    else:
        print("Exactly " + str(length) + " characters: " + word)

def stop_light(light_color, time):
    if light_color == "green" and time > 60:
        light_color = "yellow"
        return light_color
    elif light_color == "green" and time <= 60:
        light_color = "green"
        return light_color
    elif light_color == "yellow" and time > 5:
        light_color = "red"
        return light_color
    elif light_color == "yellow" and time <= 5:
        light_color = "yellow"
        return light_color
    elif light_color == "red" and time > 55:
        light_color = "green"
        return light_color
    else:
        light_color == "red"
        return light_color
    

def is_normal_blood_pressure(sbp, dbp):
    if sbp < 120 and dbp < 80:
        return True
    else:
        return False

def doctor():
    systolic_bp_reading = int(input("Enter your systolic reading: "))
    diastolic_bp_reading = int(input("Enter your diastolic reading: "))

    if systolic_bp_reading < 120 and diastolic_bp_reading < 80:
        print("Your blood pressure is normal.")
    else:
        print("Your blood pressure is high.")

def pants_size(waist_size):
    pant_size = ""
    if waist_size >= 34:
        pant_size = "large"
        return pant_size
    elif waist_size >= 30 and waist_size < 34:
        pant_size = "medium"
        return pant_size
    else:
        pant_size = "small"
        return pant_size

def pants_fitter():
    pants_cost = 0
    name = input("Enter your name: ")
    print("Greetings " + name + " welcome to Pants-R-Us")
    waist_size = input("Enter your waist size in inches: ")
    amount = input("How many pairs of pants would you like: ")
    pant_style = input("Would you like regular or fancy pants? ")
    if pant_style == "fancy":
        pants_cost = amount * 100
    else:
        pants_cost = amount * 40
    print(str(amount) + " pairs of " + pants_size(int(waist_size)) + " " + pant_style + " pants: $ " + str(pants_cost))
    

def digdug(number):
    for i in range(1, number + 1):
        if i % 5 == 0 and i % 3 == 0:
            print(str(i) + " : digdug")
        elif i % 5 == 0:
            print(str(i) + " : dug")
        elif i % 3 == 0:
            print(str(i) + " : dig")

def beef_type(percent_lean):
    if percent_lean < 78:
        percent_lean = "Hamburger"
        return percent_lean
    elif percent_lean >= 78 and percent_lean < 85:
        percent_lean = "Chuck"
        return percent_lean
    elif percent_lean >= 85 and percent_lean < 90:
        percent_lean = "Round"
        return percent_lean
    elif percent_lean >= 90 and percent_lean <= 95:
        percent_lean = 'Sirloin'
        return percent_lean
    else:
        percent_lean = 'Unknown'
        return percent_lean

def species_height(species, height):
    if species == "Human" and height == 67:
        print("Average")
    elif species == "Human" and height < 67:
        print("Below Average")
    elif species == "Human" and height > 67:
        print("Above Average")
    elif species == "Klingon" and height == 71:
        print("Average")
    elif species == "Klingon" and height < 71:
        print("Below Average")
    elif species == "Klingon" and height > 71:
        print("Above Average")

def sooner_date(month1, day1, month2, day2):
    if month1 < month2:
        print(str(month1) + " / " + str(day1))
    elif month2 < month1:
        print(str(month2) + " / " + str(day2))
    elif month1 == month2 and day1 < day2:
        print(str(month1) + " / " + str(day1))
    else:
        print(str(month2) + " / " + str(day2))
        
        
    



        

#==========================================================
def main():
    '''
    Write a description of what happens when you run
    this file here.
    '''
    word_length("boop", 8)
    stop_light('green', 61)
    is_normal_blood_pressure(120, 80)
    doctor()
    pants_size(38)
    pants_fitter()
    digdug(3)
    beef_type(91.2)
    species_height("Human", 62.1)
    sooner_date(1, 1, 2, 2)

    main()

if __name__ == '__main__':
    main()
