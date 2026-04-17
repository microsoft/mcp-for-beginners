import sys
from pathlib import Path

# Allow `import db` / `import server` when running pytest from repo root or this folder.
_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
