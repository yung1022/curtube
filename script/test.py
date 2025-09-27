# This is an example of how the system works.

import curtubemodule
issuccess = curtubemodule.signin('ASSHELL', 'ASS')
if issuccess == 1:
    print('successfully created account')
curtubemodule.login('ASSHELL', 'ASS')
curtubemodule.getalluser()
curtubemodule.upload('video', 'HELLO')
curtubemodule.getallvid(0)