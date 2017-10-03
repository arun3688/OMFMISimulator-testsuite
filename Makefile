.PHONY: all OMSimulator difftool clean

all: OMSimulator

OMSimulator: difftool
	@$(MAKE) -C OMSimulator > OMSimulator.log
	@$(MAKE) -C OMSimulator clean
	@grep == OMSimulator.log

clean:
	@$(MAKE) -C OMSimulator clean

difftool:
	@$(MAKE) -C difftool
