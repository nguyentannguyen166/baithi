def totalDigitsOfNumber(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
n = 9;
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n));