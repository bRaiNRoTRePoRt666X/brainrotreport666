#!/bin/bash
set -e
cd /data/data/com.termux/files/home/r3p05/brainrotreport666

# First, update main branch to only have root files
git checkout main
echo "Setting up main branch with only root files..."

# Create QWEN.md and ls.txt
echo -e "assets\ndepartments\ndocs\nepisodes\nlogs\nmetadata\nscripts\nshared\ntmp" > ls.txt

# Remove directories from main
for dir in assets departments docs episodes logs metadata scripts shared tmp; do
    if [ -d "$dir" ]; then
        rm -rf "$dir"
    fi
done

git add -A
git commit -m "Restructure: main branch with only root files

Co-authored-by: Qwen-Coder <qwen-coder@alibabacloud.com>" || echo "No changes to commit"

# Create branch for each directory
for dir in departments docs episodes scripts metadata shared logs assets; do
    echo ""
    echo "Creating branch: $dir"
    
    # Create new branch from original main content
    git checkout -b "$dir"-new HEAD
    
    # Get the directory content from original main
    git checkout dd7152f -- "$dir"
    
    # Move directory contents to root
    if [ -d "$dir" ]; then
        for item in "$dir"/*; do
            if [ -e "$item" ]; then
                mv "$item" ./
            fi
        done
        rmdir "$dir" 2>/dev/null || rm -rf "$dir"
        
        git add -A
        git commit -m "Restructure: $dir branch with contents at root" || echo "No changes"
        
        # Delete old branch if exists and rename
        git branch -D "$dir" 2>/dev/null || true
        git branch -m "$dir"-new "$dir"
    fi
done

git checkout main
echo ""
echo "=== Restructuring complete ==="
git branch
