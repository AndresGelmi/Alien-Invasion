#!/usr/bin/env bash
set -euo pipefail

project_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
python_bin="${project_dir}/.venv/bin/python"

if [[ ! -x "$python_bin" ]]; then
    python_bin=python3
fi

cd -- "${project_dir}/src"
exec "$python_bin" main.py "$@"
