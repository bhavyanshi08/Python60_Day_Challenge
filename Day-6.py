from unicodedata import category

n=int(input("Enter the number of songs: "))
songs=[0]*n
for i in range(n):
    songs[i]=int(input())
invalid= False
for d in songs:
    if d<=0:
        Invalid = True
        break
if invalid:
    print("Invalid Playlist")
else:
    total_duration=sum(songs)
    number_of_songs=len(songs)
    duplicate= False
    for j in range(len(songs)):
        if songs.count(songs[j])>1:
            duplicate= True
            break
    if total_duration<300:
        category= "Too Short Playlist"
        recommendation="Add more songs"
    elif total_duration>3600:
        category="Too Long Playlist"
        recommendation="Consider shortening the Playlist"
    elif duplicate:
        category="Repetitive Playlist"
        recommendation="Add some Variety"
    elif(max(songs)-min(songs))<=300:
        category="Balanced Playlist"
        recommendation="good listening Session"
    else:
        category="Irregular Playlist"
        recommendation="Adjust song selection"
    print("Total duration: ",total_duration)
    print("Number of Songs:",number_of_songs)
    print("Category: ",category)
    print("Recommendations: ",recommendation)



