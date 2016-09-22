#!/bin/bash
echo "###################################################################"
echo ""
echo "ANISO feild removal -by Dr. Choi"
echo ""
echo "###################################################################"

File1=$1
echo "Your input file name is :" $File1
#Cut doesn't work cut only work of data inside input file
#Name1= $(echo $File1 | cut -f 1 -d '.')
#so used parameter expansion
Name1=${File1%.*}

echo "Please type one of the option below"
echo "ANISOU"
echo "HETATM"
echo "ATOM"
printf 'Which Feild do you want to remove?:'
read Userinput

case $Userinput in
     ANISOU)
          sed '/ANISOU/d'$File1 > ${Name1}-without-ANISOU.pdb
          echo "Your output file name is :" $Name1-without-ANISOU.pdb
          ;;
     HETATM)
          sed '/HETATM/d' $File1 > ${Name1}--without-HETATM.pdb
          echo "Your output file name is :" $Name1-without-HETATM.pdb
          ;;
     ATOM)
          sed '/ATOM/d' $File1 > ${Name1}--only-ATOM.pdb
          echo "Your output file name is :" $Name1-only-ATOM.pdb
          ;; 
     *)
          echo "Hmm, it seems you are a Ph.D student! hahaha~ Man, You should read a manual carfully."
          ;;
esac




