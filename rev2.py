from rev import School
s1=School("Mercy","8899")
s2=School("Jaon","9998")
s3=School("KRIS","0099")

print(School.number_students)
print(s1.name)
print(s2.id)
print(s1.calculate_fees("One thousand"))
print(s1.calculate_fees(1000))
print(s1.calculate_fees(90))
print(s1.calculate_fees(90000))
