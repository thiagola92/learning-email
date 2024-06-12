from asyncio import events
from aiosmtpd.smtp import Session, Envelope, SMTP
from aiosmtpd.controller import Controller


class ExampleHandler:
    async def handle_RCPT(
        self,
        server: SMTP,
        session: Session,
        envelope: Envelope,
        address: str,
        rcpt_options: list,
    ):
        envelope.rcpt_tos.append(address)
        return "250 OK"

    async def handle_DATA(
        self,
        server: SMTP,
        session: Session,
        envelope: Envelope,
    ):
        return "250 Message accepted for delivery"


controller = Controller(ExampleHandler(), "localhost", 8025)
controller.start()

events.get_event_loop().run_forever()
