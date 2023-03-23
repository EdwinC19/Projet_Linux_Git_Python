curl -s https://www.boursorama.com/bourse/indices/cours/1rPCAC/ > /home/ubuntu/Projet_Linux_Git_Python/données.txt
CAC40_direct=$(cat /home/ubuntu/Projet_Linux_Git_Python/données.txt | grep -A 5 "c-faceplate c-faceplate--index is-positive" | grep -o -P '(?<=last&quot;:).*(?=,&quot;exchange)')
Date_CAC40_direct=$(date +"%H:%M %d|%m|%Y")
echo $Date_CAC40_direct";"$CAC40_direct >> /home/ubuntu/Projet_Linux_Git_Python/données.direct.csv

