def staircase(n, display='#'):
    if not (0 < n <= 30):
        return ""
    
    result = []
    for i in range(1, n + 1):
        # สร้างช่องว่างด้านหน้า แล้วตามด้วยตัวอักษร
        step = " " * (n - i) + display * i
        result.append(step)
        
    return "\n".join(result)