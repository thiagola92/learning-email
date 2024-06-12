import os
from asyncio import events
from tempfile import TemporaryDirectory
from contextlib import ExitStack
from aiosmtpd.handlers import Mailbox
from aiosmtpd.controller import Controller

resources = ExitStack()
tempdir = resources.enter_context(TemporaryDirectory())
maildir_path = os.path.join(tempdir, "maildir")
mailbox = Controller(Mailbox(maildir_path), "localhost", 8025)

mailbox.start()

ignore = resources.callback(mailbox.stop)

events.get_event_loop().run_forever()
