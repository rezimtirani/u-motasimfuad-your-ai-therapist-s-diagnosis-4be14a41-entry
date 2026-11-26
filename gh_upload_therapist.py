"""Push this entry's files to its GitHub repository.

Uploads main.py and README.md to
rezimtirani/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41-entry
on the main branch through the GitHub Contents API, creating each file or
updating it in place when it already exists. Authentication comes from the
stored GitHub PAT surrogate (custom.github); no token is ever written here.

Usage:
    python3 gh_upload_therapist.py
"""

import base64
import importlib.util
import json
import os
import sys
import urllib.error
import urllib.request

OWNER = "rezimtirani"
REPO = "u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41-entry"
BRANCH = "main"
API_ROOT = "https://api.github.com"
CREDENTIALS_HELPER = "/opt/muse/skills/custom-connector-setup/bin/dynamic_credentials.py"

HERE = os.path.dirname(os.path.abspath(__file__))
PAYLOAD_FILES = ["main.py", "README.md"]


def load_surrogate_helper():
    spec = importlib.util.spec_from_file_location(
        "dynamic_credentials", CREDENTIALS_HELPER
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def authorised_request(helper, url, method="GET", payload=None):
    body = None
    headers = {"Accept": "application/vnd.github+json"}
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=body, headers=headers, method=method)
    helper.add_surrogate_to_request(
        request, "custom.github", allowed_hosts=["api.github.com"]
    )
    return request


def existing_sha(helper, path):
    url = f"{API_ROOT}/repos/{OWNER}/{REPO}/contents/{path}?ref={BRANCH}"
    try:
        with urllib.request.urlopen(authorised_request(helper, url)) as response:
            return json.loads(response.read().decode("utf-8"))["sha"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def push_one(helper, path):
    local_path = os.path.join(HERE, path)
    with open(local_path, "rb") as handle:
        encoded = base64.b64encode(handle.read()).decode("ascii")
    sha = existing_sha(helper, path)
    payload = {
        "message": f"Upload {path} for Your AI Therapist's Diagnosis entry",
        "content": encoded,
        "branch": BRANCH,
    }
    if sha:
        payload["sha"] = sha
    url = f"{API_ROOT}/repos/{OWNER}/{REPO}/contents/{path}"
    try:
        with urllib.request.urlopen(
            authorised_request(helper, url, method="PUT", payload=payload)
        ) as response:
            result = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        detail = err.read().decode("utf-8", errors="replace")
        print(f"FAILED {path}: HTTP {err.code} {detail}", file=sys.stderr)
        return False
    verb = "updated" if sha else "created"
    print(f"{verb} {path} -> {result['content']['html_url']}")
    return True


def main():
    helper = load_surrogate_helper()
    failures = [path for path in PAYLOAD_FILES if not push_one(helper, path)]
    if failures:
        print("failed uploads: " + ", ".join(failures), file=sys.stderr)
        return 1
    print("all files uploaded to %s/%s (%s)" % (OWNER, REPO, BRANCH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
