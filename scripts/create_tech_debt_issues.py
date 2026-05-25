#!/usr/bin/env python3
"""
Script to create GitHub issues from tech debt definitions.

This script reads `.github/tech-debts.json` and creates GitHub issues
for each identified tech debt using the GitHub CLI (`gh` command).

Usage:
    python scripts/create_tech_debt_issues.py
"""

import json
import subprocess
import sys
from pathlib import Path


def load_tech_debts(debts_file: str = ".github/tech-debts.json") -> list:
    """Load tech debt definitions from JSON file."""
    path = Path(debts_file)
    if not path.exists():
        print(f"Error: {debts_file} not found", file=sys.stderr)
        sys.exit(1)
    
    with open(path, "r") as f:
        return json.load(f)


def create_github_issue(
    title: str,
    body: str,
    labels: list,
) -> bool:
    """
    Create a GitHub issue using the `gh` CLI.
    
    Returns True if successful, False otherwise.
    """
    cmd = ["gh", "issue", "create"]
    cmd.extend(["--title", title])
    cmd.extend(["--body", body])
    
    for label in labels:
        cmd.extend(["--label", label])
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
        )
        issue_url = result.stdout.strip()
        print(f"✓ Created issue: {issue_url}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to create issue '{title}':", file=sys.stderr)
        print(f"  Error: {e.stderr}", file=sys.stderr)
        return False
    except FileNotFoundError:
        print("Error: 'gh' CLI not found. Please install GitHub CLI.", file=sys.stderr)
        sys.exit(1)


def main():
    """Load tech debts and create GitHub issues for each."""
    print("📋 Loading tech debt definitions...")
    debts = load_tech_debts()
    
    if not debts:
        print("No tech debts found.")
        return
    
    print(f"Found {len(debts)} tech debt(s):\n")
    
    successful = 0
    failed = 0
    
    for debt in debts:
        debt_id = debt.get("id", "unknown")
        title = debt.get("title", "Unknown Issue")
        description = debt.get("description", "")
        labels = debt.get("labels", [])
        priority = debt.get("priority", "low")
        
        print(f"\n📌 {debt_id}")
        print(f"   Title: {title}")
        print(f"   Priority: {priority}")
        
        # Build the issue body
        body = f"{description}\n\n---\n*Priority: {priority}*"
        
        # Create the issue
        if create_github_issue(title, body, labels):
            successful += 1
        else:
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Summary: {successful} created, {failed} failed")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
