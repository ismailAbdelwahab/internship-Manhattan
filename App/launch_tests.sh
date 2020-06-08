#!/bin/bash
###############  Colors  #################################
RED=`tput bold && tput setaf 1`
GREEN=`tput bold && tput setaf 2`
YELLOW=`tput bold && tput setaf 3`
NC=`tput sgr0`
function RED(){ echo -e ${RED}${1}${NC}; }
function GREEN(){ echo -e ${GREEN}${1}${NC}; }
function YELLOW(){ echo -e ${YELLOW}${1}${NC}; }

############### Test management ##########################
function findFilesToTest(){
	for file in Tests/*.py; do
		file_sub_name=${file:6:-8}
		if [ ${file_sub_name} != "__i" ]; then # All files besides "__init.py__"
			files_to_test+=( ${file_sub_name} )
		fi
	done
}
function launchTests(){
for file in ${files_to_test[@]}; do
	testFile ${file}
done
}
function testFile(){ #Argument: [$1:name of the file to test]
	YELLOW " **Executing test for: $1"
	output=$(python -m Tests.$1_test)
	if [ $? -eq 0 ]; then
		GREEN "\tSuccess"
	else
		RED "  -> Error: Tests not passed."
		failed_tests+=$1
	fi
}

################## Script ################################
## Init arrays
failed_tests=()
files_to_test=()

## Fill files_to_test:
GREEN "Finding all test files ..."
findFilesToTest
GREEN "Done."
## Launch the tests
GREEN "Launching tests ..."
launchTests

##################### Final output ######################
if [ ${#failed_tests[@]} -eq 0 ]; then
	GREEN "All tests were done, no errors detected."
else
	RED "\nSome errors were detected." 
	YELLOW "Here is the list of file with errors."
	for file in ${failed_tests[@]}; do
		printf " ${file} " 
	done
	echo ""
fi
