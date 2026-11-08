"""Route parity: every gated page route in agent/web.py must be reachable through the
frontend Worker, i.e. its first path segment must appear in the Worker's UI_PREFIXES
(both sides carry a keep-in-sync comment). The 2026-11-09 /compare session found five
quick-win routes 404ing live because the allowlist lagged the web routes — this test
pins the contract so CI fails before the next deploy, not in a browser after it."""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _web_prefixes():
    text = (ROOT / "agent" / "web.py").read_text()
    m = re.search(r'^PREFIXES = \((.*?)\)$', text, re.M | re.S)
    assert m, "PREFIXES literal not found in agent/web.py"
    return sorted(re.findall(r'"(/[^"]+)"', m.group(1)))


def _worker_prefixes():
    text = (ROOT / "deploy" / "frontend" / "src" / "index.ts").read_text()
    m = re.search(r'const UI_PREFIXES = \[(.*?)\];', text, re.S)
    assert m, "UI_PREFIXES literal not found in the frontend worker"
    return sorted(re.findall(r'"(/[^"]+)"', m.group(1)))


def test_prefix_lists_match():
    assert _web_prefixes() == _worker_prefixes(), (
        "agent/web.py PREFIXES and the frontend Worker UI_PREFIXES drifted — "
        "keep them in sync (both files carry the keep-in-sync comment)")


def test_every_gated_page_route_is_covered():
    text = (ROOT / "agent" / "web.py").read_text()
    routes = re.findall(r'Route\("(/[^"{]+)"', text)  # literal pages only ({id} params ride a covered prefix)
    web_prefixes = tuple(_web_prefixes())
    for route in routes:
        covered = route == "/" or route.startswith(web_prefixes)
        assert covered, f"{route} is not covered by any PREFIXES entry — a live 404 is waiting"
