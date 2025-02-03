#!/usr/bin/env bash

# GLOBAL VARIABLES
export PYTHONPATH=/var/app:/var/app/workers

PYTHON=/usr/local/bin/python3
ENTRYPOINT_DEPLOY=/var/app/scripts/deploy.py
ENTRYPOINT_DELETE=/var/app/scripts/delete.py
ENTRYPOINT_DEBUG=/var/app/scripts/debug.py
ENTRYPOINT_SNIPPETS=/var/app/scripts/snippets.py
PARAMS="${@:2}"

if [[ -z ${EVERYSK_ENVIRONMENT} ]]; then
    export EVERYSK_ENVIRONMENT=local
fi

run_python() {
    if [[ $1 == "debug" ]]; then
        entrypoint=${ENTRYPOINT_DEBUG}
    elif [[ $1 == "deploy" ]]; then
        entrypoint=${ENTRYPOINT_DEPLOY}
    elif [[ $1 == "delete" ]]; then
        entrypoint=${ENTRYPOINT_DELETE}
    elif [[ $1 == "snippets" ]]; then
        entrypoint=${ENTRYPOINT_SNIPPETS}
    fi

    ${PYTHON} "${entrypoint}" "${PARAMS}"
}

# Define the TESTS value if not is passed
if [[ -z ${PARAMS} ]]; then
    TESTS="scripts.tests"
else
    TESTS="${PARAMS}"
fi

github_sync(){
    if [[ ${EVERYSK_ENVIRONMENT} == "local" ]]; then
        # Fetch the latest changes from the repository
        git fetch
        # Always merge the dev branch to the current branch to ensure the latest changes of the templates.
        git merge dev
    else
        echo "Syncing with GitHub..."
        # Set the git user
        git config --global user.email "${GH_USER_EMAIL}"
        git config --global user.name "${GH_USER_NAME}"
        # Checkout the repository
        echo "Checking out the repository..."
        git checkout dev
        # Pull the latest changes
        echo "Pulling the latest changes..."
        git pull
        # Add new files to repository
        echo "Adding new files to the repository..."
        git add workers/*
        # Commit the changes
        echo "Committing the changes..."
        git commit -m "actions-runner: Update worker config file"
        # Push the changes to the repository
        echo "Pushing the changes to the repository..."
        git push -u origin dev
        echo "Changes pushed successfully!"
    fi

}

case $1 in

    shell)
        # Access ipython shell
        /usr/local/bin/ipython
    ;;

    snippets)
        # create everysk snippets
        run_python "$1"
    ;;

    deploy)
        run_python "$1"
        EXIT_CODE=$?
        if [[ $EXIT_CODE -eq 0 ]]; then
            github_sync
        else
            echo "Deployment failed, aborting git sync..."
        fi
    ;;

    delete)
        run_python "$1"
        if [[ $EXIT_CODE -eq 0 ]]; then
            github_sync
        else
            echo "Delete failed, aborting git sync..."
        fi

    ;;
    debug)
        echo "Debugging..."
        echo "${PARAMS}"

        run_python "$1"

    ;;
    tests)
        echo "Tests..."

        ${PYTHON} -W ignore -m unittest -f "${TESTS}"

    ;;
    coverage)
        echo "Coverage..."

        export PYTHONWARNINGS="ignore"
        # Run tests with coverage meassurement
        # shellcheck disable=SC2086
        /usr/local/bin/coverage run -m unittest -f ${TESTS}
        /usr/local/bin/coverage report

    ;;

    *)
        echo "Option not found, please select one of the following options: deploy, delete, debug, tests, coverage"
        exit 1
    ;;

esac
