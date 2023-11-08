net=$1
for i in `seq 1 100`
do
   python3 sir.py $net >>${net}_result
done
cat ${net}_result |cut -f 1,5 -d " "| python3 calc_ave.py 

