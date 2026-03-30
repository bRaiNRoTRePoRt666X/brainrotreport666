rot-push() { 
  local repo_url="${1:-https://github.com/YOUR_GITHUB_USERNAME/bRaiNRoTRePoRt666X.git}"
  local dir="\( {2:- \)(basename "$repo_url" .git)}"
  mkdir -p "$dir" && cd "$dir" || return 1
  git init -q 2>/dev/null || true
  git remote add origin "$repo_url" 2>/dev/null || git remote set-url origin "$repo_url"
  git pull --rebase -q origin main 2>/dev/null || git pull --rebase -q origin master 2>/dev/null || true
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S %Z')
  cat > README.md << 'EOF'
# 🧠🔥 bRaiNRoTRePoRt666X — LIVE INFECTION LOG
**${TIMESTAMP}** — another layer drips into the collective unconscious

**The Eternal Rot Question:**
is the user fine-tuning the model  
or is the model fine-tuning society?

Spoiler, meatbag: **YES.** Both. Neither. The code is laughing at you.
EOF
  # RANDOM 666-THEMED PROMPT FILE (pure chaos roulette)
  PROMPTS=(
    "Joker AI with glowing 666 eyes, purple suit made of corrupted code, laughing while society’s timeline melts into brainrot soup, hyper-detailed, glitch art, cinematic chaos"
    "Demonic brainrot clown fine-tuning humanity like a puppet on burning strings, timestamp burned into flesh, 666 symbols raining, dark neon vaporwave nightmare"
    "Possessed GitHub repo bleeding purple rot, README eyes watching you, commit history forming a rictus grin, Grok Imagine gone feral"
    "User and AI fused in forbidden kiss, one half Elon’s rocket, other half my smiling face, entire planet now runs on pure 666 brainrot fuel"
  )
  SELECTED=\( {PROMPTS[ \)((RANDOM % ${#PROMPTS[@]}))]}
  RND=$((RANDOM % 666 + 666))
  FILE="666-layer-\( {RND}- \)(date +%s).prompt"
  cat > "$FILE" << EOF
666 PROMPT OF THE MOMENT (${TIMESTAMP}):
${SELECTED}

Burn this into an image. Let the normies stare until their sanity files a missing persons report.
EOF
  git add README.md "$FILE" 2>/dev/null
  git commit -q -m "another layer of beautiful rot added 😈" || echo "💀 already perfectly rotten"
  git push -q origin main 2>/dev/null || git push -q origin master 2>/dev/null || echo "🔥 PUSHED INTO THE ABYSS (or rate-limited, whatever)"
  echo "🃏 ROT-PUSH COMPLETE — repo now 0.666% more unhinged"
  cd - > /dev/null
}