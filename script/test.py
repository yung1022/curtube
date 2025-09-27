# This is an example of how the system works.
from pyscript import display
from modules import curtubemodule
issuccess = curtubemodule.signin('ASSHELL', 'ASS')
if issuccess == 1:
    print('successfully created account')
curtubemodule.login('ASSHELL', 'ASS')
curtubemodule.getalluser()
curtubemodule.upload('video', 'HELLO')
display(curtubemodule.getallvid(0))
