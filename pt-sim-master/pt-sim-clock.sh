echo "Welcome to PT-Sim-Clock, the enhanced page table simulator"
echo "Using input file $1"

# This is where you would run your program
python3 pt-sim-python.py --clock $1

# If it were a binary called pt-sim.x, just do
# ./pt-sim.x $1
# and it will read from stdin, as normal


