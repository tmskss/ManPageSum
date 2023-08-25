commands_list=$(ls /bin /usr/bin)
for command in $commands_list; do
    echo "Downloading command $command"
    wget -r -np -k -P /Users/tmskss/Development/Component_AI_Project/man_pages https://man7.org/linux/man-pages/man1/$command.1.html
done