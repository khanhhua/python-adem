from time import localtime

zeit = localtime()
stunde = zeit.tm_hour

print(stunde)