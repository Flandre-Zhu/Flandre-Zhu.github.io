PANDOC  := pandoc
MATHJAX := https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js

PD_FLAGS := -s -f markdown+raw_html --mathjax=$(MATHJAX) --metadata title="problem"

MD_FILES   := $(shell find . -type f -name '*.md')
HTML_FILES := $(MD_FILES:.md=.html)

.PHONY: all clean

all: $(HTML_FILES)

%.html: %.md
	@echo "[Pandoc] $< -> $@"
	$(PANDOC) $< -o $@ $(PD_FLAGS)

clean:
	rm -f $(HTML_FILES)
