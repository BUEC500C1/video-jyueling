import img2video

def test():
    assert img2video.ffmpeg("@Discovery") == "Success"
    
    assert img2video.ffmpeg("@Twitter") == "Success"
    
if __name__ == '__main__':
    test()
