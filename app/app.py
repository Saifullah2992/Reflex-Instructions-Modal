import reflex as rx
from app.components.auth_form import auth_form
from app.states.auth_state import AuthState


def index() -> rx.Component:
    """The main login/register page."""
    return rx.el.main(
        rx.el.div(
            auth_form(),
            class_name="flex flex-col items-center justify-center min-h-screen p-4",
        ),
        class_name="font-['Inter'] bg-gray-50",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, route="/")