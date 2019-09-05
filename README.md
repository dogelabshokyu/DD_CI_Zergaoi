최은기
class MyError(Exception):
    def __str__(self):
        return("허용되지 않는 별명입니다.")
    
def say_nick(nick):
    if nick == "fool":
        raise MyError()
    print(nick)

try :
    say_nick("nick")
    say_nick("fool")
except MyError as e :
    print(e)
