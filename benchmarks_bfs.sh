#!/bin/bash

# Benchmark script for Sokoban solver using BFS algorithm
# Results are saved to benchmark_results_bfs.csv

LEVELS="01 02 03 04 05 06 07 08 09 10 11 12 13 14 15"
METHOD="bfs"

# Create or overwrite the results file with headers
echo "Level,Method,Success,Steps,Time(s),NodesExplored" > benchmark_results_bfs.csv

for level in $LEVELS; do
    echo "Running level $level with BFS..."
    # Run the solver and capture the output
    output=$(python3 solve.py --level $level --method $METHOD <<< "n")
    
    # Check if solution was found
    if echo "$output" | grep -q "Solution trouvée"; then
        success="Yes"
        # Extract steps, time and nodes explored
        steps=$(echo "$output" | grep "Solution trouvée" | awk '{print $6}')
        time=$(echo "$output" | grep "Temps d'exécution: " | awk '{print $3}')
        nodes=$(echo "$output" | grep "Nombre de noeuds explorés : " | awk '{print $6}')
    else
        success="No"
        steps="N/A"
        time=$(echo "$output" | grep "Temps d'exécution : " | awk '{print $3}')
        nodes=$(echo "$output" | grep "Nombre de noeuds explorés : " | awk '{print $5}')
        if [ -z "$nodes" ]; then
            nodes="N/A"
        fi
    fi
    
    # Add the results to the CSV file
    echo "$level,$METHOD,$success,$steps,$time,$nodes" >> benchmark_results_bfs.csv
    
    # Take a short break between runs
    sleep 1
done

echo "BFS Benchmark complete. Results saved to benchmark_results_bfs.csv"

# Print a summary of the results
echo -e "\nBFS Benchmark Summary:"
echo "======================="
echo "Legend: ✓ = Solved, ✗ = Not solved"
echo ""
echo "Level | Result | Time(s) | Steps | Nodes Explored"
echo "-----------------------------------------------"

while IFS=, read -r level method success steps time nodes; do
    # Skip header
    if [ "$level" = "Level" ]; then
        continue
    fi
    
    result_symbol="✗"
    if [ "$success" = "Yes" ]; then
        result_symbol="✓"
    fi
    
    printf " %2s   | %s      | %7s | %5s | %s\n" "$level" "$result_symbol" "$time" "$steps" "$nodes"
done < benchmark_results_bfs.csv

echo "======================="