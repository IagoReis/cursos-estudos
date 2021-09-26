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
