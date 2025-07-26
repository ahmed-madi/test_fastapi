# 🕵️ FastAPI + mitmproxy Integration with Interceptor Script

This project demonstrates how to integrate [mitmproxy](https://mitmproxy.org/) with a custom Python interceptor script (`interceptor.py`) to capture and manipulate HTTP/S traffic. It's built using a Python 3.12 virtual environment with specific versions of dependencies to ensure compatibility and avoid common errors such as `ImportError: cannot import name 'get_encoding' from 'urwid.util'`.

---

## 📁 Project Structure

```
fast_api_test/
├── interceptor.py           # Your mitmproxy logic
├── README.md                # This file
├── requirements.txt         # Dependency pins
└── .venv/                   # Virtual environment (optional, ignored by Git)
```

---

## 🧰 Prerequisites

- Python 3.12 installed
- `git` installed
- `pip` installed
- Internet connection to install packages

---

## ⚙️ Full Setup Instructions (Start to Finish)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/fast_api_test.git
cd fast_api_test
```

### Step 2: Create and Activate a Virtual Environment

#### On macOS/Linux:

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

#### On Windows:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Compatible Dependencies

Install `mitmproxy` and `urwid` manually:

```bash
pip install mitmproxy<9.0.0 urwid==2.1.2
```

Or install everything from a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

> ⚠️ **Important**: `urwid` must be version `2.1.2` or older. Newer versions removed `get_encoding`, which `mitmproxy` depends on.

---

## 🧑‍💻 interceptor.py Example

Create a file named `interceptor.py` in the root directory with the following content:

```python
def request(flow):
    if "example.com" in flow.request.pretty_url:
        flow.request.headers["x-debug"] = "Intercepted"
        print(f"[+] Intercepted request to: {flow.request.pretty_url}")
```

---

## 🚀 Running mitmproxy

Make sure your virtual environment is activated, then run:

```bash
mitmproxy -s interceptor.py
```

This will:

- Start mitmproxy in terminal UI mode
- Load and execute your custom `interceptor.py` script
- Log or modify requests as they pass through the proxy

---

## 🔐 HTTPS Interception (Optional but Recommended)

mitmproxy can intercept HTTPS traffic too. To enable that:

1. Run mitmproxy:

   ```bash
   mitmproxy
   ```

2. Open your browser and go to:  
   [http://mitm.it](http://mitm.it)

3. Download and install the certificate for your operating system and browser

Now HTTPS traffic can also be intercepted and manipulated.

---

## 🛠️ Troubleshooting

### ❌ Error: `ImportError: cannot import name 'get_encoding' from 'urwid.util'`

**Cause**: `mitmproxy` is incompatible with newer versions of `urwid`.

**Fix**: Downgrade `urwid` to version 2.1.2:

```bash
pip install urwid==2.1.2
```

Make sure you’ve pinned it in `requirements.txt` if you're using one.

---

## 📦 requirements.txt Contents

If you're using a `requirements.txt` file, make sure it includes:

```
mitmproxy<9.0.0
urwid==2.1.2
```

Save it in the root of your project as `requirements.txt`.

Then install with:

```bash
pip install -r requirements.txt
```

---

## 📚 Resources

- 🧰 mitmproxy Documentation: https://docs.mitmproxy.org/
- ⚙️ urwid GitHub: https://github.com/urwid/urwid
- 🚀 FastAPI Documentation: https://fastapi.tiangolo.com/

---

## 👨‍💻 Author

**Ahmed Madi**  
GitHub: [https://github.com/your-username](https://github.com/your-username)  
Feel free to fork, modify, or contribute.

---

## 📝 License

This project is licensed under the MIT License. You can freely use, modify, and distribute it.

---

## ✅ Summary

This README gave you:

- ✅ A clean setup for mitmproxy in Python 3.12
- ✅ An interceptor script to modify HTTP requests
- ✅ Fix for the `urwid` import error
- ✅ HTTPS proxying support

You're ready to run `mitmproxy -s interceptor.py` and begin intercepting requests!

Happy hacking! 🐍🛠️
