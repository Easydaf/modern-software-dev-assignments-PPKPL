import re

_BULLET_PREFIX_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)?")
_CHECKBOX_RE = re.compile(r"^\[(?:\s|x|X)\]\s+\S")
_KEYWORD_RE = re.compile(r"^(?:TODO|ACTION|TASK|BUG|FIXME)\s*:\s*\S", re.IGNORECASE)
_MENTION_RE = re.compile(r"^@[A-Za-z0-9_][A-Za-z0-9_.-]*\b")


def extract_action_items(text: str) -> list[str]:
    results: list[str] = []
    for raw_line in text.splitlines():
        if not raw_line.strip():
            continue

        line = _BULLET_PREFIX_RE.sub("", raw_line).strip()
        if not line:
            continue

        if _CHECKBOX_RE.match(line) or _KEYWORD_RE.match(line) or _MENTION_RE.match(line):
            results.append(line)

    return results
