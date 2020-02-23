import tweet_api

def test():
    assert tweet_api.createImg("test1","./test/img1.jpg") == "Success"
    
    assert tweet_api.createImg("test2","./test/img2.jpg") == "Success"
    
if __name__ == '__main__':
    test()
