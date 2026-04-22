#!/bin/bash
set -e

CONDA_BASE=/root/miniconda3
source $CONDA_BASE/etc/profile.d/conda.sh
conda activate teacher_ai

PROJECT_DIR=/root/Teacher_Assistant_AI
BACKEND_DIR=$PROJECT_DIR/backend
LOG_DIR=$BACKEND_DIR/logs

mkdir -p $LOG_DIR

export $(grep -v '^#' $BACKEND_DIR/.env | grep -v '^$' | xargs)

echo "=== Starting Teacher Assistant AI Backend Services (Production Mode) ==="
echo "DASHSCOPE_API_KEY is set: ${DASHSCOPE_API_KEY:+YES}"
echo ""

echo "[1/6] Starting Login Service (Port 5000)..."
nohup python $BACKEND_DIR/Login/login.py > $LOG_DIR/login.log 2>&1 &
LOGIN_PID=$!
echo "  PID: $LOGIN_PID"

sleep 1

echo "[2/6] Starting Paper Marking Service (Port 5001)..."
nohup python $BACKEND_DIR/Paper_marking/marking.py > $LOG_DIR/marking.log 2>&1 &
MARKING_PID=$!
echo "  PID: $MARKING_PID"

sleep 1

echo "[3/6] Starting Paper Composition Service (Port 5002)..."
nohup python $BACKEND_DIR/Paper_composition/main.py > $LOG_DIR/composition.log 2>&1 &
COMPOSITION_PID=$!
echo "  PID: $COMPOSITION_PID"

sleep 1

echo "[4/6] Starting Achievement Analysis Service (Port 5003)..."
nohup python $BACKEND_DIR/achievement_analysis/data_analyzer.py > $LOG_DIR/analysis.log 2>&1 &
ANALYSIS_PID=$!
echo "  PID: $ANALYSIS_PID"

sleep 1

echo "[5/6] Starting Code Correction Service (Port 5004)..."
nohup python $BACKEND_DIR/Code_correction/Code_correction.py > $LOG_DIR/code_correction.log 2>&1 &
CODE_PID=$!
echo "  PID: $CODE_PID"

sleep 1

echo "[6/6] Starting Prompt Arena Service (Port 5005)..."
nohup python $BACKEND_DIR/Prompt_arena/main.py > $LOG_DIR/prompt_arena.log 2>&1 &
ARENA_PID=$!
echo "  PID: $ARENA_PID"

sleep 2

echo ""
echo "=== Checking Service Status ==="

check_port() {
    local port=$1
    local name=$2
    if ss -tlnp | grep -q ":$port "; then
        echo "  [OK] $name (Port $port) is running"
    else
        echo "  [FAIL] $name (Port $port) is NOT running"
    fi
}

check_port 5000 "Login Service"
check_port 5001 "Paper Marking Service"
check_port 5002 "Paper Composition Service"
check_port 5003 "Achievement Analysis Service"
check_port 5004 "Code Correction Service"
check_port 5005 "Prompt Arena Service"

echo ""
echo "=== All Python backend services started ==="
echo "Log files are in: $LOG_DIR/"
