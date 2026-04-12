PYTHON ?= python3

POWER_POSING_PAGE_GENERATOR := pilots/living-knowledge-case/cases/power-posing/page/generate_page_data.py
POWER_POSING_PUBLIC_LAYER_CHECKER := scripts/check_power_posing_public_layer.py

.PHONY: check-page check-page-json power-posing-page power-posing-page-json check-public-layer power-posing-public-layer

check-page: power-posing-page

check-page-json: power-posing-page-json

check-public-layer: power-posing-public-layer

power-posing-page:
	$(PYTHON) $(POWER_POSING_PAGE_GENERATOR) --check

power-posing-page-json:
	$(PYTHON) $(POWER_POSING_PAGE_GENERATOR) --check --json-summary

power-posing-public-layer:
	$(PYTHON) $(POWER_POSING_PUBLIC_LAYER_CHECKER)
