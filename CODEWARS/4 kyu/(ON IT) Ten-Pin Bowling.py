# https://www.bowlinggenius.com/

def bowling_score(frames: str):
    frames_list = frames.split()

    total = 0
    bonus1 = False
    bonus2 = False
    double_bonus = False

    for index, frame in enumerate(frames_list):

        if frame.isnumeric():  # 62
            total += sum(int(j) for j in frame)

        elif index == "X":
            total += 10
        elif index == "XXX":
            total += 30


bowling_score("11 11 11 11 11 11 11 11 11 11")
