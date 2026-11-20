def solve():
    violator_songs_list = [
        ['World in My Eyes', 4.86], ['Sweetest Perfection', 4.43],
        ['Personal Jesus', 4.56], ['Halo', 4.9],
        ['Waiting for the Night', 6.07], ['Enjoy the Silence', 4.20],
        ['Policy of Truth', 4.76], ['Blue Dress', 4.29], ['Clean', 5.83],
    ]
    
    songs_to_find = ['Halo', 'Enjoy the Silence', 'Clean']
    total_time = sum(song[1] for song in violator_songs_list if song[0] in songs_to_find)
    print(f"Три песни звучат {round(total_time, 3)} минут")
    
    violator_songs_dict = {
        'World in My Eyes': 4.76, 'Sweetest Perfection': 4.43,
        'Personal Jesus': 4.56, 'Halo': 4.30,
        'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6,
        'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68,
    }
    
    songs_dict_find = ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']
    total_time_dict = sum(violator_songs_dict[song] for song in songs_dict_find)
    print(f"А другие три песни звучат {round(total_time_dict, 3)} минут")

if __name__ == "__main__":
    solve()