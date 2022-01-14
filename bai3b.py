def isThuanNghich(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;
n = 636;
print("Tổng các chữ số của", n, "là", isThuanNghich(n));
