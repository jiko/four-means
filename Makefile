.PHONY: clean all more

all: more

more:
	./dash-dl.py

clean:
	rm *.pyc img/*
