weight = float(input("Enter weight in lbs.: "))
feet = float( input("Enter height in feet: "))
inches = float( input("Enter height in inches: "))

heightininches = 12*feet + inches;
BMI = (weight*703) / (heightininches * heightininches)

print ("BMI=%.2f" % BMI)
