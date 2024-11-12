#!/usr/bin/env bash

REPO="https://github.com/PragyanPandeyX/pypandey.git"
CURRENT_DIR="$(pwd)"
ENV_FILE_PATH=".env"
DIR="/root/pyPandey"
BRANCH="master"  # Set to master branch

# Parse parameters
while [ $# -gt 0 ]; do
    case "$1" in
    --dir=*)
        DIR="${1#*=}" || DIR="/root/pyPandey"
        ;;
    --branch=*)
        BRANCH="${1#*=}" || BRANCH="master"  # Default to master branch
        ;;
    --env-file=*)
        ENV_FILE_PATH="${1#*=}" || ENV_FILE_PATH=".env"
        ;;
    --no-root)
        NO_ROOT=true
        ;;
    *)
        echo "Unknown parameter passed: $1"
        exit 1
        ;;
    esac
    shift
done

# Check system dependencies
check_dependencies() {
    echo "Checking dependencies..."
    
    if ! [ -x "$(command -v python3)" ] || ! [ -x "$(command -v python)" ]; then
        echo -e "Python3 isn't installed. Please install python3.8 or higher to run this bot." >&2
        exit 1
    fi
    if [ $(python3 -c "import sys; print(sys.version_info[1])") -lt 8 ]; then
        echo -e "Python 3.8 or higher is required to run this bot." >&2
        exit 1
    fi
    if ! command -v ffmpeg &>/dev/null || ! command -v mediainfo &>/dev/null || ! command -v neofetch &>/dev/null || ! command -v git &>/dev/null; then
        echo -e "Some dependencies aren't installed. Please install ffmpeg, mediainfo, neofetch, and git to run this bot." >&2
        exit 1
    fi
}

# Check Python version
check_python() {
    if ! command -v python3 &>/dev/null; then
        echo -e "Python3 isn't installed. Please install python3.8 or higher to run this bot."
        exit 1
    fi
    if [ $(python3 -c "import sys; print(sys.version_info[1])") -lt 8 ]; then
        echo -e "Python 3.8 or higher is required to run this bot."
        exit 1
    fi
}

# Clone the repository
clone_repo() {
    cd $DIR
    if [ -d $DIR ]; then
        if [ -d $DIR/.git ]; then
            echo -e "Updating Pandey ${BRANCH}... "
            cd $DIR
            git pull
            currentbranch="$(git rev-parse --abbrev-ref HEAD)"
            if [ ! $BRANCH ]; then
                export BRANCH=$currentbranch
            fi
            case $currentbranch in
            $BRANCH)
                # do nothing
                ;;
            *)
                echo -e "Switching to branch ${BRANCH}... "
                git checkout $BRANCH
                ;;
            esac
        else
            rm -rf $DIR
            exit 1
        fi
        return
    else
        mkdir -p $DIR
        echo -e "Cloning Pandey ${BRANCH}... "
        git clone -b $BRANCH $REPO $DIR
    fi
}

# Install requirements
install_requirements() {
    if [ ! -d "$DIR" ]; then
        echo "Directory $DIR does not exist. Exiting."
        exit 1
    fi
    if [ ! -f "$DIR/requirements.txt" ]; then
        echo "Missing requirements.txt. Please check the repository."
        exit 1
    fi
    pip3 install -q --upgrade pip
    echo -e "\n\nInstalling requirements... "
    pip3 install -q --no-cache-dir -r $DIR/requirements.txt
    pip3 install -q -r $DIR/resources/startup/optional-requirements.txt
}

# Install DB Requirements
install_db_requirements() {
    echo -e "\n\nInstalling DB Requirement..."
    if [ $MONGO_URI ]; then
        echo -e "   Installing MongoDB Requirements..."
        pip3 install -q pymongo[srv]
    elif [ $DATABASE_URL ]; then
        echo -e "   Installing PostgreSQL Requirements..."
        pip3 install -q psycopg2-binary
    elif [ $REDIS_URI ]; then
        echo -e "   Installing Redis Requirements..."
        pip3 install -q redis hiredis
    fi
}

# Miscellaneous installations
misc_install() {
    if [ $SETUP_PLAYWRIGHT ]
    then
        echo -e "Installing playwright."
        pip3 install playwright
        playwright install
    fi
    if [ $OKTETO_TOKEN ]; then
        echo -e "Installing Okteto-CLI... "
        curl https://get.okteto.com -sSfL | sh
    elif [ $VCBOT ]; then
        if [ -d $DIR/vcbot ]; then
            cd $DIR/vcbot
            git pull
        else
            echo -e "Cloning VCBOT.."
            git clone https://github.com/TeamPandey/VcBot $DIR/vcbot
        fi
        pip3 install pytgcalls==3.0.0.dev23 && pip3 install av -q --no-binary av
    fi
}

# Main setup function
main() {
    echo -e "Starting Pandey Setup..."
    if [ -f $ENV_FILE_PATH ]
    then
        set -a
        source <(cat $ENV_FILE_PATH | sed -e '/^#/d;/^\s*$/d' -e "s/'/'\\\''/g" -e "s/=\(.*\)/='\1'/g")
        set +a
        cp $ENV_FILE_PATH .env
    fi
    (check_dependencies)
    (check_python)
    (clone_repo)
    (install_requirements)
    (install_db_requirements)
    (misc_install)
    echo -e "\n\nSetup Completed."
}

# Run setup
if [ $NO_ROOT ]; then
    echo -e "Running with non root"
    main
else
    main
fi
