# Git Workflow Guide

## Quick Reference: Push Changes to GitHub

### Step 1: Check what files changed
```bash
"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe" status
```

### Step 2: Add files to staging
```bash
# Add all changed files
"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe" add .

# OR add specific files only
"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe" add FileroomLogin.py pingid_automation.py
```

### Step 3: Commit with a message
```bash
"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe" commit -m "Your commit message here"
```

### Step 4: Push to GitHub
```bash
"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe" push
```

---

## Fix Git PATH (One-Time Setup)

To use `git` directly without the full path, add Git to your system PATH:

### Option A: Add Git to PATH for Current PowerShell Session
```powershell
$env:Path += ";C:\Users\6124436\AppData\Local\Programs\Git\cmd"
```

### Option B: Restart Your Terminal/IDE (Recommended)
Simply close and reopen your terminal or VS Code. Git should work with just `git` command.

### Option C: Permanent PATH Addition (Windows)
1. Press `Win + X` and select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "System variables" or "User variables", find "Path"
5. Click "Edit"
6. Click "New"
7. Add: `C:\Users\6124436\AppData\Local\Programs\Git\cmd`
8. Click "OK" on all windows
9. Restart terminal/IDE

---

## After Fixing PATH - Simple Commands

Once Git is in your PATH, use these simpler commands:

### Complete Workflow:
```bash
# 1. Check status
git status

# 2. Add files
git add .

# 3. Commit
git commit -m "Your message"

# 4. Push
git push
```

---

## Common Git Workflows

### Workflow 1: Quick Update (All Files)
```bash
git add .
git commit -m "Updated PingID automation"
git push
```

### Workflow 2: Specific Files Only
```bash
git add FileroomLogin.py
git commit -m "Fixed login flow"
git push
```

### Workflow 3: With Status Check
```bash
git status                              # See what changed
git add .                               # Stage all changes
git commit -m "Added new features"      # Commit with message
git push                                # Push to GitHub
```

---

## Useful Git Commands

### Check Current Status
```bash
git status
```

### View Recent Commits
```bash
git log --oneline -5
```

### See What Changed in Files
```bash
git diff                    # Unstaged changes
git diff --staged          # Staged changes
```

### Undo Accidental `git add`
```bash
git reset HEAD <file>      # Unstage specific file
git reset HEAD .           # Unstage all files
```

### Pull Latest Changes (Before Pushing)
```bash
git pull origin main
```

---

## Commit Message Best Practices

Good commit messages:
- ✅ `"Added PingID MFA automation"`
- ✅ `"Fixed PIN input field detection"`
- ✅ `"Updated documentation with troubleshooting steps"`
- ✅ `"Refactored config structure for better security"`

Bad commit messages:
- ❌ `"update"`
- ❌ `"fix"`
- ❌ `"changes"`
- ❌ `"wip"`

---

## Important Reminders

### Always Check Status First
Before committing, run `git status` to see:
- What files changed
- What's staged for commit
- What's untracked

### config.py is Protected
Remember: `config.py` (with your PIN) is in `.gitignore` and will NOT be pushed to GitHub. This is intentional for security!

### Commit Often
- Make small, focused commits
- Each commit should represent one logical change
- Easier to track and revert if needed

---

## Example: Complete Push Workflow

Let's say you modified `FileroomLogin.py` and `pingid_automation.py`:

```bash
# Navigate to project directory
cd C:\PlawrightPythonTraining

# Check what changed
git status

# Output shows:
#   modified:   FileroomLogin.py
#   modified:   pingid_automation.py

# Add the changes
git add .

# Commit with descriptive message
git commit -m "Improved PingID window detection and error handling"

# Push to GitHub
git push

# Done! Changes are now on GitHub
```

---

## Troubleshooting

### "git" is not recognized
Use full path: `"C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe"`

### Authentication Required
If GitHub asks for credentials:
- Username: `tejasautomation08`
- Password: Use a Personal Access Token (not your GitHub password)
- [Create token here](https://github.com/settings/tokens)

### Push Rejected (Behind Remote)
```bash
git pull origin main    # Pull latest changes first
git push               # Then push your changes
```

### Merge Conflict
```bash
git status             # See conflicting files
# Edit files to resolve conflicts (look for <<<< ==== >>>> markers)
git add .
git commit -m "Resolved merge conflict"
git push
```

---

## Quick Cheat Sheet

| Command | What It Does |
|---------|-------------|
| `git status` | Show changed files |
| `git add .` | Stage all changes |
| `git add <file>` | Stage specific file |
| `git commit -m "msg"` | Create commit |
| `git push` | Upload to GitHub |
| `git pull` | Download from GitHub |
| `git log` | View commit history |
| `git diff` | See file changes |

---

## Setting Up Git Alias (Optional)

To make `git` work easily, add this to your PowerShell profile:

```powershell
# Open profile
notepad $PROFILE

# Add this line:
Set-Alias git "C:\Users\6124436\AppData\Local\Programs\Git\cmd\git.exe"

# Save and reload:
. $PROFILE
```

Now you can just type `git` instead of the full path!
