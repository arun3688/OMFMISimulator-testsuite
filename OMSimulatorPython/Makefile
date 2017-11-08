TEST = ../rtestPython -v

TESTFILES = \
cs_BouncingBall.py \
cs_HelloWorld_Reset.py \
cs_loop1.py \
cs_test1.py \
ImportExport.py \
Importxml.py \
me_BouncingBall.py \
me_HelloWorld_Reset.py \
me_loop1.py \
me_test1.py \
test2.py \
test3.py \

# Run make failingtest
FAILINGTESTFILES = \

# Dependency files that are not .py or Makefile
# Add them here or they will be cleaned.
DEPENDENCIES = \
*.py \
Makefile \
ConnectedFmu.xml \

CLEAN = `ls | grep -w -v -f deps.tmp`

.PHONY : test clean getdeps failingtest

test:
	@echo
	@echo Running tests...
	@$(TEST) $(TESTFILES)

# Cleans all files that are not listed as dependencies
clean:
	@echo $(DEPENDENCIES) | sed 's/ /\\\|/g' > deps.tmp
	@rm -rf $(CLEAN)

# Run this if you want to list out the files (dependencies).
# do it after cleaning and updating the folder
# then you can get a list of file names (which must be dependencies
# since you got them from repository + your own new files)
# then add them to the DEPENDENCIES. You can find the
# list in deps.txt
getdeps:
	@echo $(DEPENDENCIES) | sed 's/ /\\\|/g' > deps.tmp
	@echo $(CLEAN) | sed -r 's/deps.txt|deps.tmp//g' | sed 's/ / \\\n/g' > deps.txt
	@echo Dependency list saved in deps.txt.
	@echo Copy the list from deps.txt and add it to the Makefile @DEPENDENCIES

failingtest:
	@echo
	@echo Running failing tests...
	@echo
	@$(TEST) $(FAILINGTESTFILES)
