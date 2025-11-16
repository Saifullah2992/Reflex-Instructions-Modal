import reflex as rx
from app.states.auth_state import AuthState
from app.components.help_modal import help_modal


def auth_form() -> rx.Component:
    """The login/register form component."""
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "PayMatcher",
                    class_name="text-3xl font-bold bg-gradient-to-r from-blue-600 to-indigo-400 bg-clip-text text-transparent",
                ),
                rx.el.h2(
                    rx.cond(
                        AuthState.form_type == "login",
                        "Welcome Back",
                        "Create an Account",
                    ),
                    class_name="text-2xl font-bold text-gray-800 mt-2",
                ),
                rx.el.p(
                    rx.cond(
                        AuthState.form_type == "login",
                        "Sign in to access your dashboard.",
                        "Join us and start matching payments effortlessly.",
                    ),
                    class_name="text-gray-500 mt-2",
                ),
                class_name="text-center mb-8",
            ),
            rx.el.form(
                rx.el.div(
                    rx.el.label(
                        "Email", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        name="email",
                        type="email",
                        placeholder="user@example.com",
                        required=True,
                        class_name="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500",
                    ),
                    class_name="mb-4",
                ),
                rx.el.div(
                    rx.el.label(
                        "Password", class_name="text-sm font-medium text-gray-700"
                    ),
                    rx.el.input(
                        name="password",
                        type="password",
                        placeholder="••••••••",
                        required=True,
                        class_name="mt-1 w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500",
                    ),
                    class_name="mb-6",
                ),
                rx.cond(
                    AuthState.error_message != "",
                    rx.el.div(
                        rx.icon("badge_alert", class_name="w-4 h-4 mr-2"),
                        rx.el.p(AuthState.error_message),
                        class_name="flex items-center p-3 mb-4 text-sm text-red-700 bg-red-100 rounded-lg",
                    ),
                    None,
                ),
                rx.el.button(
                    rx.cond(
                        AuthState.loading,
                        rx.el.div(
                            class_name="animate-spin rounded-full h-5 w-5 border-b-2 border-white"
                        ),
                        rx.cond(AuthState.form_type == "login", "Sign In", "Register"),
                    ),
                    type="submit",
                    disabled=AuthState.loading,
                    class_name="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 transition-colors",
                ),
                on_submit=AuthState.handle_submit,
            ),
            rx.radix.primitives.dialog.root(
                rx.radix.primitives.dialog.trigger(
                    rx.el.button(
                        rx.icon("info", class_name="mr-2 h-4 w-4"),
                        "How to Use PayMatcher",
                        class_name="mt-4 w-full flex items-center justify-center px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
                    )
                ),
                help_modal(),
                open=AuthState.is_help_modal_open,
                on_open_change=AuthState.set_is_help_modal_open,
            ),
            rx.el.div(
                rx.cond(
                    AuthState.form_type == "login",
                    "Don't have an account?",
                    "Already have an account?",
                ),
                rx.el.button(
                    rx.cond(AuthState.form_type == "login", "Register", "Sign In"),
                    on_click=lambda: AuthState.set_form_type(
                        rx.cond(AuthState.form_type == "login", "register", "login")
                    ),
                    class_name="font-medium text-blue-600 hover:text-blue-500 ml-1",
                ),
                class_name="mt-6 text-center text-sm text-gray-600",
            ),
            class_name="w-full max-w-md",
        ),
        class_name="bg-white p-8 md:p-12 rounded-2xl shadow-lg border border-gray-200",
    )