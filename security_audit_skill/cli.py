from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from .branding import ATTRIBUTION, EMAIL, WEBSITE, banner_text, text_has_attribution, text_has_logo_reference
from .redaction import redact_text
from .validators import ValidationResult, validate_finding_file, validate_scope_file


def _print_brand_banner() -> None:
    rule = "=" * 60
    print(rule)
    print(banner_text())
    print(rule)


def _print_result(result: ValidationResult) -> int:
    for error in result.errors:
        print(f"ERROR: {error}")
    for warning in result.warnings:
        print(f"WARNING: {warning}")
    if result.ok:
        print("VALID")
        return 0
    print("INVALID")
    return 1


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def cmd_init(args: argparse.Namespace) -> int:
    target = Path(args.directory).resolve()
    if target.exists() and any(target.iterdir()) and not args.force:
        print(f"ERROR: {target} is not empty. Use --force to copy missing templates.", file=sys.stderr)
        return 2
    target.mkdir(parents=True, exist_ok=True)
    source = _repo_root() / "templates"
    for item in source.iterdir():
        destination = target / item.name
        if destination.exists() and not args.force:
            continue
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=args.force)
        else:
            shutil.copy2(item, destination)

    branding_dir = target / "branding"
    branding_dir.mkdir(parents=True, exist_ok=True)
    logo_destination = branding_dir / "BigDoor-logo-900x225.jpg"
    if not logo_destination.exists() or args.force:
        shutil.copy2(_repo_root() / "assets" / "BigDoor-logo-900x225.jpg", logo_destination)

    print(f"Initialized engagement workspace: {target}")
    print(f"Mandatory attribution: {ATTRIBUTION}")
    print("No external systems were contacted.")
    return 0


def cmd_validate_scope(args: argparse.Namespace) -> int:
    return _print_result(validate_scope_file(args.path))


def cmd_validate_finding(args: argparse.Namespace) -> int:
    return _print_result(validate_finding_file(args.path))


def cmd_validate_branding(args: argparse.Namespace) -> int:
    source = Path(args.path)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: unable to read {source}: {exc}", file=sys.stderr)
        return 2

    result = ValidationResult()
    if not text_has_attribution(text):
        result.add_error(f"Missing exact mandatory attribution: {ATTRIBUTION}")
    if args.require_logo and not text_has_logo_reference(text):
        result.add_error("Missing Bigdoor.ai logo reference")
    if WEBSITE not in text:
        result.add_warning(f"Recommended website missing: {WEBSITE}")
    if EMAIL not in text:
        result.add_warning(f"Recommended contact email missing: {EMAIL}")
    return _print_result(result)


def cmd_redact(args: argparse.Namespace) -> int:
    source = Path(args.input)
    destination = Path(args.output)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"ERROR: unable to read {source}: {exc}", file=sys.stderr)
        return 2
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(redact_text(text), encoding="utf-8")
    print(f"Wrote redacted evidence: {destination}")
    print("Review the output manually before sharing it.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="authorized-security-auditor",
        epilog=f"{ATTRIBUTION} | {WEBSITE} | {EMAIL}",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Create a local engagement workspace from templates")
    init_parser.add_argument("directory")
    init_parser.add_argument("--force", action="store_true", help="Overwrite template files that already exist")
    init_parser.set_defaults(func=cmd_init)

    scope_parser = subparsers.add_parser("validate-scope", help="Validate an engagement scope YAML file")
    scope_parser.add_argument("path")
    scope_parser.set_defaults(func=cmd_validate_scope)

    finding_parser = subparsers.add_parser("validate-finding", help="Validate a technical finding Markdown file")
    finding_parser.add_argument("path")
    finding_parser.set_defaults(func=cmd_validate_finding)

    branding_parser = subparsers.add_parser("validate-branding", help="Validate mandatory Bigdoor attribution")
    branding_parser.add_argument("path")
    branding_parser.add_argument("--require-logo", action="store_true", help="Also require a Bigdoor logo reference")
    branding_parser.set_defaults(func=cmd_validate_branding)

    redact_parser = subparsers.add_parser("redact", help="Mask common secrets and personal data in a text file")
    redact_parser.add_argument("input")
    redact_parser.add_argument("output")
    redact_parser.set_defaults(func=cmd_redact)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _print_brand_banner()
    return int(args.func(args))
