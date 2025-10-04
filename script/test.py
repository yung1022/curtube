# This is an example of how the system works.
from modules import curtubemodule
issuccess = curtubemodule.signin('0', 'ASSHELL', 'ASS')
if issuccess == 1:
    print('successfully created account')
# the command below is not reworked yet.
#
# curtubemodule.login('ASSHELL', 'ASS')
# curtubemodule.getalluser()
# curtubemodule.upload('video', 'HELLO')
# curtubemodule.getallvid(0)
