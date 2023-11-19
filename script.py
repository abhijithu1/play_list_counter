import pytube,os
# Video playlist length calculator 


def func():
    playlist = input("Enter the link of the playlist : \n")

    def playlist_processing(url):
        pl = pytube.Playlist(url=url)
        count = str(pl.count)[33:-1]
        count = count.replace(']',"")
        count = count.replace("'","")
        pl_list = count.split(sep=",")
        return pl_list

    def time_calc(playlist):
        t = 0
        for vid in playlist:
            yt = pytube.YouTube(vid)
            t += yt.length
        raw_time = t
        minutes, seconds = divmod(raw_time, 60)
        hours, minutes = divmod(minutes, 60)
        minutes15, seconds15 = divmod(raw_time / 1.5, 60)
        hours15, minutes15 = divmod(minutes15, 60)
        return [hours, minutes, seconds, hours15, minutes15, seconds15]
	


    time = time_calc(playlist_processing(playlist))
    # print(f"{playlist_processing(playlist)} \n \n")
    print(f"Time original : \n\t {time[0]} hours ,{time[1]} minutes {time[2]} seconds\nTime in 1.5x is : \n\t {time[3]} hours {time[4]} minutes {time[5]} Seconds")

try:
    func()


except KeyError :
    print("Enter the correct link: \n")
    func()

input("{Enter to exit}")



