.PHONY: install lint test format

install:
	bash .devops/scripts/run-install.sh

lint:
	bash .devops/scripts/run-lint.sh
	bash .devops/scripts/run-type-check.sh

test:
	bash .devops/scripts/run-test.sh

format:
	bash .devops/scripts/run-format-code.sh
