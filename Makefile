PYTHON ?= python3

POWER_POSING_PAGE_GENERATOR := pilots/living-knowledge-case/cases/power-posing/page/generate_page_data.py

.PHONY: check-page check-page-json power-posing-page power-posing-page-json

check-page: power-posing-page

check-page-json: power-posing-page-json

power-posing-page:
	$(PYTHON) $(POWER_POSING_PAGE_GENERATOR) --check

power-posing-page-json:
	$(PYTHON) $(POWER_POSING_PAGE_GENERATOR) --check --json-summary
