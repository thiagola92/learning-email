from smtplib import SMTP

client = SMTP("localhost", 8025)
client.sendmail(
    "from@example.com",
    ["to@example.com"],
    """\
From: MyName <from@example.com>
To: MyFriend <to@example.com>
Subject: Hiiiii
Message-ID: <ant>

Hi friend!
""",
)
