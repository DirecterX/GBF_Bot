import threading
import time


def threat_1(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        print ("working on %s" % arg)
        time.sleep(0.5)
    print("Stopping as you wish.")

def threat_2(thread_resume):
    for i in range(5):
        print("\nTask 2 working "+str(i))

    thread_resume.do_run = True

def main():
    t = threading.Thread(target=threat_1, args=("task1",))
    t2 = threading.Thread(target=threat_2 ,  args=(t,))

    t.start()

    t.sleep
    time.sleep(0.2)
    t2.start()
    t2.join()
    
    
    
if __name__ == "__main__":
    main()