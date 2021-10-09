for counter in ${seq 1 255}; do
    echo "teste";
done


complemento="abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123"
header=true
footer=false
for counter in $(seq 1 5); do
    echo "header: ${header}"
    echo "footer: ${footer}"
    if [ "$header" == true ]; then
        echo "ENtrou header"
        header = false
    elif [ "$footer" == true ]; then
        echo "ENtrou footer"
        footer = false
        header = true
    else
        echo "5${complemento}"
    fi
    echo ""
done





for counter in $(seq 1 998); do
    echo "5${complemento}" >> teste.txt
done;

for counter in $(seq 1 10); do
    cat teste1k.txt >> cnab.txt
done;



complemento="abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123abc123"
header=true
footer=false
for counter in $(seq 1 11000000); do
    if [ $header = true ]; then
        echo "0${complemento}" >> teste.txt
        header=false
    elif [ $footer = true ]; then
        echo "9${complemento}" >> teste.txt
        header=true
        footer=false
    else
        echo "5${complemento}" >> teste.txt
        if ! (($RANDOM % 9)); then
            footer=true
        fi
    fi
done
if [ $footer = false ]; then
    echo "9${complemento}" >> teste.txt
    header=true
    footer=false
fi



for counter in $(seq 1 50); do
    cat teste2k.txt >> teste100k.txt
done

for counter in $(seq 1 10); do
    cat teste100k.txt >> teste1mi.txt
done

for counter in $(seq 1 15); do
    cat teste1mi.txt >> teste15mi.txt
done

for counter in $(seq 1 2); do
    cat cnab.txt >> cnab.txt
done


for counter in $(seq 1 100); do
    cat teste1k.txt >> teste100k.txt
done

for counter in $(seq 1 30); do
    cat teste1k.txt >> teste30k.txt
done

for counter in $(seq 1 10); do
    cat teste100k.txt >> teste1mi.txt
done







aws s3 cp teste15mi.txt s3://alura-reko-site/s3-lambda-running/
aws s3 cp teste1mi.txt s3://alura-reko-site/s3-lambda-running/

aws s3 rm s3://alura-reko-site/s3-lambda-running/server.txt

aws s3 rm s3://alura-reko-site/s3-lambda-running/teste15mi.txt
aws s3 rm s3://alura-reko-site/s3-lambda-running/teste1mi.txt
aws s3 rm s3://alura-reko-site/s3-lambda-running/cnab.txt

aws s3 ls s3://alura-reko-site/s3-lambda-running/cnab.txt