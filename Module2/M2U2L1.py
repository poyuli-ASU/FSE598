def main():
    str1 = "Arizona State University";
    str2 = "in Tempe, Arizona";
    str3 = str2.replace("Tempe", "Phoenix Downtown");
    # substitute Phoenix Downtown for Tempe
    str4 = str3.upper();
    str5 = "-".join(str2);
    str6 = "".join(reversed(str2))
    str7 = str1.split(' ')
    print(F'str1 = {str1}')
    print(F'str2 = {str2}')
    print(F'str3 = {str3}')
    print(F'str4 = {str4}')
    print(F'str5 = {str5}')
    print(F'str6 = {str6}')
    print(F'str7 = {str7}')
    name = input("Please enter your name:") # input() 回傳的值是字串
    print("Hello " + name + ", welcome to Python programming!")
if __name__ == "__main__":
    main()