def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
def main():
    a = []
    try:
        number = int(input("How many numbers?: "))
        for i in range(number):
            value = int(input("Give index [%d] number : " %i))
            a.append(value)
        print("Sorted list: ", bubble_sort(a))
    except Exception:
        print("Not a number!")

if __name__ == "__main__":
    main()