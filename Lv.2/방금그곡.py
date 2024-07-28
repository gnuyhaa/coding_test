def replace_code(s):
    s = s.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    return s

def solution(m, musicinfos):
    m = replace_code(m)    
    music = dict()
    musicTime = dict()
    for info in musicinfos:
        info = list(info.split(','))
        startT = list(info[0].split(':'))
        endT = list(info[1].split(':'))
        startMusic = min(int(startT[0])*60+int(startT[1]), int(endT[0])*60+int(endT[1]))
        endMusic = max(int(startT[0])*60+int(startT[1]), int(endT[0])*60+int(endT[1]))
        time = endMusic - startMusic
        musicTime[info[2]] = time # 음악 재생 시간
        info[3] = replace_code(info[3])
        lyrics = info[3]
        if len(lyrics) > time: 
            lyrics = lyrics[0:time]
        elif len(lyrics) < time:
            while len(lyrics) < time:
                lyrics += info[3]
        music[info[2]] = lyrics # 음악 가사 길이
    
    listenedMusic = list() # Idx0: 조건이 일치하는 음악 제목, Idx1: 재생 시간
    for title, lyrics in music.items():
        if m in lyrics:
            listenedMusic.append([title, musicTime[title]])
    
    if len(listenedMusic) == 0:
        return "(None)"
    
    listenedMusic.sort(key=lambda x:x[1], reverse=True)    
    return listenedMusic[0][0]
