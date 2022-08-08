import datetime, time

def quando(momento):
    return time.mktime(momento.timetuple())

if __name__ == '__main__':
    quando()
