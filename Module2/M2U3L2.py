def main():
    print("遞歸函式範例-Recursion")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def hanoi(n, source, target, temp):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
    else:
        hanoi(n-1, source, temp, target)
        print(f"Move disk {n} from {source} to {target}")
        hanoi(n-1, temp, target, source)

if __name__ == "__main__":
    main()
    print("5!=",factorial(5))
    print("Fibonacci(5)=", fibonacci(5))
    hanoi(3, "A", "C", "B")