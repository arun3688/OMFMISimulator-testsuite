.PHONY: all OMSimulator clean

all: OMSimulator

OMSimulator:
	@$(MAKE) -C OMSimulator > OMSimulator.log
	@grep == OMSimulator.log

clean:
	@$(MAKE) -C OMSimulator clean
