# Simple UNIX password authenticator 

---

This Python script demonstrates how to authenticate users on a Unix-based operating system (such as Linux or macOS) by verifying the password provided by the user against the hash stored in the system.

!!! **Disclaimer:** This is an educational script used in CTFs (Capture The Flag challenges). It accesses system authentication information and must be used with caution. Execution usually requires `root` privileges (using `sudo`) if your system uses shadow passwords (`/etc/shadow`). !!!

---

## Features

*   Prompts for a username.
*   Securely requests the password (hides input).
*   Verifies the password hash using the `passlib` library.
*   Informs whether the login attempt was successful or not.

## Prerequisites

This script requires the `passlib` library.

### Installation

You can install `passlib` using pip:

```bash
pip install passlib
/path/to/your/.venv/bin/python -m pip install passlib
