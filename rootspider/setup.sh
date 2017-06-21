awk '/[^!-~]/' "chinese.txt" | while read line
do
    for i in `seq ${#line}`
    do
        scrapy crawl root -a c=${line:$((i-1)):1}
    done
done
