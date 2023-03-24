curl -s https://www.boursorama.com/bourse/indices/cours/1rPCAC/ > /home/ubuntu/Projet_Linux_Git_Python/donnees.txt
CAC40_direct=$(cat /home/ubuntu/Projet_Linux_Git_Python/donnees.txt | grep -A 5 "c-faceplate c-faceplate" | grep -o -P '(?<=last&quot;:).*(?=,&quot;exchange)')
Date_CAC40_direct=$(date +"%H:%M %d|%m|%Y")
echo $Date_CAC40_direct";"$CAC40_direct >> /home/ubuntu/Projet_Linux_Git_Python/donnees.direct.csv

