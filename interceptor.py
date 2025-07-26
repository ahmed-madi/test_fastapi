from mitmproxy import http
import datetime

# Keywords to identify login/authentication requests
LOGIN_KEYWORDS = ["login", "auth", "signin", "session"]

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
SEPARATOR = f"{YELLOW}" + "=" * 80 + f"{RESET}"


def request(flow: http.HTTPFlow) -> None:
    if any(keyword in flow.request.pretty_url.lower() for keyword in LOGIN_KEYWORDS):
        print(SEPARATOR)
        print(f"{YELLOW}[Request] {flow.request.method} {flow.request.pretty_url}{RESET}")
        print(f"Time: {datetime.datetime.now()}")
        print(f"Headers: {dict(flow.request.headers)}")
        print(f"Body:\n{flow.request.get_text()}")
        print(SEPARATOR)


def response(flow: http.HTTPFlow) -> None:
    if any(keyword in flow.request.pretty_url.lower() for keyword in LOGIN_KEYWORDS):
        status = flow.response.status_code
        success = 200 <= status < 300

        print(SEPARATOR)
        print(f"{YELLOW}[Response] {status} for {flow.request.pretty_url}{RESET}")
        print(f"Time: {datetime.datetime.now()}")
        print(f"Headers: {dict(flow.response.headers)}")
        print(f"Body:\n{flow.response.get_text()}\n")

        if success:
            print(f"{GREEN}✅✅✅ LOGIN STEP SUCCESSFUL ✅✅✅{RESET}")
        else:
            print(f"{RED}❌❌❌ LOGIN STEP FAILED ❌❌❌{RESET}")
        print(SEPARATOR)
