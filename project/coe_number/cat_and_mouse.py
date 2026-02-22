def cat_and_mouse(x: int, y: int, z: int) -> str:
    # หาระยะห่างของแมว A และ B จากหนู C
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    
    # เปรียบเทียบระยะห่าง
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"