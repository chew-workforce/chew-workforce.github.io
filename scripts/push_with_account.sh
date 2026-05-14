#!/usr/bin/env bash

set -euo pipefail

account="${1:-}"

if [[ -z "${account}" ]]; then
  printf "Select GitHub account for push:\n"
  printf "  1) chew-workforce\n"
  printf "  2) fractal-rb\n"
  read -r -p "Choice [1/2]: " choice
  case "${choice}" in
    1) account="chew-workforce" ;;
    2) account="fractal-rb" ;;
    *)
      printf "Invalid choice.\n" >&2
      exit 1
      ;;
  esac
fi

remote_url="$(git remote get-url origin)"
repo_path="${remote_url#https://github.com/}"
repo_path="${repo_path#http://github.com/}"

if [[ "${repo_path}" == "${remote_url}" ]]; then
  printf "This helper currently supports HTTPS remotes only.\n" >&2
  exit 1
fi

push_url="https://github.com/${repo_path}"

printf "Pushing %s to %s\n" "${account}" "${push_url}"
git \
  -c credential.helper= \
  -c credential.interactive=always \
  -c core.askPass= \
  push "${push_url}" "HEAD:main"
