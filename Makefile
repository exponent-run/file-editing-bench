.PHONY: task

download:
	./scripts/download.sh

create_diffs:
	@./scripts/create_diffs.sh
