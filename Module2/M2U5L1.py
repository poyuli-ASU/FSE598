def main():
    fileName = "MyFile.txt" # Pointer
    fileBuf = None
    try:
        fileBuf = open(fileName, "w") 
        s = "The first string into file\n"
        fileBuf.write(s)
        s = "The second string into file\n"
        fileBuf.write(s)
        print("After writing the file:",s)
        fileBuf.close()

        fileBuf = open(fileName, "r")
        r = fileBuf.readline()
        print("First reading the file:",r)
        r = fileBuf.readline()
        print("Second reading the file:",r)
        fileBuf.close()
        
    except FileNotFoundError:
        print(f"File {fileName} not found.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if fileBuf:
            fileBuf.close()
if __name__ == "__main__":
    main()
