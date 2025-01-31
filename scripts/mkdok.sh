#!/usr/bin/env bash

HERE="$(dirname "$(readlink -f "${0}")")"
ROOT_DIR="$(dirname "${HERE}")"

cd "${ROOT_DIR}" || exit 1

# shellcheck disable=SC1091
[ -f "${ROOT_DIR}/.env" ] && . "${ROOT_DIR}/.env"

have_command() {
    command -v "${1}" >/dev/null 2>&1
}

ensure_node() {
    if ! have_command node; then
        curl -sL https://deb.nodesource.com/setup_20.x | sudo -E bash -
        sudo apt install -y nodejs
    fi
}

ensure_bun() {
    if ! have_command bun; then
        curl -fsSL https://bun.sh/install | bash
        export PATH="${HOME}/.bun/bin:${PATH}"
    else
        bun upgrade
    fi
}

make_docs() {
    # shellcheck disable=SC1091
    [ -f "${ROOT_DIR}/.venv/bin/activate" ] && . "${ROOT_DIR}/.venv/bin/activate"
    # pip install -r requirements.txt
    rm -rf site
    make docs
}

make_playground() {
    mkdir -p "${ROOT_DIR}/.local"
    rm -rf "${ROOT_DIR}/.local/playground"
    if [ !  -d "${ROOT_DIR}/.local/react" ]; then
        git clone https://github.com/waldiez/react.git -b dev "${ROOT_DIR}/.local/react"
    fi
    cd "${ROOT_DIR}/.local/react" || exit 1
    git stash && git pull
    ensure_node
    ensure_bun
    bun install
    echo 'BASE_URL="/playground/"' > .env
    bun build:web
    cp -rp ./out/static "${ROOT_DIR}/.local/playground"
    cd "${ROOT_DIR}" || exit 1
}

rsync_to_remote() {
    # only if $REMOTE_USER, $REMOTE_HOST and $REMOTE_PATH are set
    if [ -z "${REMOTE_USER}" ] || [ -z "${REMOTE_HOST}" ] || [ -z "${REMOTE_PATH}" ]; then
        return
    fi
    REMOTE_PORT="${REMOTE_PORT:-22}"
    rsync -avz --delete -e "ssh -p ${REMOTE_PORT}" "${ROOT_DIR}/site/" "${REMOTE_USER}@${REMOTE_HOST}:${REMOTE_PATH}"
}

_ONLY_PLAYGROUND=false
_INCLUDE_PLAYGROUND=false
_SYNC_TO_REMOTE=true

usage() {
    echo "Usage: $0 [options]"
    echo "Options:"
    echo "  --help, -h: show this help"
    echo "  --include-playground: also build the playground site"
    echo "  --playground: only build the playground site"
    echo "  --no-sync: do not rsync to remote"
}

while [ "${#}" -gt 0 ]; do
    case "${1}" in
        --playground)
            _ONLY_PLAYGROUND=true
            shift
            ;;
        --include-playground)
            _INCLUDE_PLAYGROUND=true
            shift
            ;;
        --no-sync)
            _SYNC_TO_REMOTE=false
            shift
            ;;
        --help|-h)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: ${1}"
            usage
            exit 1
            ;;
    esac
done

main() {
    if [ "${_ONLY_PLAYGROUND}" = "true" ]; then
        make_playground
        exit 0
    fi
    make_docs
    if [ "${_INCLUDE_PLAYGROUND}" = "true" ]; then
        make_playground
    fi
    if [ -d "${ROOT_DIR}/.local/playground" ]; then
        cp -rp "${ROOT_DIR}/.local/playground" "${ROOT_DIR}/site/playground"
    fi
    if [ "${_SYNC_TO_REMOTE}" = "true" ]; then
        rsync_to_remote
    fi
}

main
