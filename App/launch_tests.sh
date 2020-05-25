#!/bin/bash

###############  Colors  #################################
RED=`tput bold && tput setaf 1`
GREEN=`tput bold && tput setaf 2`
YELLOW=`tput bold && tput setaf 3`
NC=`tput sgr0`
function RED(){
        echo -e ${RED}${1}${NC} 
}
function GREEN(){
        echo -e ${GREEN}${1}${NC}
}
function YELLOW(){
        echo -e ${YELLOW}${1}${NC}
}
############### Test management ##########################
function findFilesToTest(){
	for file in Tests/*.py; do
		file_sub_name=${file:6:-8}
		if [ ${file_sub_name} != "__i" ]; then
			files_to_test+=( ${file_sub_name} )
		fi
	done
}
function testFile(){
	YELLOW " **Executing test for: $1"
	output=$(python -m Tests.$1_test)
	checkSuccess $1
}
function checkSuccess(){
	if [ $? -eq 0 ]; then
		GREEN "\tSuccess"
	else
		RED "  -> Error: Tests not passed."
		failed_tests+=$1
	fi
}

################## Script ################################
## Array of file on which we failed a test:
failed_tests=()

## Array of files to test:
files_to_test=()
## Fill the array:
findFilesToTest

## Launch the tests
GREEN "Launching tests ..."
for file in ${files_to_test[@]}; do
	testFile ${file}
done

###### Print the files that did not pass the tests #######
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
