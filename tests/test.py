import curtubemodule
issuccess = curtubemodule.signin('CurtisPlaysYT', 'abc123')
if issuccess == 1:
    print('successfully created account')
curtubemodule.login('CurtisPlays', 'abc123')
curtubemodule.getalluser()
