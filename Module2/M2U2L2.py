def main():
    myTup1 = (0,1,20,3,51,7,9,20)
    myTup2 = ("b","c","b","p","t")
    myTup3 = (1,2,3,"bike","car","train")
    #print(myTup1[0],"1'st element in myTup1")
    print(myTup1[2:6],"elements 2 to 5 in myTup1") # 2-6包含2不包含6
    print(myTup1[:-3],"counting from the back myTup1") # -3是倒數第3個元素，也不算
    

if __name__ == "__main__":
    main()