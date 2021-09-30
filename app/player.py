from mpv import MPV

class Player:

    def __init__(self):
        pass

    def play(self, url: str):
        pass

    def resume(self):
        pass

    def pause(self):
        pass

    def close(self):
        pass

    def set_volume(self, volume: int):
        pass

    def go_at(self, seconds: int):
        pass
    
    def get_status(self): # {"paused": false, "duration": "60", "position": "30", "volume": 30, "name": "song", "url": "url"}
        pass

    def playlist_append(self, url: str):
        pass

    def playlist_remove(self, index: int):
        pass

    def playlist_clear(self):
        pass

    def playlist_go(self, index: int):
        pass


class MPVPlayer(Player):

    def __init__(self):
        self.player = MPV(video=False)
        
    def play(self, url: str):
        self.player.play(url)
    
    def resume(self):
        self.player.pause = False

    def pause(self):
        self.player.pause = True

    def close(self):
        self.player.stop()

    def set_volume(self, volume: int):
        self.player.volume = volume

    def go_at(self, seconds: int):
        self.player.time_pos = seconds

    def get_status(self):
        if self.player.time_pos is None:
            return {"playing": False}
        return {
            "playing": True, 
            "paused": self.player.pause, 
            "duration": self.player.duration, 
            "position": self.player.time_pos, 
            "volume": self.player.volume,
            "name": self.player.media_title, 
            "url": self.player.filename
        }

    def playlist_append(self, url: str):
        self.player.playlist_append(url)

    def playlist_remove(self, index: int):
        self.player.playlist_remove(index)

    def playlist_clear(self):
        self.player.stop()
        self.player.playlist_clear()

    def playlist_go(self, index: int):
        self.player.playlist_pos = index
