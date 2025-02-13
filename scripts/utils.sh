#!/usr/bin/env bash

WORKERS_DIR="/var/app/workers"

# Create folder structure for a new worker
create_folder_structure(){
    # Create folder with argument name
    folder_name="wk_$1"
    mkdir -p "${WORKERS_DIR}/$folder_name"

    # Copy the sample worker folder into the new worker folder
    cp -r /var/app/worker_template/* "${WORKERS_DIR}/$folder_name/"

    echo "Folder '$folder_name' created with config.json, inputs.json, and outputs.json files."
}

case $1 in
    create)
        create_folder_structure "$2"
    ;;
    *)
        echo "Invalid argument. "
    ;;
esac
