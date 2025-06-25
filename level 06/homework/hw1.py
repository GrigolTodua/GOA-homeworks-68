



#1 დავალება




#1 სახელი

#input() → ეს არის პითონის ბრძანება, რომლითაც პროგრამა ეკითხება ადამიანს რაღაცას.
name = input("enter your name: Grigoli")
#print() → ეს არის ბრძანება, რომლითაც პროგრამა აჩვენებს ან ბეჭდავს ეკრანზე რაღაცას.
print("name")

#2. ასაკი

age = input("how old are you? 14")
print("your age is:", age)

#3. ორი რიცხვის ჯამი
num1 = int(input(90))
num2 = int(input(20))
print(sum, num1 + num2)

#4. საყვარელი წიგნი
book = input ("your favorite book: 80000 კილომეტრი წყლალქვეშ")
print("i also like:", book)

#5. გამოყენება ფაილში (output ფაილში)
text = input("enter any sentence: i like apples")
with open("output.txt", "w") as file:
    file.write(text)
print("sentence was stored in a file: output.txt")




#2 დავალება




name = input("enter your name: Grigoli")
surname = input("enter your surname: Todua")
age = input("enter your age: 14")
address = input("enter your address: Tbilisi, Georgia")
hobby = input("enter your hobby: football")
fav_movie = input("enter your favorite movie: Bruce almighty")

print("hello,", name, surname + "!", "you are", age, "years old and live", address + "in", "your hobby is", hobby, "and your favorite movie is", fav_movie + ".")




#3 დავალება




number1 = int(input("enter first number: 10"))
number2 = int(input("enter second number: 15"))
number3 = int(input("enter third number: 20"))
number4 = int(input("enter fourth number: 25"))
number5 = int(input("enter fifth number: 30"))

average = (number1 + number2 + number3 + number4 + number5) / 5
print("entered number's average is:", average)




#4 დავალება





num1 = int(input("enter first number: 5"))
num2 = int(input("enter second: 2"))

print("sum:", num1 + num2)
print("difference:", num1 - num2)
print("product:", num1 * num2)
print("division:", num1 / num2)
print("mod:", num1 % num2)
print("upgrade:", num1 ** num2)

