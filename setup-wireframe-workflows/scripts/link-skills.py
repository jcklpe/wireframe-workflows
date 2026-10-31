#!/usr/bin/env python3
"""Preview or create selected local agent discovery links. Python 3.9+."""
import argparse
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
CLIENTS = {"codex": ".agents/skills", "claude": ".claude/skills"}


def plan(skills, clients, override=None):
    result = []
    for client in dict.fromkeys(clients):
        dest_dir = override or Path.home() / CLIENTS[client]
        if not dest_dir.is_absolute():
            raise ValueError("Discovery directory must be absolute")
        for ancestor in (dest_dir, *dest_dir.parents):
            if ancestor.is_symlink():
                raise ValueError("Discovery path has a symlink; select its verified real path: " + str(ancestor))
            if ancestor.exists() and not ancestor.is_dir():
                raise ValueError("Discovery path has a non-directory ancestor: " + str(ancestor))
        for skill in dict.fromkeys(skills):
            source = ROOT / skill
            if source.is_symlink() or not (source / "SKILL.md").is_file():
                raise ValueError("Missing ordinary skill directory: " + str(source))
            dest = dest_dir / skill
            exists = os.path.lexists(dest)
            same = dest.is_symlink() and dest.resolve() == source
            result.append({"client": client, "skill": skill, "source": str(source), "destination": str(dest), "action": "unchanged" if same else "conflict" if exists else "create"})
    return result


def main(argv=None):
    available = sorted(p.parent.name for p in ROOT.glob("*/SKILL.md") if not p.parent.is_symlink())
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--client", choices=CLIENTS, required=True, action="append")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--skill", choices=available, action="append")
    selection.add_argument("--all", action="store_true", help="Select all Wireframe Workflows skills, not nested Project Workflows")
    parser.add_argument("--skills-dir", type=Path, help="Verified absolute discovery directory; requires one client")
    parser.add_argument("--execute", action="store_true", help="Create links; default is a read-only preview")
    args = parser.parse_args(argv)
    if args.skills_dir and len(set(args.client)) != 1:
        parser.error("--skills-dir requires exactly one client")
    completed = []
    try:
        selected = available if args.all else args.skill
        entries = plan(selected, args.client, args.skills_dir)
        if any(e["action"] == "conflict" for e in entries):
            print(json.dumps({"status": "conflict", "links": entries, "completed": []}, indent=2))
            return 1
        if args.execute:
            # Recheck the complete selection before writing; exclusive creation refuses racing destinations.
            if plan(selected, args.client, args.skills_dir) != entries:
                raise ValueError("Discovery state changed; preview again")
            for entry in entries:
                if entry["action"] != "create":
                    continue
                dest = Path(entry["destination"])
                dest.parent.mkdir(parents=True, exist_ok=True)
                # Validate ancestors again after creating directories.
                plan([entry["skill"]], [entry["client"]], dest.parent)
                dest.symlink_to(entry["source"], target_is_directory=True)
                completed.append(str(dest))
        print(json.dumps({"status": "applied" if args.execute else "preview", "links": entries, "completed": completed}, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "error": str(exc), "completed": completed}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
