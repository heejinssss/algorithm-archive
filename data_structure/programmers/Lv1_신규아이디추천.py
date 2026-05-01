def solution(new_id):

    avl = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v", "w","x","y","z",
           "1","2","3","4","5","6","7","8","9","0",
           "_","-","."]

    # 1단계
    new_id = new_id.lower()

    # 2단계
    rlt = ""
    for i in range(len(new_id)):
        # if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
        rlt = rlt + new_id[i] if new_id[i] in avl else rlt

    # 3단계
    while ".." in rlt:
        rlt = rlt.replace("..", ".")

    # 4단계
    rlt = rlt.rstrip(".") if rlt and rlt[-1] == "." else rlt

    # 4단계
    rlt = rlt.lstrip(".") if rlt and rlt[0] == "." else rlt

    # 5단계
    rlt = rlt if rlt else "a"

    # 6단계
    if (len(rlt) >= 16):
        rlt = rlt[:15]
        if (rlt[-1] == "."):
            rlt = rlt[:14]

    # 7단계
    if (len(rlt) <= 2):
        last_word = rlt[-1]
        while (len(rlt) < 3):
            rlt += last_word

    # ASCII
    # a~z : 97~122
    # 0~9 : 48~57
    # - : 45
    # . : 46
    # _ : 95

    return rlt
