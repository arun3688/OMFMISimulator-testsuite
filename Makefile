.PHONY: all OMSimulator clean

all: OMSimulator

OMSimulator:
	@$(MAKE) -C OMSimulator > OMSimulator.log
	@$(MAKE) -C OMSimulator clean
	@grep == OMSimulator.log

clean:
	@$(MAKE) -C OMSimulator clean
