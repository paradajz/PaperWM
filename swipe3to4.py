#original author: icedman
#taken/reworked from https://github.com/icedman/gnome-shell-hammer

f=open("/usr/lib64/gnome-shell/libgnome-shell.so","rb")
s=f.read()
f.close()

str=b'GESTURE_FINGER_COUNT\x20=\x203'

if (s.find(str) != -1):
    s=s.replace(str,b'GESTURE_FINGER_COUNT\x20=\x204')

    f=open("libgnome-shell-replaced.so","wb")
    f.write(s)
    f.close()