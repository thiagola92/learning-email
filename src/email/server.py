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
        print("RCPT")
        print(f"{server=}")
        print(f"{server.hostname=}")
        print(f"{session=}")
        print(f"{session.authenticated=}")
        print(f"{session.extended_smtp=}")
        print(f"{session.host_name=}")
        print(f"{envelope=}")
        print(f"{envelope.mail_from=}")
        print(f"{envelope.content=}")
        print(f"{address=}")
        print(f"{rcpt_options=}")

        envelope.rcpt_tos.append(address)
        return "250 OK"

    async def handle_DATA(
        self,
        server: SMTP,
        session: Session,
        envelope: Envelope,
    ):
        print("DATA")
        print(f"{server=}")
        print(f"{server.hostname=}")
        print(f"{session=}")
        print(f"{session.authenticated=}")
        print(f"{session.extended_smtp=}")
        print(f"{session.host_name=}")
        print(f"{envelope=}")
        print(f"{envelope.mail_from=}")
        print(f"{envelope.content=}")

        return "250 Message accepted for delivery"


controller = Controller(ExampleHandler(), "localhost", port=8025)
controller.start()

events.get_event_loop().run_forever()
