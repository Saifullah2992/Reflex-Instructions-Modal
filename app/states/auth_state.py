import reflex as rx
import asyncio
from typing import Literal


class AuthState(rx.State):
    """Manages authentication state and the help modal."""

    form_type: Literal["login", "register"] = "login"
    is_help_modal_open: bool = False
    loading: bool = False
    error_message: str = ""

    @rx.event
    def set_form_type(self, form_type: Literal["login", "register"]):
        self.form_type = form_type
        self.error_message = ""

    @rx.event
    def set_is_help_modal_open(self, open: bool):
        """Sets the visibility of the help modal."""
        self.is_help_modal_open = open

    @rx.event
    async def handle_submit(self, form_data: dict):
        """Handles the form submission for both login and register."""
        self.loading = True
        self.error_message = ""
        yield
        await asyncio.sleep(2)
        if self.form_type == "login":
            if (
                form_data["email"] == "user@example.com"
                and form_data["password"] == "password"
            ):
                yield rx.redirect("/")
            else:
                self.error_message = "Invalid email or password."
        elif not form_data["email"] or not form_data["password"]:
            self.error_message = "Email and password are required."
        else:
            yield rx.toast.success("Registration successful! Please log in.")
            self.form_type = "login"
        self.loading = False