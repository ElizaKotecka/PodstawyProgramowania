try:
    with open("int_powers.txt", "w") as file:
        for i in range(1, 101):
            second_power = i ** 2
            third_power = i ** 3
            
            result = f"{i},{second_power},{third_power}\n"
            file.write(result)

except Exception as e:
    print(f"An error occurred: {e}")