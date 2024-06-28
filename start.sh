command_list=()
python_pids=()
echo '[ping_graph]: program start' & 
command_list+=('[ping_graph]: program start')

if ! command -v python3 &>/dev/null; then
    echo '[ping_graph]: python3 is not installed in PATH'
    command_list+=('[ping_graph]: python3 is not installed on this machine')
    exit 1
fi

function handle_end {
    clear
    for pid in "${python_pids[@]}"; do
        kill "$pid"
	sleep 1
	if ps -p "$pid" > /dev/null; then 
            kill -9 "$pid"
        fi
    done
    for command_run in "${command_list[@]}"; do
        echo "$command_run"
    done
    echo '[ping_graph]: program end'
    exit 0
}

function start_script {
    python3 "$1" &
    python_pids+=($1)
    echo "[ping_graph]: started $1"
    comamnd_list+=("[ping_graph]: started $1")
}

trap handle_end SIGINT

python3 -c "import plotext"
if [ $? != 0 ];
then
    echo '[ping_graph]: plotext not installed, installing now' & 
    command_list+=('[ping_graph]: plotext not installed, installing now')
    python3 -m pip install plotext --user --no-warn-script-location
else 
    echo '[ping_graph]: plotext installed' &
    command_list+=('[ping_graph]: plotext installed')
fi

if [ -e data/static_ping.txt ];
then
    rm data/static_ping.txt
    echo '[ping_graph]: leftover static_ping.txt file removed' &
    command_list+=('[ping_graph]: leftover static_ping.txt file removed')
fi
if [ -e data/ping_data.csv ];
then
    rm data/ping_data.csv
    echo '[ping_graph]: leftover ping_data.csv file removed' &
    command_list+=('[ping_graph]: leftover ping_data.csv file removed')
else
    echo '[ping_graph]: failure in removing ping_data.csv' &
    command_list+=('[ping_graph]: failure in removing ping_data.csv')
fi
if [ -e data/current_ip.txt ]; 
then
    rm data/current_ip.txt
    echo '[ping_graph]: leftover current_ip.txt file removed' &
    command_list+=('[ping_graph]: leftover current_ip.txt file removed')
fi


echo '[ping_graph]: starting loggers' &
command_list+=('[ping_graph]: starting loggers')
start_script get_ping.py & 
start_script get_ip.py &
sleep 3
echo '[ping_graph]: starting display' &
command_list+=('[ping_graph]: starting display')
start_script display.py
