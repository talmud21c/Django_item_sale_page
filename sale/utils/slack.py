from slacker import Slacker


def slack_notify(text=None, channel='#test', username='알림봇', attachments=None):
    token = 'xoxb-1670192234467-3826473453813-IhgFO2npD2B87OTaCLiHspaN'
    slack = Slacker(token)
    slack.chat.post_message(
        text=text,
        channel=channel,
        username=username,
        attachments=attachments
    )