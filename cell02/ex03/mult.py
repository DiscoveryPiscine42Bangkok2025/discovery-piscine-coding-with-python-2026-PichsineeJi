firstN = int(input("Enter the first number:\n"))
secN = int(input("Enter the second number:\n"))
result = firstN*secN

print(f"{firstN} x {secN} = {result}")

if result > 0:
    print("This result is positive.")
elif result < 0:
    print("This result is negative.")
else:
    print("This result is positive and negative.")