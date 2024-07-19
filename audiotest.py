import vlc
import time

def play_radio(url):
    # Create an instance of the VLC player with ALSA audio output
    instance = vlc.Instance('--aout=alsa', '-vvv')
    player = instance.media_player_new()
    
    # Set the media (radio stream URL)
    media = instance.media_new(url)
    player.set_media(media)
    
    # Play the media
    player.play()
    
    # Keep the script running while the media is playing
    try:
        while True:
            state = player.get_state()
            if state == vlc.State.Ended or state == vlc.State.Error:
                print("Playback ended or encountered an error.")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping radio playback.")
        player.stop()

if __name__ == "__main__":
    # Example URL of a radio stream that uses HTTP
    radio_url = "http://stream.zenolive.com/g0wsfbbaft5tv"
    play_radio(radio_url)
