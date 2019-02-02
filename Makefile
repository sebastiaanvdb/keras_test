#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR       := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
BUCKET             =
PROFILE            = default
PROJECT_NAME       = keras_test
PYTHON_INTERPRETER = python3
PI_NAME            = pi@192.168.0.240

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## ssh pi
setup_ssh:
	ssh pi@192.168.0.240

## Setup SSH tunnels
setup_tunnels:
	while True; do \
		rsync -avz -e ssh ./ $(PI_NAME):~pi/git/$(PROJECT_NAME)/; \
		sleep 1; \
	done