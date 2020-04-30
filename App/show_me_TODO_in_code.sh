#!/bin/bash
################## Colors ##########################
GREEN=`tput bold && tput setaf 2`
YELLOW=`tput bold && tput setaf 3`
NC=`tput sgr0`
function GREEN(){ echo -e ${GREEN}${1}${NC} ;}
function YELLOW(){  echo -e ${YELLOW}${1}${NC} ;}

################ Functions ####################
function findAllProject_sFiles(){
	my_files=$( find . -type f -not -name "*show_me_TODO*" | tr "\n" " ")
}
function catAllTODO(){
	for filename in ${my_files[@]};do
		output=$(cat ${filename} | grep TODO)
		if [ "$output" != "" ];then
			YELLOW " Todo in file: [${NC}${filename}${YELLOW}]"
			files_with_todo+=${file}
			echo "${output}" 
		fi
	done
}
################ Script ############################
my_files=()
files_with_todo=()
GREEN " **Finding project's files ..."
findAllProject_sFiles
GREEN " **Searching for TODO statements ..."
catAllTODO

if [ ${#files_with_todo[@]} -eq 0 ]; then
	GREEN "No TODO where found!"
	YELLOW "Are you sure you have nothing to do ... go back to work!"
else
	GREEN " **You can now see that you have work todo :)"
fi

