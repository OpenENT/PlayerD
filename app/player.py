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

    def go_at(self, seconds: int):
        pass
    
    def get_status(self): # {"paused": false, "duration": "60", "position": "30", "name": "song", "url": "url"}
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
            "name": self.player.media_title, 
            "url": self.player.filename
        }