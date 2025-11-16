import reflex as rx
from app.states.auth_state import AuthState


def help_step(step_number: str, title: str, description: str) -> rx.Component:
    """A single step in the help modal."""
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                step_number,
                class_name="flex items-center justify-center w-8 h-8 rounded-full bg-blue-100 text-blue-600 font-bold",
            ),
            class_name="mr-4",
        ),
        rx.el.div(
            rx.el.h4(title, class_name="font-semibold text-gray-800"),
            rx.el.p(description, class_name="text-sm text-gray-600 mt-1"),
        ),
        class_name="flex items-start mb-4",
    )


def help_modal() -> rx.Component:
    """A modal dialog explaining how to use PayMatcher."""
    return rx.radix.primitives.dialog.portal(
        rx.radix.primitives.dialog.overlay(
            class_name="fixed inset-0 bg-black/30 backdrop-blur-sm z-50"
        ),
        rx.radix.primitives.dialog.content(
            rx.radix.primitives.dialog.title(
                "How to Use PayMatcher",
                class_name="text-2xl font-bold text-gray-900 mb-6 border-b pb-4 flex items-center gap-3",
            ),
            rx.el.div(
                help_step(
                    "1",
                    "Register & Login",
                    "Create an account or sign in to get started. This gives you access to your personal dashboard.",
                ),
                help_step(
                    "2",
                    "Create an Event",
                    "Define a new event for which you want to track payments. Give it a name, date, and description.",
                ),
                help_step(
                    "3",
                    "Link Google Form",
                    "Connect a Google Form to your event. PayMatcher will watch for new submissions to verify payments against.",
                ),
                help_step(
                    "4",
                    "Link Transaction SMS",
                    "Forward your payment confirmation SMS messages to your unique PayMatcher phone number. This is how we know a payment has been made.",
                ),
                help_step(
                    "5",
                    "Automatic Verification",
                    "PayMatcher automatically cross-references incoming payments with Google Form submissions and marks them as verified in your dashboard.",
                ),
                class_name="max-h-[60vh] overflow-y-auto p-1",
            ),
            rx.el.div(
                rx.radix.primitives.dialog.close(
                    rx.el.button(
                        "Close",
                        class_name="mt-6 w-full px-4 py-2 bg-gray-200 text-gray-800 font-semibold rounded-lg hover:bg-gray-300 transition-colors",
                    )
                ),
                class_name="mt-4",
            ),
            class_name="fixed top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-8 rounded-xl shadow-2xl w-full max-w-lg z-50",
        ),
    )