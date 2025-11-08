# 🔧 HƯỚNG DẪN GIT WORKFLOW - TRÁNH LỖI KHI PULL CODE

## 📋 VẤN ĐỀ VỪA GẶP

### Lỗi:
```
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)
```

### Nguyên nhân:
- Bạn đã pull một branch đã được merge vào master
- Git tạo merge commit nhưng chưa hoàn tất
- Có file thay đổi chưa được commit

### Đã xử lý:
```bash
git add MANUAL_POSITION_CLOSE_SUMMARY.md
git commit -m "Complete merge and add manual position close feature"
git push origin master
```

✅ **Kết quả:** Code đã được đồng bộ thành công!

---

## 🚀 WORKFLOW CHUẨN ĐỂ TRÁNH LỖI

### 1. Trước khi pull code

```bash
# Bước 1: Kiểm tra trạng thái hiện tại
git status

# Bước 2: Nếu có thay đổi chưa commit, có 2 lựa chọn:

# Lựa chọn A: Commit thay đổi
git add .
git commit -m "Your commit message"

# Lựa chọn B: Stash thay đổi (tạm cất)
git stash save "Work in progress"
```

### 2. Pull code từ master

```bash
# Pull từ master (branch chính)
git pull origin master

# KHÔNG pull từ branch feature đã merge
# ❌ SAI: git pull origin claude/fix-reward-data-filtering-011CUuhn9tcAmwj5m18g831z
# ✅ ĐÚNG: git pull origin master
```

### 3. Sau khi pull

```bash
# Nếu đã stash, lấy lại thay đổi
git stash pop

# Kiểm tra trạng thái
git status
```

---

## 📖 CÁC LỆNH GIT QUAN TRỌNG

### Kiểm tra trạng thái

```bash
# Xem trạng thái hiện tại
git status

# Xem lịch sử commit
git log --oneline -10

# Xem các branch
git branch -a

# Xem thay đổi chưa commit
git diff

# Xem thay đổi đã staged
git diff --cached
```

### Quản lý thay đổi

```bash
# Add tất cả file
git add .

# Add file cụ thể
git add filename.py

# Commit
git commit -m "Your message"

# Add và commit cùng lúc
git commit -am "Your message"

# Sửa commit message cuối cùng
git commit --amend -m "New message"
```

### Pull và Push

```bash
# Pull từ master
git pull origin master

# Pull và rebase (tránh merge commit)
git pull --rebase origin master

# Push lên master
git push origin master

# Force push (CẨN THẬN!)
git push -f origin master
```

### Xử lý merge conflicts

```bash
# Nếu có conflict khi pull
# 1. Sửa file conflict thủ công
# 2. Add file đã sửa
git add conflicted_file.py

# 3. Commit merge
git commit -m "Resolve merge conflicts"

# Hoặc hủy merge
git merge --abort
```

### Stash (tạm cất thay đổi)

```bash
# Stash thay đổi
git stash save "Work in progress"

# Xem danh sách stash
git stash list

# Lấy lại stash cuối cùng
git stash pop

# Lấy lại stash cụ thể
git stash apply stash@{0}

# Xóa stash
git stash drop stash@{0}

# Xóa tất cả stash
git stash clear
```

### Reset và Revert

```bash
# Hủy thay đổi chưa commit
git restore filename.py

# Hủy tất cả thay đổi chưa commit
git restore .

# Unstage file (hủy git add)
git restore --staged filename.py

# Reset về commit trước (giữ thay đổi)
git reset --soft HEAD~1

# Reset về commit trước (xóa thay đổi)
git reset --hard HEAD~1

# Reset về commit cụ thể
git reset --hard commit_hash
```

---

## 🎯 WORKFLOW KHUYẾN NGHỊ

### Workflow hàng ngày:

```bash
# 1. Sáng: Pull code mới nhất
git pull origin master

# 2. Làm việc: Commit thường xuyên
git add .
git commit -m "Add feature X"

# 3. Tối: Push code lên
git push origin master
```

### Workflow khi có nhiều người cùng làm:

```bash
# 1. Tạo branch mới cho feature
git checkout -b feature/your-feature-name

# 2. Làm việc trên branch
git add .
git commit -m "Add feature"

# 3. Push branch lên
git push origin feature/your-feature-name

# 4. Tạo Pull Request trên GitHub

# 5. Sau khi merge, về master và pull
git checkout master
git pull origin master

# 6. Xóa branch local
git branch -d feature/your-feature-name
```

---

## ⚠️ CÁC LỖI THƯỜNG GẶP VÀ CÁCH XỬ LÝ

### Lỗi 1: "Your branch is behind"

```bash
# Nguyên nhân: Code local cũ hơn remote
# Giải pháp:
git pull origin master
```

### Lỗi 2: "Your branch is ahead"

```bash
# Nguyên nhân: Code local mới hơn remote
# Giải pháp:
git push origin master
```

### Lỗi 3: "Merge conflict"

```bash
# Nguyên nhân: Cùng sửa 1 file
# Giải pháp:
# 1. Mở file conflict
# 2. Tìm dòng có <<<<<<< HEAD
# 3. Sửa thủ công
# 4. Xóa các dấu <<<<<<<, =======, >>>>>>>
# 5. git add filename
# 6. git commit -m "Resolve conflict"
```

### Lỗi 4: "All conflicts fixed but you are still merging"

```bash
# Nguyên nhân: Merge chưa hoàn tất
# Giải pháp:
git add .
git commit -m "Complete merge"
```

### Lỗi 5: "fatal: refusing to merge unrelated histories"

```bash
# Nguyên nhân: 2 repo không liên quan
# Giải pháp:
git pull origin master --allow-unrelated-histories
```

### Lỗi 6: "Permission denied (publickey)"

```bash
# Nguyên nhân: Chưa setup SSH key
# Giải pháp:
# 1. Tạo SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# 2. Copy public key
cat ~/.ssh/id_ed25519.pub

# 3. Add vào GitHub Settings > SSH Keys
```

### Lỗi 7: "LF will be replaced by CRLF"

```bash
# Nguyên nhân: Windows vs Linux line endings
# Giải pháp (không cần làm gì, chỉ là warning):
# Hoặc config:
git config --global core.autocrlf true
```

---

## 🔍 KIỂM TRA TRƯỚC KHI PULL

### Checklist:

```bash
# 1. Kiểm tra branch hiện tại
git branch
# Đảm bảo đang ở master

# 2. Kiểm tra trạng thái
git status
# Đảm bảo "working tree clean"

# 3. Kiểm tra remote
git remote -v
# Đảm bảo đúng repo

# 4. Pull
git pull origin master

# 5. Kiểm tra lại
git status
git log --oneline -5
```

---

## 📝 QUY TẮC COMMIT MESSAGE

### Format chuẩn:

```
<type>: <subject>

<body>

<footer>
```

### Types:

- `feat`: Tính năng mới
- `fix`: Sửa lỗi
- `docs`: Thay đổi tài liệu
- `style`: Format code (không ảnh hưởng logic)
- `refactor`: Refactor code
- `test`: Thêm test
- `chore`: Công việc maintenance

### Ví dụ:

```bash
git commit -m "feat: add manual position close feature"
git commit -m "fix: resolve merge conflict in market_scanner_v2.py"
git commit -m "docs: update README with new instructions"
```

---

## 🎯 BEST PRACTICES

### 1. Commit thường xuyên

```bash
# ✅ ĐÚNG: Commit nhỏ, thường xuyên
git commit -m "Add position display function"
git commit -m "Add close position logic"
git commit -m "Add confirmation prompt"

# ❌ SAI: Commit lớn, ít
git commit -m "Add everything"
```

### 2. Pull trước khi push

```bash
# ✅ ĐÚNG
git pull origin master
git push origin master

# ❌ SAI
git push origin master  # Có thể bị reject
```

### 3. Không commit file không cần thiết

```bash
# Tạo file .gitignore
echo "*.pyc" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "venv/" >> .gitignore
echo ".env" >> .gitignore

git add .gitignore
git commit -m "Add .gitignore"
```

### 4. Kiểm tra trước khi commit

```bash
# Xem thay đổi
git diff

# Xem file sẽ commit
git status

# Commit
git add .
git commit -m "Your message"
```

---

## 🚨 KHẨN CẤP: CÁCH HỦY THAO TÁC

### Hủy commit cuối cùng (giữ thay đổi)

```bash
git reset --soft HEAD~1
```

### Hủy commit cuối cùng (xóa thay đổi)

```bash
git reset --hard HEAD~1
```

### Hủy merge đang thực hiện

```bash
git merge --abort
```

### Hủy rebase đang thực hiện

```bash
git rebase --abort
```

### Khôi phục file đã xóa

```bash
git restore filename.py
```

### Khôi phục về commit cũ

```bash
# Xem lịch sử
git log --oneline

# Khôi phục
git reset --hard commit_hash
```

---

## 📞 KHI CẦN TRỢ GIÚP

### 1. Kiểm tra log chi tiết

```bash
git log --oneline --graph --all -20
```

### 2. Kiểm tra reflog (lịch sử tất cả thao tác)

```bash
git reflog
```

### 3. Backup trước khi làm gì đó nguy hiểm

```bash
# Tạo branch backup
git branch backup-$(date +%Y%m%d-%H%M%S)

# Hoặc
git stash save "Backup before dangerous operation"
```

---

## ✅ TÓM TẮT

### Workflow đơn giản nhất:

```bash
# 1. Pull code mới
git pull origin master

# 2. Làm việc
# ... code code code ...

# 3. Commit
git add .
git commit -m "Your message"

# 4. Push
git push origin master
```

### Khi gặp lỗi:

```bash
# 1. Đọc thông báo lỗi
# 2. Chạy git status
# 3. Tìm trong guide này
# 4. Hoặc hỏi AI
```

---

**Chúc bạn làm việc với Git hiệu quả! 🚀**

---

**Ngày tạo:** 2025-11-07  
**Người tạo:** AI Assistant  
**Status:** ✅ READY TO USE

