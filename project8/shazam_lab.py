import glob

def load_song_dataset_mp3(dataset_dir):
    song_names = glob.glob(dataset_dir + '*.mp3')
    n_songs = len(song_names)
    return n_songs, song_names

def load_song_dataset_wav(dataset_dir):
    song_names = glob.glob(dataset_dir + '*.wav')
    n_songs = len(song_names)
    return n_songs, song_names

# Example:
# import lab6
# n_songs, song_names = lab6.load_song_dataset_mp3('song_dataset/')
#
# Be sure to include the '/' at the end of your directory name.
# In this example, all of the songs are stored in a directory called
# 'song_dataset/'.
